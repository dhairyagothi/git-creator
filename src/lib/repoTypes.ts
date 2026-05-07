export interface RepoFormState {
  // Auto-fetched from GitHub API
  repoName: string;
  repoOwner: string;         // username
  description: string;
  stars: number;
  forks: number;
  issues: number;
  license: string;
  language: string;          // primary language from API
  topics: string[];          // repo topics from API
  
  // User fills these (minimal)
  tagline: string;           // one-line catchy description
  liveUrl: string;
  videoUrl: string;
  screenshotUrl: string;
  techStack: string[];       // auto-suggested from language, user edits
  features: string[];        // user adds 3-5 bullet points
  envVars: string[];         // e.g. ["DATABASE_URL", "JWT_SECRET"]
  apiEndpoints: { method: string; path: string; desc: string }[];
  
  repoStructure: { name: string; type: "file" | "dir" }[];
  
  // Detected automatically
  repoType: "frontend" | "fullstack" | "backend" | "library" | "cli" | "ai" | "web3" | "mobile" | "generic";
  hasBackend: boolean;       // detected from topics/language
  hasDocker: boolean;
  hasTesting: boolean;
  packageManager: "npm" | "yarn" | "pnpm" | "pip" | "cargo" | "go" | "maven";
}

export const emptyRepoForm: RepoFormState = {
  repoName: "",
  repoOwner: "",
  description: "",
  stars: 0,
  forks: 0,
  issues: 0,
  license: "MIT",
  language: "",
  topics: [],
  tagline: "",
  liveUrl: "",
  videoUrl: "",
  screenshotUrl: "",
  techStack: [],
  features: [],
  envVars: [],
  apiEndpoints: [],
  repoStructure: [],
  repoType: "generic",
  hasBackend: false,
  hasDocker: false,
  hasTesting: false,
  packageManager: "npm",
};
