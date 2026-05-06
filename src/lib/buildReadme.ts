import type { FormState } from "./types";
import type { SectionId, TemplateId } from "./templates";
import { getTemplate } from "./templates";
import { replacePlaceholders } from "./templateFields";
import { getSectionUrl } from "./sectionLinks";

const enc = (s: string) => encodeURIComponent(s.trim());

function badge(label: string, color: string, logo?: string) {
  const l = logo ? `&logo=${encodeURIComponent(logo)}&logoColor=white` : "";
  return `![${label}](https://img.shields.io/badge/-${enc(label)}-${color}?style=for-the-badge${l})`;
}

function metricBadge(label: string, value: string | number, color: string, logo?: string) {
  const l = logo ? `&logo=${encodeURIComponent(logo)}&logoColor=white` : "";
  return `![${label}](https://img.shields.io/badge/${enc(label)}-${enc(String(value))}-${color}?style=for-the-badge${l})`;
}

function techBadge(name: string) {
  // map common names to slugs/colors
  const map: Record<string, [string, string]> = {
    react: ["61DAFB", "react"],
    nextjs: ["000000", "nextdotjs"],
    "next.js": ["000000", "nextdotjs"],
    typescript: ["3178C6", "typescript"],
    javascript: ["F7DF1E", "javascript"],
    python: ["3776AB", "python"],
    node: ["339933", "nodedotjs"],
    "node.js": ["339933", "nodedotjs"],
    tailwind: ["06B6D4", "tailwindcss"],
    tailwindcss: ["06B6D4", "tailwindcss"],
    rust: ["000000", "rust"],
    go: ["00ADD8", "go"],
    docker: ["2496ED", "docker"],
    aws: ["232F3E", "amazonaws"],
    gcp: ["4285F4", "googlecloud"],
    postgres: ["4169E1", "postgresql"],
    postgresql: ["4169E1", "postgresql"],
    mongodb: ["47A248", "mongodb"],
    redis: ["DC382D", "redis"],
    graphql: ["E10098", "graphql"],
    figma: ["F24E1E", "figma"],
    vite: ["646CFF", "vite"],
    svelte: ["FF3E00", "svelte"],
    vue: ["4FC08D", "vuedotjs"],
    solidity: ["363636", "solidity"],
    ethereum: ["3C3C3D", "ethereum"],
    tensorflow: ["FF6F00", "tensorflow"],
    pytorch: ["EE4C2C", "pytorch"],
    pandas: ["150458", "pandas"],
    numpy: ["013243", "numpy"],
  };
  const key = name.trim().toLowerCase();
  const [color, logo] = map[key] ?? ["6E40C9", key.replace(/[^a-z0-9]/g, "")];
  return badge(name, color, logo || undefined);
}

function header(form: FormState, template: TemplateId): string {
  const name = form.displayName || form.username || "Developer";
  const tagline = form.tagline || "Welcome to my profile";

  if (template === "animated") {
    const lines = [
      `${name} 👋`,
      tagline,
      form.currentlyLearning ? `Currently learning ${form.currentlyLearning}` : "",
    ].filter(Boolean).map(enc).join(";");
    return [
      `<h1 align="center">`,
      `  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=28&duration=3000&pause=800&color=A78BFA&center=true&vCenter=true&width=600&lines=${lines}" alt="Typing SVG" />`,
      `</h1>`,
      ``,
      `<p align="center"><img src="https://komarev.com/ghpvc/?username=${enc(form.username || "user")}&style=for-the-badge&color=A78BFA" alt="Profile views" /></p>`,
    ].join("\n");
  }

  if (template === "professional") {
    return [
      `<h1 align="center">${name}</h1>`,
      `<h3 align="center">${tagline}</h3>`,
      form.location ? `<p align="center">📍 ${form.location}</p>` : "",
    ].filter(Boolean).join("\n");
  }

  return [
    `# Hi there, I'm ${name} 👋`,
    ``,
    `### ${tagline}`,
  ].join("\n");
}

