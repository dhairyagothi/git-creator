import { detectRepoType, getSectionsForType } from "./repoTemplates";
import type { RepoFormState } from "./repoTypes";

export function buildRepoReadme(form: RepoFormState, customSections?: string[]): string {
  const type = detectRepoType(form);
  const sections = customSections || getSectionsForType(type);

  const builders: Record<string, () => string> = {
    header: () => buildHeader(form),
    overview: () => buildOverview(form),
    structure: () => buildStructure(form),
    features: () => buildFeatures(form),
    techStack: () => buildTechStack(form),
    screenshots: () => buildScreenshots(form),
    demo: () => buildDemo(form),
    installation: () => buildInstallation(form),
    envVars: () => (form.envVars.length ? buildEnvVars(form) : ""),
    usage: () => buildUsage(form),
    apiEndpoints: () => (form.apiEndpoints.length ? buildAPI(form) : ""),
    aiFeatures: () => buildAIFeatures(form),
    smartContracts: () => buildWeb3(form),
    api: () => buildLibraryAPI(form),
    contributing: () => buildContributing(form),
    contributors: () => buildContributors(form),
    license: () => buildLicense(form),
    footer: () => buildFooter(form),
  };

  return sections
    .map((s) => builders[s]?.() ?? "")
    .filter(Boolean)
    .join("\n\n---\n\n");
}

function buildHeader(form: RepoFormState): string {
  const colors: Record<string, string> = {
    ai: "0:6366F1,100:A78BFA",
    web3: "0:F59E0B,100:EF4444",
    frontend: "0:38BDF8,100:818CF8",
    backend: "0:10B981,100:06B6D4",
    fullstack: "0:22D3EE,100:3B82F6",
    library: "0:8B5CF6,100:EC4899",
    cli: "0:1F2937,100:374151",
    generic: "0:7C3AED,100:0d1117",
  };
  const color = colors[form.repoType] ?? colors.generic;
  const owner = form.repoOwner || "username";
  const repo = form.repoName || "repository";

  return `<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=${color}&height=200&section=header&text=${encodeURIComponent(repo)}&fontSize=50&fontColor=fff&animation=twinkling"/>

# ${repo}
### ${form.tagline || form.description || "Project description goes here"}

[![Stars](https://img.shields.io/github/stars/${owner}/${repo}?style=for-the-badge&color=7C3AED)](https://github.com/${owner}/${repo}/stargazers)
[![Forks](https://img.shields.io/github/forks/${owner}/${repo}?style=for-the-badge&color=58A6FF)](https://github.com/${owner}/${repo}/forks)
[![Issues](https://img.shields.io/github/issues/${owner}/${repo}?style=for-the-badge&color=F59E0B)](https://github.com/${owner}/${repo}/issues)
[![License](https://img.shields.io/github/license/${owner}/${repo}?style=for-the-badge&color=10B981)](https://github.com/${owner}/${repo}/blob/main/LICENSE)
</div>`;
}

function buildOverview(form: RepoFormState): string {
  return `## 📖 Overview
${form.description || "Detailed description of the project, its purpose, and what it solves."}`;
}

function buildStructure(form: RepoFormState): string {
  if (!form.repoStructure.length) return "";
  
  const lines = form.repoStructure.map(item =>
    item.type === "dir"
      ? `│   ├── 📁 ${item.name}/`
      : `│   ├── 📄 ${item.name}`
  ).join("\n");

  return `## 📂 Project Structure

\`\`\`
${form.repoName}/
${lines}
\`\`\`
`;
}

function buildFeatures(form: RepoFormState): string {
  if (!form.features.length) return "";
  return `## ✨ Features
${form.features.map((f) => `- **${f}**`).join("\n")}`;
}

function buildTechStack(form: RepoFormState): string {
  if (!form.techStack.length) return "";
  const icons = form.techStack
    .map((t) => t.toLowerCase().replace(/[^a-z0-9]/g, ""))
    .join(",");
  return `## 🚀 Tech Stack
<p align="left">
  <img src="https://skillicons.dev/icons?i=${icons}" alt="Tech Stack" />
</p>`;
}

function buildScreenshots(form: RepoFormState): string {
  if (!form.screenshotUrl) return "";
  return `## 📸 Screenshots
<p align="center">
  <img src="${form.screenshotUrl}" alt="Screenshot" width="800" />
</p>`;
}

