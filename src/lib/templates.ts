export type TemplateId = string;
export type TemplateKind = "builder" | "markdown";

export type SectionId =
  | "header"
  | "typing"
  | "socials"
  | "techStack"
  | "githubStats"
  | "topLangs"
  | "streak"
  | "trophies"
  | "activityGraph"
  | "projects"
  | "footer"
  | "about"
  | "skills"
  | "leetcode"
  | "spotify"
  | "snake"
  | "quote"
  | "badges"
  | "profileViews"
  | "followers";

export interface Template {
  id: TemplateId;
  name: string;
  description: string;
  tags: string[];
  accent: string; // tailwind gradient classes
  defaultSections: SectionId[];
  kind: TemplateKind;
  content?: string;
  placeholders?: string[];
}

export const ALL_SECTIONS: { id: SectionId; label: string }[] = [
  { id: "header", label: "Header" },
  { id: "typing", label: "Typing SVG" },
  { id: "socials", label: "Social Links" },
  { id: "techStack", label: "Tech Stack" },
  { id: "githubStats", label: "GitHub Stats" },
  { id: "topLangs", label: "Top Languages" },
  { id: "streak", label: "Streak Stats" },
  { id: "trophies", label: "Trophies" },
  { id: "activityGraph", label: "Activity Graph" },
  { id: "projects", label: "Projects" },
  { id: "footer", label: "Footer" },
  { id: "profileViews", label: "Profile Views" },
  { id: "followers", label: "Followers Badge" },
  // Optional / Working but not default
  { id: "about", label: "About Me" },
  { id: "skills", label: "Skills" },
  { id: "leetcode", label: "LeetCode Stats" },
  { id: "spotify", label: "Spotify Now Playing" },
  { id: "snake", label: "Snake Animation" },
  { id: "quote", label: "Quote" },
  { id: "badges", label: "Badges" },
];

export const DEFAULT_PROFILE_SECTIONS: SectionId[] = [
  "header",
  "typing",
  "socials",
  "techStack",
  "githubStats",
  "topLangs",
  "streak",
  "trophies",
  "activityGraph",
  "projects",
  "footer",
];

const SECTION_IDS = ALL_SECTIONS.map((s) => s.id);
const PLACEHOLDER_REGEX = /YOUR_[A-Z0-9_]+/g;

const CATEGORY_ACCENTS: Record<string, string> = {
  minimal: "from-slate-400 to-slate-600",
  animated: "from-fuchsia-500 to-violet-500",
  fullstack: "from-cyan-400 to-blue-500",
  student: "from-emerald-400 to-teal-500",
  opensource: "from-orange-400 to-rose-500",
  "data-ai": "from-indigo-400 to-purple-500",
  web3: "from-yellow-400 to-pink-500",
  professional: "from-blue-400 to-violet-500",
  devops: "from-sky-400 to-cyan-500",
  mobile: "from-rose-400 to-amber-400",
  security: "from-red-400 to-orange-500",
  gaming: "from-lime-400 to-emerald-500",
  "ux-ui": "from-amber-400 to-fuchsia-500",
  indie: "from-teal-400 to-emerald-500",
  content: "from-purple-400 to-rose-500",
  hackathon: "from-violet-400 to-indigo-500",
  space: "from-indigo-900 via-purple-900 to-black",
  cyberpunk: "from-fuchsia-600 via-pink-600 to-blue-600",
  pastel: "from-pink-200 via-purple-200 to-blue-200",
  ocean: "from-blue-600 via-cyan-500 to-teal-400",
  sunset: "from-orange-500 via-rose-500 to-purple-600",
  forest: "from-emerald-600 via-green-500 to-teal-600",
  fire: "from-red-600 via-orange-500 to-yellow-500",
  retro: "from-yellow-600 via-orange-600 to-red-600",
  aurora: "from-green-400 via-teal-400 to-blue-500",
  matrix: "from-black via-green-900 to-black",
  gradient: "from-fuchsia-500 via-purple-500 to-blue-500",
  mono: "from-slate-700 via-slate-800 to-slate-900",
  purple: "from-purple-600 via-violet-600 to-indigo-600",
  teal: "from-teal-500 via-cyan-500 to-emerald-500",
};

const CATEGORY_ORDER = Object.keys(CATEGORY_ACCENTS);

const markdownFiles = import.meta.glob("../../md-templates/*.md", {
  as: "raw",
  eager: true,
}) as Record<string, string>;

const markdownTemplatesWithOrder = Object.entries(markdownFiles)
  .map(([path, content]) => {
    const fileName = path.split("/").pop() ?? "";
    const baseName = fileName.replace(/\.md$/i, "");
    const match = baseName.match(/^(\d+)-(.+)$/);
    const sort = match ? Number(match[1]) : 999;
    const slug = match ? match[2] : baseName;
    const category = getCategoryFromSlug(slug);
    const placeholders = extractPlaceholders(content);
    const tags = buildTags(slug, category, sort);
    return {
      id: slug,
      name: titleFromSlug(slug),
      description: descriptionFromSlug(slug, category),
      tags,
      accent: CATEGORY_ACCENTS[category] ?? "from-slate-400 to-slate-600",
      defaultSections: DEFAULT_PROFILE_SECTIONS,
      kind: "markdown",
      content,
      placeholders,
      sort,
    } as Template & { sort: number };
  })
  .sort((a, b) => a.sort - b.sort)
  .map(({ sort, ...template }) => template);

