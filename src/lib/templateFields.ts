import type { FormState } from "./types";

const AUTO_PLACEHOLDERS: Record<string, (form: FormState) => string> = {
  YOUR_NAME: (form) => form.displayName || form.username,
  YOUR_USERNAME: (form) => form.username,
  YOUR_GITHUB: (form) => form.username,
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
  YOUR_PROJECT_1_DEMO: (form) => encodeURI(form.projects[0]?.url ?? ""),
  YOUR_PROJECT_2_DEMO: (form) => encodeURI(form.projects[1]?.url ?? ""),
  YOUR_TWITTER: (form) => encodeURI(form.socials.twitter),
  YOUR_LINKEDIN: (form) => encodeURI(form.socials.linkedin),
  YOUR_WEBSITE: (form) => encodeURI(form.socials.website),
  YOUR_YOUTUBE: (form) => encodeURI(form.socials.youtube),
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
  YOUR_STARS: (form) => String(form.githubStats.totalStars || 0),
  YOUR_TOTAL_STARS: (form) => String(form.githubStats.totalStars || 0),
  YOUR_FOLLOWERS: (form) => String(form.githubStats.followers || 0),
  YOUR_PUBLIC_REPOS: (form) => String(form.githubStats.publicRepos || 0),
  YOUR_TOTAL_COMMITS: (form) => String(form.githubStats.totalStars || 0),
  YOUR_TOP_LANGS: (form) => form.githubStats.topLanguages.join(", "),
  YOUR_LANGUAGES: (form) => [...form.githubStats.topLanguages, ...form.techStack].slice(0, 5).join(", "),
  YOUR_FRAMEWORKS: (form) => form.techStack.join(", "),
  YOUR_DATABASES: (form) => form.tools.join(", "),
  YOUR_HOBBY_1: (form) => form.funFacts[0] ?? "",
  YOUR_HOBBY_2: (form) => form.funFacts[1] ?? "",
  YOUR_OSS_PROJECT_1: (form) => form.projects[0]?.name ?? "",
  YOUR_OSS_PROJECT_2: (form) => form.projects[1]?.name ?? "",
  YOUR_OSS_PROJECT_3: (form) => form.projects[2]?.name ?? "",
  YOUR_DESC_1: (form) => form.projects[0]?.description ?? "",
  YOUR_DESC_2: (form) => form.projects[1]?.description ?? "",
  YOUR_DESC_3: (form) => form.projects[2]?.description ?? "",
  YOUR_PROJECT_1_URL: (form) => form.projects[0]?.url ?? "",
  YOUR_PROJECT_2_URL: (form) => form.projects[1]?.url ?? "",
  YOUR_SPECIALTY: (form) => form.focus || form.role,
  YOUR_COLLAB: (form) => form.currentlyWorkingOn,
  YOUR_TEAM_SIZE: (_form) => "",
  YOUR_YEARS_: (form) => form.experienceYears,
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
  let result = content.replace(/YOUR_[A-Z0-9_]+/g, (match) => resolvePlaceholderValue(form, match) ?? match);

  // Fix skillicons spaces (skillicons API fails with spaces)
  result = result.replace(/(https:\/\/skillicons\.dev\/icons\?i=)([^&"\s>]+(?: [^&"\s>]+)*)/g, (match, p1, p2) => {
    return p1 + p2.replace(/\s+/g, '');
  });

  // Fix github-readmeapp repo names (replace spaces with hyphens for valid repo slugs)
  result = result.replace(/(&repo=)([^&"\s>]+(?: [^&"\s>]+)*)/g, (match, p1, p2) => {
    return p1 + encodeURIComponent(p2.replace(/\s+/g, '-'));
  });

  return result;
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

export interface SocialOption {
  key: keyof FormState["socials"];
  label: string;
  color: string;
  logo: string;
  urlPattern: string; // use {} as placeholder for username
}

export const SOCIAL_OPTIONS: SocialOption[] = [
  { key: "github", label: "GitHub", color: "181717", logo: "github", urlPattern: "https://github.com/{}" },
  { key: "linkedin", label: "LinkedIn", color: "0A66C2", logo: "linkedin", urlPattern: "https://linkedin.com/in/{}" },
  { key: "instagram", label: "Instagram", color: "E4405F", logo: "instagram", urlPattern: "https://instagram.com/{}" },
  { key: "twitter", label: "Twitter", color: "000000", logo: "x", urlPattern: "https://x.com/{}" },
  { key: "gmail", label: "Gmail", color: "EA4335", logo: "gmail", urlPattern: "mailto:{}" },
  { key: "youtube", label: "YouTube", color: "FF0000", logo: "youtube", urlPattern: "https://youtube.com/@{}" },
  { key: "discord", label: "Discord", color: "5865F2", logo: "discord", urlPattern: "https://discord.gg/{}" },
  { key: "telegram", label: "Telegram", color: "26A5E4", logo: "telegram", urlPattern: "https://t.me/{}" },
  { key: "website", label: "Portfolio", color: "7C3AED", logo: "googlechrome", urlPattern: "{}" },
  { key: "devto", label: "Dev.to", color: "0A0A0A", logo: "devdotto", urlPattern: "https://dev.to/{}" },
  { key: "medium", label: "Medium", color: "12100E", logo: "medium", urlPattern: "https://medium.com/@{}" },
  { key: "hashnode", label: "Hashnode", color: "2962FF", logo: "hashnode", urlPattern: "https://hashnode.com/@{}" },
  { key: "leetcode", label: "LeetCode", color: "FFA116", logo: "leetcode", urlPattern: "https://leetcode.com/u/{}" },
  { key: "hackerrank", label: "HackerRank", color: "00EA64", logo: "hackerrank", urlPattern: "https://hackerrank.com/{}" },
  { key: "codeforces", label: "Codeforces", color: "1F8ACB", logo: "codeforces", urlPattern: "https://codeforces.com/profile/{}" },
  { key: "geeksforgeeks", label: "GeeksforGeeks", color: "2F8D46", logo: "geeksforgeeks", urlPattern: "https://auth.geeksforgeeks.org/user/{}" },
  { key: "reddit", label: "Reddit", color: "FF4500", logo: "reddit", urlPattern: "https://reddit.com/u/{}" },
  { key: "spotify", label: "Spotify", color: "1DB954", logo: "spotify", urlPattern: "https://open.spotify.com/user/{}" },
  { key: "twitch", label: "Twitch", color: "9146FF", logo: "twitch", urlPattern: "https://twitch.tv/{}" },
  { key: "stackoverflow", label: "StackOverflow", color: "F58025", logo: "stackoverflow", urlPattern: "https://stackoverflow.com/users/{}" },
  { key: "facebook", label: "Facebook", color: "1877F2", logo: "facebook", urlPattern: "https://facebook.com/{}" },
];

export function getSocialBadgeMd(option: SocialOption, username: string): string {
  const url = username.startsWith("http") ? username : option.urlPattern.replace("{}", username);
  return `[![${option.label}](https://img.shields.io/badge/${option.label.replace(/\s+/g, "_")}-${option.color}?style=for-the-badge&logo=${option.logo}&logoColor=white)](${url})`;
}