function about(form: FormState): string {
  const lines: string[] = ["## 🧑‍💻 About Me", ""];
  if (form.bio) lines.push(form.bio, "");
  const bullets: string[] = [];
  if (form.currentlyWorkingOn) bullets.push(`🔭 I'm currently working on **${form.currentlyWorkingOn}**`);
  if (form.currentlyLearning) bullets.push(`🌱 I'm currently learning **${form.currentlyLearning}**`);
  if (form.contributionGoals) bullets.push(`🎯 ${form.contributionGoals}`);
  if (form.email) bullets.push(`📫 Reach me at **${form.email}**`);
  if (form.funFacts && form.funFacts.length) bullets.push(`⚡ Fun fact: ${form.funFacts[0]}`);
  return lines.concat(bullets.map((b) => `- ${b}`)).join("\n");
}

function skills(form: FormState): string {
  const all = [...form.techStack, ...form.tools];
  if (!all.length) return "";
  return ["## 🛠️ Skills", "", all.map(techBadge).join(" ")].join("\n");
}

function techStack(form: FormState): string {
  if (!form.techStack.length) return "";
  return [
    "## 🚀 Tech Stack",
    "",
    `<p>${form.techStack.map(techBadge).join(" ")}</p>`,
    form.tools.length ? `\n**Tools:**\n\n<p>${form.tools.map(techBadge).join(" ")}</p>` : "",
  ].filter(Boolean).join("\n");
}

function githubStats(form: FormState): string {
  const url = getSectionUrl("githubStats", form);
  if (!url) return "";
  return [
    "## 📊 GitHub Stats",
    "",
    `<p align="center">`,
    `  <img src="${url}" alt="GitHub Stats" />`,
    `</p>`,
  ].join("\n");
}

function streak(form: FormState): string {
  const url = getSectionUrl("streak", form);
  if (!url) return "";
  return [
    "## 🔥 Streak",
    "",
    `<p align="center">`,
    `  <img src="${url}" alt="Streak Stats" />`,
    `</p>`,
  ].join("\n");
}

function topLangs(form: FormState): string {
  const url = getSectionUrl("topLangs", form);
  if (!url) return "";
  return [
    "## 💡 Top Languages",
    "",
    `<p align="center">`,
    `  <img src="${url}" alt="Top Languages" />`,
    `</p>`,
  ].join("\n");
}

function projects(form: FormState): string {
  if (!form.projects.length) return "";

  const getRepoFromUrl = (url: string): string | null => {
    try {
      const u = new URL(url);
      if (u.hostname !== "github.com") return null;
      const parts = u.pathname.split("/").filter(Boolean);
      if (parts.length < 2) return null;
      return parts[1] ?? null;
    } catch {
      return null;
    }
  };

  const cards = form.projects
    .map((p) => {
      const repo = (p.url ? getRepoFromUrl(p.url) : null) ?? (p.name ? p.name.trim() : "");
      if (!repo) return "";
      const url = getSectionUrl("projects", form, { repo });
      if (!url) return "";
      return `<img src="${url}" alt="${repo}" />`;
    })
    .filter(Boolean);

  if (!cards.length) {
    const rows = form.projects
      .map((p) => `- **[${p.name || "Project"}](${p.url || "#"})** — ${p.description || ""}`)
      .join("\n");
    return ["## 🧪 Projects", "", rows].join("\n");
  }

  return [
    "## 🧪 Projects",
    "",
    `<p align="center">${cards.join(" ")}</p>`,
  ].join("\n");
}