const builderTemplates: Template[] = [
  {
    id: "minimal",
    name: "Minimal Profile",
    description: "Clean, focused, no fluff. Just the essentials with elegant typography.",
    tags: ["minimal", "popular", "builder"],
    accent: "from-slate-400 to-slate-600",
    defaultSections: DEFAULT_PROFILE_SECTIONS,
    kind: "builder",
  },
  {
    id: "animated",
    name: "Animated Profile",
    description: "Typing SVG headers, animated stats and a dynamic vibe.",
    tags: ["popular", "advanced", "builder"],
    accent: "from-fuchsia-500 to-violet-500",
    defaultSections: DEFAULT_PROFILE_SECTIONS,
    kind: "builder",
  },
  {
    id: "fullstack",
    name: "Full Stack Developer",
    description: "Front-end, back-end, infra. Show off your complete toolkit.",
    tags: ["popular", "builder"],
    accent: "from-cyan-400 to-blue-500",
    defaultSections: DEFAULT_PROFILE_SECTIONS,
    kind: "builder",
  },
  {
    id: "student",
    name: "Student / Beginner",
    description: "Friendly intro for learners with goals and currently learning.",
    tags: ["minimal", "builder"],
    accent: "from-emerald-400 to-teal-500",
    defaultSections: DEFAULT_PROFILE_SECTIONS,
    kind: "builder",
  },
  {
    id: "opensource",
    name: "Open Source Contributor",
    description: "Highlight contributions, badges, and OSS projects.",
    tags: ["advanced", "builder"],
    accent: "from-orange-400 to-rose-500",
    defaultSections: DEFAULT_PROFILE_SECTIONS,
    kind: "builder",
  },
  {
    id: "data-ai",
    name: "Data / AI Developer",
    description: "Notebooks, models, and a data-driven aesthetic.",
    tags: ["advanced", "builder"],
    accent: "from-indigo-400 to-purple-500",
    defaultSections: DEFAULT_PROFILE_SECTIONS,
    kind: "builder",
  },
  {
    id: "web3",
    name: "Web3 / Blockchain Developer",
    description: "Smart contracts, dApps, and on-chain achievements.",
    tags: ["advanced", "builder"],
    accent: "from-yellow-400 to-pink-500",
    defaultSections: DEFAULT_PROFILE_SECTIONS,
    kind: "builder",
  },
  {
    id: "professional",
    name: "Professional Portfolio",
    description: "Recruiter-ready, polished and structured for impact.",
    tags: ["popular", "builder"],
    accent: "from-blue-400 to-violet-500",
    defaultSections: DEFAULT_PROFILE_SECTIONS,
    kind: "builder",
  },
];

export const TEMPLATES: Template[] = [...markdownTemplatesWithOrder, ...builderTemplates];

export function getTemplate(id: TemplateId): Template {
  return TEMPLATES.find((t) => t.id === id) ?? TEMPLATES[0];
}

export function getTemplatePlaceholders(id: TemplateId): string[] {
  return getTemplate(id).placeholders ?? [];
}

function extractPlaceholders(content: string): string[] {
  const matches = content.match(PLACEHOLDER_REGEX) ?? [];
  return Array.from(new Set(matches));
}

function buildTags(slug: string, category: string, sort: number): string[] {
  const tags = new Set<string>();
  if (category) tags.add(category);
  if (sort <= 4) tags.add("popular");
  return Array.from(tags);
}

function getCategoryFromSlug(slug: string): string {
  for (const category of CATEGORY_ORDER) {
    if (slug === category || slug.startsWith(`${category}-`)) return category;
  }
  return slug.split("-")[0] ?? "misc";
}

function titleFromSlug(slug: string): string {
  return slug
    .split("-")
    .filter(Boolean)
    .map((word) => formatWord(word))
    .join(" ");
}

function descriptionFromSlug(slug: string, category: string): string {
  const categoryLabel = titleFromSlug(category);
  if (slug === category) return `${categoryLabel} template for GitHub profile READMEs.`;
  const variant = slug.startsWith(`${category}-`) ? slug.slice(category.length + 1) : slug;
  const variantLabel = titleFromSlug(variant);
  return `${categoryLabel} template with ${variantLabel} styling.`;
}

function formatWord(word: string): string {
  const lower = word.toLowerCase();
  const overrides: Record<string, string> = {
    ai: "AI",
    ml: "ML",
    nlp: "NLP",
    sre: "SRE",
    ux: "UX",
    ui: "UI",
    web3: "Web3",
    defi: "DeFi",
    nft: "NFT",
    dao: "DAO",
    devops: "DevOps",
    opensource: "Open Source",
  };
  if (overrides[lower]) return overrides[lower];
  return lower.charAt(0).toUpperCase() + lower.slice(1);
}
