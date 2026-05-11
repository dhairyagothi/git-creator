// api/analyze-repo.js
import Groq from "groq-sdk";

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method Not Allowed" });
  }

  const { repoUrl, userApiKey } = req.body;
  if (!repoUrl) {
    return res.status(400).json({ error: "repoUrl is required" });
  }

  // Use user-provided key if any, else fallback to GROQ_API_KEY env variable
  const apiKey = userApiKey || process.env.GROQ_API_KEY;
  if (!apiKey) {
    return res.status(400).json({
      error: "No Groq API key. Set GROQ_API_KEY in environment or pass userApiKey.",
    });
  }

  try {
    // 1. Extract owner/repo from GitHub URL
    const { owner, repoName } = parseGitHubUrl(repoUrl);

    // 2. Fetch repo metadata + file tree
    const headers = {
      "User-Agent": "git-creator-analyzer",
      ...(process.env.GITHUB_TOKEN ? { Authorization: `token ${process.env.GITHUB_TOKEN}` } : {}),
    };
    const [repoData, treeData] = await Promise.all([
      fetch(`https://api.github.com/repos/${owner}/${repoName}`, { headers }).then(r => r.json()),
      fetch(`https://api.github.com/repos/${owner}/${repoName}/git/trees/main?recursive=1`, { headers }).then(r => r.json()),
    ]);

    if (repoData.message === "Not Found") throw new Error("Repository not found");
    const branch = repoData.default_branch || "main";
    const files = treeData.tree || [];

    // 3. Build a compact context from the repo
    const context = await buildContext(owner, repoName, branch, files, headers);

    // 4. Call Groq
    const groq = new Groq({ apiKey });
    const prompt = buildPrompt(context);
    const result = await groq.chat.completions.create({
      model: "llama-3.1-8b-instant",   // fast, cheap, reliable
      messages: [{ role: "user", content: prompt }],
      temperature: 0.7,
      max_tokens: 1024,
      response_format: { type: "json_object" },
    });

    const text = result.choices[0].message.content;

    // 5. Parse the AI’s JSON output
    const sections = parseAIResponse(text);
    return res.status(200).json(sections);
  } catch (error) {
    console.error("Analyze error:", error);
    return res.status(500).json({ error: error.message });
  }
}

// --- Helpers ---
function parseGitHubUrl(url) {
  const match = url.match(/github\.com\/([^/]+)\/([^/]+?)(?:\.git)?$/);
  if (!match) throw new Error("Invalid GitHub URL");
  return { owner: match[1], repoName: match[2] };
}

async function buildContext(owner, repoName, branch, files, fetchHeaders) {
  const manifestCandidates = ["package.json", "requirements.txt", "pom.xml", "Cargo.toml", "go.mod"];
  const mainCandidates = ["index.js", "app.js", "server.js", "app.py", "main.py", "src/index.js", "src/App.js", "main.go"];

  let manifestContent = null;
  for (const name of manifestCandidates) {
    const found = files.find(f => f.path === name);
    if (found) {
      const url = `https://raw.githubusercontent.com/${owner}/${repoName}/${branch}/${found.path}`;
      const res = await fetch(url, { headers: fetchHeaders });
      manifestContent = res.ok ? await res.text() : null;
      break;
    }
  }

  let mainContent = null;
  for (const name of mainCandidates) {
    const found = files.find(f => f.path === name);
    if (found) {
      const url = `https://raw.githubusercontent.com/${owner}/${repoName}/${branch}/${found.path}`;
      const res = await fetch(url, { headers: fetchHeaders });
      if (res.ok) {
        mainContent = await res.text();
        mainContent = mainContent.split("\n").slice(0, 200).join("\n");
        break;
      }
    }
  }

  const topDirs = [...new Set(files.map(f => f.path.split("/")[0]))]
    .filter(d => !d.startsWith("."))
    .join(", ");

  return {
    owner,
    repoName,
    topDirs,
    manifestContent: manifestContent?.substring(0, 2000),
    mainContent,
  };
}

function buildPrompt(ctx) {
  return `
You are an expert technical writer. Based on the following information about a GitHub repository, generate README content in JSON format.

Project: ${ctx.owner}/${ctx.repoName}
Top-level folders: ${ctx.topDirs}

Manifest file (package.json / requirements.txt etc.):
\`\`\`
${ctx.manifestContent || "(none)"}
\`\`\`

Main entry file (first 200 lines):
\`\`\`
${ctx.mainContent || "(none)"}
\`\`\`

Return ONLY a valid JSON object with these keys:
{
  "tagline": "a catchy one-liner",
  "description": "2-3 paragraphs describing the project, its purpose, and who it's for",
  "features": ["list", "of", "5-8", "key", "features"],
  "techStack": ["list", "of", "technology", "names", "in lowercase", "e.g. react", "tailwindcss"]
}

If you can't determine something, use an empty string or empty array. Do not include any explanations, only the JSON.
`.trim();
}

function parseAIResponse(text) {
  // Remove possible code fences
  const clean = text.replace(/```json|```/g, "").trim();
  return JSON.parse(clean);
}