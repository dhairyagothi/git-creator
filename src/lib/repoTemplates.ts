import type { RepoFormState } from "./repoTypes";

export function detectRepoType(form: RepoFormState): RepoFormState["repoType"] {
  const lang = form.language.toLowerCase();
  const topics = form.topics.map((t) => t.toLowerCase());
  const stack = form.techStack.map((t) => t.toLowerCase());

  // AI/ML detection
  if (
    topics.some((t) =>
      ["ai", "ml", "llm", "nlp", "deep-learning", "pytorch", "tensorflow"].includes(t),
    ) ||
    stack.some((t) => ["pytorch", "tensorflow", "openai", "langchain"].includes(t))
  )
    return "ai";

  // Web3
  if (
    topics.some((t) => ["web3", "solidity", "ethereum", "blockchain", "defi", "nft"].includes(t)) ||
    stack.some((t) => ["solidity", "ethers", "hardhat", "foundry"].includes(t))
  )
    return "web3";

  // Mobile
  if (
    topics.some((t) => ["ios", "android", "flutter", "react-native"].includes(t)) ||
    stack.some((t) => ["flutter", "swift", "kotlin", "expo"].includes(t))
  )
    return "mobile";

  // CLI tool
  if (topics.includes("cli") || lang === "rust" || lang === "go") return "cli";

  // Library/package
  if (topics.some((t) => ["library", "package", "sdk", "npm"].includes(t))) return "library";

  // Backend only
  if (
    lang === "python" ||
    lang === "go" ||
    lang === "rust" ||
    topics.some((t) => ["api", "backend", "microservice"].includes(t))
  )
    return "backend";

  // Fullstack
  if (form.hasBackend && stack.some((t) => ["react", "vue", "next", "angular"].includes(t)))
    return "fullstack";

  // Frontend
  if (stack.some((t) => ["react", "vue", "next", "svelte", "angular"].includes(t))) return "frontend";

  return "generic";
}

export const REPO_SECTIONS: { id: string; label: string }[] = [
  { id: "header", label: "Header & Badges" },
  { id: "overview", label: "Overview" },
  { id: "features", label: "Features" },
  { id: "techStack", label: "Tech Stack" },
  { id: "screenshots", label: "Screenshots" },
  { id: "demo", label: "Live Demo" },
  { id: "structure", label: "Repo Structure" },
  { id: "installation", label: "Installation" },
  { id: "envVars", label: "Environment Variables" },
  { id: "usage", label: "Usage" },
  { id: "apiEndpoints", label: "API Endpoints" },
  { id: "aiFeatures", label: "AI Features" },
  { id: "contributing", label: "Contributing" },
  { id: "contributors", label: "Contributors" },
  { id: "license", label: "License" },
  { id: "footer", label: "Footer Note" },
];

// Returns different template sections based on type
export function getSectionsForType(type: RepoFormState["repoType"]): string[] {
  const base = ["header", "overview", "structure", "features", "techStack", "screenshots", "demo"];
  const maps: Record<string, string[]> = {
    frontend: [...base, "installation", "usage", "contributing", "contributors", "license", "footer"],
    fullstack: [
      ...base,
      "installation",
      "envVars",
      "usage",
      "apiEndpoints",
      "contributing",
      "contributors",
      "license",
      "footer",
    ],
    backend: [...base, "installation", "envVars", "apiEndpoints", "usage", "contributing", "contributors", "license", "footer"],
    library: ["header", "overview", "features", "installation", "usage", "api", "contributing", "contributors", "license", "footer"],
    cli: ["header", "overview", "features", "installation", "usage", "contributing", "contributors", "license", "footer"],
    ai: [...base, "installation", "envVars", "aiFeatures", "usage", "contributing", "contributors", "license", "footer"],
    web3: [...base, "installation", "envVars", "smartContracts", "usage", "contributing", "contributors", "license", "footer"],
    mobile: [...base, "installation", "usage", "contributing", "contributors", "license", "footer"],
    generic: [...base, "installation", "usage", "contributing", "contributors", "license", "footer"],
  };
  return maps[type] ?? maps.generic;
}