function socials(form: FormState): string {
  const s = form.socials;
  const items: { name: string; url: string; color: string; logo: string }[] = [];
  if (s.twitter) items.push({ name: "Twitter", url: `https://twitter.com/${s.twitter}`, color: "1DA1F2", logo: "twitter" });
  if (s.linkedin) items.push({ name: "LinkedIn", url: `https://linkedin.com/in/${s.linkedin}`, color: "0A66C2", logo: "linkedin" });
  if (s.website) items.push({ name: "Website", url: s.website, color: "0EA5E9", logo: "googlechrome" });
  if (s.youtube) items.push({ name: "YouTube", url: `https://youtube.com/@${s.youtube}`, color: "FF0000", logo: "youtube" });
  if (s.devto) items.push({ name: "DEV.to", url: `https://dev.to/${s.devto}`, color: "0A0A0A", logo: "devdotto" });
  if (s.instagram) items.push({ name: "Instagram", url: `https://instagram.com/${s.instagram}`, color: "E4405F", logo: "instagram" });
  if (form.email) items.push({ name: "Email", url: `mailto:${form.email}`, color: "EA4335", logo: "gmail" });
  if (!items.length) return "";

  const links = items
    .map((i) => `[![${i.name}](https://img.shields.io/badge/-${enc(i.name)}-${i.color}?style=for-the-badge&logo=${i.logo}&logoColor=white)](${i.url})`)
    .join(" ");
  return ["## 🌐 Connect with me", "", `<p align="center">${links}</p>`].join("\n");
}

function quote(form: FormState): string {
  if (!form.quote) return "";
  return [
    "## ✨ Quote",
    "",
    `> ${form.quote}`,
  ].join("\n");
}

function badges(form: FormState): string {
  const views = getSectionUrl("badges", form);
  return [
    "## 🏅 Badges",
    "",
    `<p align="center">${views ? `![Profile views](${views})` : ""}</p>`,
  ].join("\n");
}

function trophies(form: FormState): string {
  const url = getSectionUrl("trophies", form);
  if (!url) return "";
  return [
    "## 🏆 Trophies",
    "",
    `<p align="center">`,
    `  <img src="${url}" alt="Trophies" />`,
    `</p>`,
  ].join("\n");
}

function gifs(form: FormState): string {
  if (!form.gifs.length) return "";
  return [
    "## ✨ GIFs",
    "",
    `<p align="center">${form.gifs.map((url) => `<img src="${url}" alt="GIF" />`).join(" ")}</p>`,
  ].join("\n");
}

function footer(form: FormState): string {
  const u = form.username || "user";
  return [
    "---",
    "",
    `<p align="center">⭐ From <a href="https://github.com/${enc(u)}">${u}</a> with love</p>`,
  ].join("\n");
}

function snake(form: FormState): string {
  const url = getSectionUrl("snake", form);
  if (!url) return "";
  return [
    "## 🐍 Contribution Snake",
    "",
    `<p align="center">`,
    `  <img src="${url}" alt="github contribution grid snake animation">`,
    `</p>`,
  ].join("\n");
}

function pacman(form: FormState): string {
  const url = getSectionUrl("pacman", form);
  if (!url) return "";
  return [
    "## 👾 Pac-Man Contribution Graph",
    "",
    `<p align="center">`,
    `  <img src="${url}" alt="pacman contribution graph">`,
    `</p>`,
  ].join("\n");
}

function skyline(form: FormState): string {
  const u = form.username || "octocat";
  return [
    "## 🌆 3D Contribution Skyline",
    "",
    `<p align="center">`,
    `  <img src="https://raw.githubusercontent.com/${enc(u)}/${enc(u)}/main/profile-3d-contrib/profile-night-view.svg" alt="3D Skyline">`,
    `</p>`,
  ].join("\n");
}

function grass(form: FormState): string {
  const u = form.username || "octocat";
  return [
    "## 🌱 Contribution Grass",
    "",
    `<p align="center">`,
    `  <img src="https://raw.githubusercontent.com/${enc(u)}/${enc(u)}/main/assets/fairy-of-grass.svg" alt="Fairy Grass">`,
    `</p>`,
  ].join("\n");
}

function gameOfLife(form: FormState): string {
  const u = form.username || "octocat";
  return [
    "## 🧬 Game of Life",
    "",
    `<p align="center">`,
    `  <img src="https://raw.githubusercontent.com/${enc(u)}/${enc(u)}/main/github4life.svg" alt="Game of Life">`,
    `</p>`,
  ].join("\n");
}

