export type TemplateId =
  | "minimal"
  | "animated"
  | "fullstack"
  | "student"
  | "opensource"
  | "data-ai"
  | "web3"
  | "professional";

export type SectionId =
  | "header"
  | "about"
  | "skills"
  | "techStack"
  | "githubStats"
  | "streak"
  | "topLangs"
  | "projects"
  | "socials"
  | "quote"
  | "badges"
  | "footer";

export interface Template {
  id: TemplateId;
  name: string;
  description: string;
  tags: string[];
  accent: string; // tailwind gradient classes
  defaultSections: SectionId[];
}

export const ALL_SECTIONS: { id: SectionId; label: string }[] = [
  { id: "header", label: "Header" },
  { id: "about", label: "About Me" },
  { id: "skills", label: "Skills" },
  { id: "techStack", label: "Tech Stack" },
  { id: "githubStats", label: "GitHub Stats" },
  { id: "streak", label: "Streak Stats" },
  { id: "topLangs", label: "Top Languages" },
  { id: "projects", label: "Projects" },
  { id: "socials", label: "Social Links" },
  { id: "quote", label: "Quote" },
  { id: "badges", label: "Badges" },
  { id: "footer", label: "Footer" },
];

export const TEMPLATES: Template[] = [
  {
    id: "minimal",
    name: "Minimal Profile",
    description: "Clean, focused, no fluff. Just the essentials with elegant typography.",
    tags: ["minimal", "popular"],
    accent: "from-slate-400 to-slate-600",
    defaultSections: ["header", "about", "techStack", "socials", "footer"],
  },
  {
    id: "animated",
    name: "Animated Profile",
    description: "Typing SVG headers, animated stats and a dynamic vibe.",
    tags: ["popular", "advanced"],
    accent: "from-fuchsia-500 to-violet-500",
    defaultSections: [
      "header", "about", "techStack", "githubStats", "streak", "topLangs", "socials", "footer",
    ],
  },
  {
    id: "fullstack",
    name: "Full Stack Developer",
    description: "Front-end, back-end, infra. Show off your complete toolkit.",
    tags: ["popular"],
    accent: "from-cyan-400 to-blue-500",
    defaultSections: [
      "header", "about", "techStack", "projects", "githubStats", "topLangs", "socials", "footer",
    ],
  },
  {
    id: "student",
    name: "Student / Beginner",
    description: "Friendly intro for learners with goals and currently learning.",
    tags: ["minimal"],
    accent: "from-emerald-400 to-teal-500",
    defaultSections: ["header", "about", "skills", "githubStats", "socials", "footer"],
  },
  {
    id: "opensource",
    name: "Open Source Contributor",
    description: "Highlight contributions, badges, and OSS projects.",
    tags: ["advanced"],
    accent: "from-orange-400 to-rose-500",
    defaultSections: [
      "header", "about", "badges", "projects", "githubStats", "streak", "socials", "footer",
    ],
  },
  {
    id: "data-ai",
    name: "Data / AI Developer",
    description: "Notebooks, models, and a data-driven aesthetic.",
    tags: ["advanced"],
    accent: "from-indigo-400 to-purple-500",
    defaultSections: [
      "header", "about", "techStack", "projects", "topLangs", "quote", "socials", "footer",
    ],
  },
  {
    id: "web3",
    name: "Web3 / Blockchain Developer",
    description: "Smart contracts, dApps, and on-chain achievements.",
    tags: ["advanced"],
    accent: "from-yellow-400 to-pink-500",
    defaultSections: [
      "header", "about", "techStack", "projects", "badges", "socials", "footer",
    ],
  },
  {
    id: "professional",
    name: "Professional Portfolio",
    description: "Recruiter-ready, polished and structured for impact.",
    tags: ["popular"],
    accent: "from-blue-400 to-violet-500",
    defaultSections: [
      "header", "about", "techStack", "projects", "githubStats", "socials", "footer",
    ],
  },
];

export function getTemplate(id: TemplateId): Template {
  return TEMPLATES.find((t) => t.id === id) ?? TEMPLATES[0];
}
