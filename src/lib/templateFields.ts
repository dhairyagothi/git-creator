import type { FormState } from "./types";

const AUTO_PLACEHOLDERS: Record<string, (form: FormState) => string> = {
  YOUR_NAME: (form) => form.displayName || form.username,
  YOUR_USERNAME: (form) => form.username,
  YOUR_TAGLINE: (form) => form.tagline,
  YOUR_ROLE: (form) => form.role,
  YOUR_TITLE: (form) => form.title,
  YOUR_COMPANY: (form) => form.company,
  YOUR_FOCUS: (form) => form.focus,
  YOUR_RESEARCH_AREA: (form) => form.focus,
  YOUR_CURRENT_FOCUS: (form) => form.currentlyWorkingOn || form.focus,
  YOUR_LOCATION: (form) => form.location,
  YOUR_CITY: (form) => form.city,
  YOUR_COUNTRY: (form) => form.country,
  YOUR_EMAIL: (form) => form.email,
  YOUR_PROJECT: (form) => form.currentlyWorkingOn,
  YOUR_CURRENTLY_LEARNING: (form) => form.currentlyLearning,
  YOUR_LEARNING: (form) => form.currentlyLearning,
  YOUR_TOPICS: (form) => form.techStack.join(", "),
  YOUR_SKILLS: (form) => form.techStack.join(", "),
  YOUR_TOOLS: (form) => form.tools.join(", "),
  YOUR_TECH_1: (form) => form.techStack[0] ?? "",
  YOUR_TECH_2: (form) => form.techStack[1] ?? "",
  YOUR_PROJECT_1: (form) => form.projects[0]?.name ?? "",
  YOUR_PROJECT_2: (form) => form.projects[1]?.name ?? "",
  YOUR_PROJECT_3: (form) => form.projects[2]?.name ?? "",
  YOUR_PROJECT_4: (form) => form.projects[3]?.name ?? "",
  YOUR_PROJECT_1_DEMO: (form) => form.projects[0]?.url ?? "",
  YOUR_PROJECT_2_DEMO: (form) => form.projects[1]?.url ?? "",
  YOUR_TWITTER: (form) => form.socials.twitter,
  YOUR_LINKEDIN: (form) => form.socials.linkedin,
  YOUR_WEBSITE: (form) => form.socials.website,
  YOUR_YOUTUBE: (form) => form.socials.youtube,
  YOUR_QUOTE: (form) => form.quote,
  YOUR_FUN_FACT: (form) => form.funFacts[0] ?? "",
  YOUR_GOAL: (form) => form.contributionGoals,
  YOUR_UNIVERSITY: (form) => form.university,
  YOUR_MAJOR: (form) => form.major,
  YOUR_YEAR: (form) => form.academicYear,
  YOUR_YEARS: (form) => form.experienceYears,
  YOUR_SCHOLAR_ID: (form) => form.scholarId,
  YOUR_RESUME_URL: (form) => form.resumeUrl,
  YOUR_ACHIEVEMENT_1: (form) => form.achievements[0] ?? "",
  YOUR_ACHIEVEMENT_2: (form) => form.achievements[1] ?? "",
  YOUR_ACHIEVEMENT_3: (form) => form.achievements[2] ?? "",
  YOUR_ACHIEVEMENT_4: (form) => form.achievements[3] ?? "",
  YOUR_FUN_FACT_1: (form) => form.funFacts[0] ?? "",
  YOUR_FUN_FACT_2: (form) => form.funFacts[1] ?? "",
  YOUR_FUN_FACT_3: (form) => form.funFacts[2] ?? "",
  YOUR_FUN_FACT_4: (form) => form.funFacts[3] ?? "",
  YOUR_PROJECT_1_DESC: (form) => form.projects[0]?.description ?? "",
  YOUR_PROJECT_2_DESC: (form) => form.projects[1]?.description ?? "",
  YOUR_PROJECT_3_DESC: (form) => form.projects[2]?.description ?? "",
  YOUR_PROJECT_4_DESC: (form) => form.projects[3]?.description ?? "",
  YOUR_GIF_1: (form) => form.gifs?.[0] ?? "https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif",
  YOUR_GIF_2: (form) => form.gifs?.[1] ?? "https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif",
};

export const AUTO_PLACEHOLDER_KEYS = new Set(Object.keys(AUTO_PLACEHOLDERS));

export function resolvePlaceholderValue(form: FormState, key: string): string | undefined {
  const override = form.templateFields?.[key];
  if (override && override.trim()) return override.trim();
  const auto = AUTO_PLACEHOLDERS[key]?.(form) ?? "";
  return auto.trim() ? auto.trim() : undefined;
}

export function replacePlaceholders(content: string, form: FormState): string {
  return content.replace(/YOUR_[A-Z0-9_]+/g, (match) => resolvePlaceholderValue(form, match) ?? match);
}

export function getPlaceholderLabel(key: string): string {
  const raw = key.replace(/^YOUR_/, "");
  return raw
    .split("_")
    .filter(Boolean)
    .map((word) => formatWord(word))
    .join(" ");
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
    mrr: "MRR",
    cve: "CVE",
  };
  if (overrides[lower]) return overrides[lower];
  return lower.charAt(0).toUpperCase() + lower.slice(1);
}