function buildDemo(form: RepoFormState): string {
  if (!form.liveUrl && !form.videoUrl) return "";
  const links = [];
  if (form.liveUrl) links.push(`[Live Demo](${form.liveUrl})`);
  if (form.videoUrl) links.push(`[Video Walkthrough](${form.videoUrl})`);
  return `## 🔗 Demo
${links.join(" | ")}`;
}

function buildInstallation(form: RepoFormState): string {
  const cmds: Record<string, { install: string; run: string; build: string }> = {
    npm:   { install: "npm install",   run: "npm run dev",      build: "npm run build" },
    yarn:  { install: "yarn",          run: "yarn dev",         build: "yarn build" },
    pnpm:  { install: "pnpm install",  run: "pnpm dev",         build: "pnpm build" },
    pip:   { install: "pip install -r requirements.txt", run: "python main.py", build: "python -m build" },
    cargo: { install: "cargo build",   run: "cargo run",        build: "cargo build --release" },
    go:    { install: "go mod tidy",   run: "go run .",         build: "go build -o bin/app" },
    maven: { install: "mvn install",   run: "mvn spring-boot:run", build: "mvn package" },
  };
  const c = cmds[form.packageManager] ?? cmds.npm;

  return `## ⚙️ Installation

\`\`\`bash
# Clone the repository
git clone https://github.com/${form.repoOwner}/${form.repoName}.git
cd ${form.repoName}

# Install dependencies
${c.install}
\`\`\`
${form.envVars.length ? `
\`\`\`bash
# Set up environment variables
cp .env.example .env
# Fill in your values in .env
\`\`\`` : ""}

\`\`\`bash
# Start development server
${c.run}
\`\`\``;
}

function buildEnvVars(form: RepoFormState): string {
  return `## 🔐 Environment Variables
To run this project, you will need to add the following environment variables to your .env file:

\`\`\`env
${form.envVars.map((v) => `${v}=your_value_here`).join("\n")}
\`\`\``;
}

function buildUsage(form: RepoFormState): string {
  let cmd = "npm run dev";
  if (form.packageManager === "pip") cmd = "python main.py";
  else if (form.packageManager === "cargo") cmd = "cargo run";
  else if (form.packageManager === "go") cmd = "go run main.go";
  else if (form.packageManager === "maven") cmd = "mvn spring-boot:run";

  return `## 🚀 Usage
Explain how to run or use the project.
\`\`\`bash
${cmd}
\`\`\``;
}

function buildAPI(form: RepoFormState): string {
  const rows = form.apiEndpoints
    .map((e) => `| \`${e.method}\` | \`${e.path}\` | ${e.desc} |`)
    .join("\n");
  return `## 🔌 API Endpoints
| Method | Path | Description |
| :--- | :--- | :--- |
${rows}`;
}

function buildAIFeatures(form: RepoFormState): string {
  return `## 🧠 AI Features
- Model Architecture
- Training Process
- Dataset details`;
}

function buildWeb3(form: RepoFormState): string {
  return `## ⛓️ Smart Contracts
- Contract Address (Mainnet/Testnet)
- Verification links`;
}

function buildLibraryAPI(form: RepoFormState): string {
  return `## 📚 API Reference
Detail the main functions or classes provided by this library.`;
}

function buildContributing(form: RepoFormState): string {
  return `## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.`;
}

function buildLicense(form: RepoFormState): string {
  return `## 📄 License
This project is licensed under the ${form.license} License.`;
}

function buildContributors(form: RepoFormState): string {
  return `## 👥 Contributors

<a href="https://github.com/${form.repoOwner}/${form.repoName}/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=${form.repoOwner}/${form.repoName}" />
</a>

Made with [contrib.rocks](https://contrib.rocks).`;
}

function buildFooter(form: RepoFormState): string {
  return `<div align="center">

---

⭐ Star this repo if you like it!  
Made with ❤️ by [${form.repoOwner}](https://github.com/${form.repoOwner})

<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDIzZTA4ZDYwYmJmZDA0ZTMwYmFkMzY0ZDMwYmFkMzY0ZDMwYmFkMzYmZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/3o7TKVUn7iM8FMEU24/giphy.gif" width="100" />

</div>`;
}