function pixelArt(form: FormState): string {
  const u = form.username || "octocat";
  return [
    "## 🎨 Pixel Art",
    "",
    `<p align="center">`,
    `  <img src="https://raw.githubusercontent.com/${enc(u)}/${enc(u)}/main/assets/gitart.svg" alt="Pixel Art">`,
    `</p>`,
  ].join("\n");
}

function typing(form: FormState): string {
  const lines = [
    form.role,
    form.tagline,
    form.currentlyWorkingOn ? `Building ${form.currentlyWorkingOn}` : "",
  ].filter(Boolean).map(enc).join(";");
  
  if (!lines) return "";
  
  return [
    "## ⌨️ About Me",
    "",
    `<p align="center">`,
    `  <a href="https://git.io/typing-svg">`,
    `    <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=500&size=20&pause=1000&color=0EA5E9&center=true&vCenter=true&width=500&lines=${lines}" alt="Typing SVG" />`,
    `  </a>`,
    `</p>`,
  ].join("\n");
}

function spotify(form: FormState): string {
  if (!form.socials.spotify) return "";
  const url = getSectionUrl("spotify", form);
  if (!url) return "";
  return [
    "## 🎵 Now Playing",
    "",
    `<p align="center">`,
    `  <img src="${url}" alt="Spotify" />`,
    `</p>`,
  ].join("\n");
}

function leetcode(form: FormState): string {
  if (!form.socials.leetcode) return "";
  const url = getSectionUrl("leetcode", form);
  if (!url) return "";
  return [
    "## 📈 LeetCode Stats",
    "",
    `<p align="center">`,
    `  <img src="${url}" alt="LeetCode Stats">`,
    `</p>`,
  ].join("\n");
}

function activityGraph(form: FormState): string {
  const url = getSectionUrl("activityGraph", form, { title: "Activity Graph" });
  if (!url) return "";
  return [
    "## � Activity Graph",
    "",
    `<p align="center">`,
    `  <img src="${url}" alt="Activity Graph">`,
    `</p>`,
  ].join("\n");
}

export function buildReadme(
  form: FormState,
  template: TemplateId,
  sections: SectionId[],
): string {
  const templateConfig = getTemplate(template);
  if (templateConfig.kind === "markdown" && templateConfig.content) {
    const content = templateConfig.content;
    const sectionContent: Record<string, string> = {};
    const regex = /<!-- SECTION:([a-zA-Z0-9_-]+) -->([\s\S]*?)<!-- \/SECTION:\1 -->/g;
    let match;
    let hasSections = false;
    
    while ((match = regex.exec(content)) !== null) {
      hasSections = true;
      sectionContent[match[1]] = match[2].trim();
    }
    
    if (!hasSections) {
      return replacePlaceholders(content, form);
    }
    
    const result = sections
      .map(id => sectionContent[id])
      .filter(Boolean)
      .join("\n\n");
      
    return replacePlaceholders(result, form);
  }

  const builders: Record<SectionId, () => string> = {
    header: () => header(form, template),
    typing: () => typing(form),
    about: () => about(form),
    skills: () => skills(form),
    techStack: () => techStack(form),
    githubStats: () => githubStats(form),
    leetcode: () => leetcode(form),
    activityGraph: () => activityGraph(form),
    streak: () => streak(form),
    topLangs: () => topLangs(form),
    projects: () => projects(form),
    snake: () => snake(form),
    pacman: () => pacman(form),
    skyline: () => skyline(form),
    grass: () => grass(form),
    gameOfLife: () => gameOfLife(form),
    pixelArt: () => pixelArt(form),
    spotify: () => spotify(form),
    socials: () => socials(form),
    quote: () => quote(form),
    badges: () => badges(form),
    trophies: () => trophies(form),
    gifs: () => gifs(form),
    footer: () => footer(form),
  };

  return sections
    .map((id) => builders[id]?.() ?? "")
    .filter(Boolean)
    .join("\n\n");
}
