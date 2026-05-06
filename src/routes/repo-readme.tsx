import { createFileRoute } from "@tanstack/react-router";
import { useCallback, useEffect, useMemo, useState } from "react";
import { motion } from "framer-motion";
import {
  Code2,
  FileText,
  GitBranch,
  GitFork,
  Link2,
  Loader2,
  Sparkles,
  Star,
  Tag,
} from "lucide-react";
import { Navbar } from "@/components/Navbar";
import { Footer } from "@/components/Footer";
import { MarkdownPreview } from "@/components/MarkdownPreview";
import repoTemplate from "../../md-templates/repo-template.md?raw";

const analysisSteps = [
  {
    title: "Validating repository URL",
    detail: "Checking format, visibility, and default branch",
  },
  {
    title: "Fetching repository signals",
    detail: "Languages, topics, and dependency markers",
  },
  {
    title: "Understanding project structure",
    detail: "Scanning folders and config files",
  },
  {
    title: "Drafting README outline",
    detail: "Planning sections and tech stack summary",
  },
];

type RepoSummary = {
  owner: string;
  name: string;
  fullName: string;
  description: string | null;
  stars: number;
  forks: number;
  defaultBranch: string;
  license: string | null;
  topics: string[];
  languages: string[];
};

const parseGitHubUrl = (rawUrl: string) => {
  try {
    const url = new URL(rawUrl);
    if (url.hostname !== "github.com") return null;
    const [owner, repo] = url.pathname.replace(/^\//, "").split("/");
    if (!owner || !repo) return null;
    return { owner, repo: repo.replace(/\.git$/, "") };
  } catch {
    return null;
  }
};

const fetchRepoSummary = async (rawUrl: string): Promise<RepoSummary> => {
  const parsed = parseGitHubUrl(rawUrl);
  if (!parsed) {
    throw new Error("Enter a valid GitHub repository URL.");
  }

  const repoResponse = await fetch(`https://api.github.com/repos/${parsed.owner}/${parsed.repo}`);
  if (!repoResponse.ok) {
    throw new Error("Repository not found or unavailable.");
  }

  const repoData = await repoResponse.json();
  const languagesResponse = await fetch(
    `https://api.github.com/repos/${parsed.owner}/${parsed.repo}/languages`
  );
  const topicsResponse = await fetch(
    `https://api.github.com/repos/${parsed.owner}/${parsed.repo}/topics`,
    { headers: { Accept: "application/vnd.github+json" } }
  );

  const languagesData = languagesResponse.ok ? await languagesResponse.json() : {};
  const topicsData = topicsResponse.ok ? await topicsResponse.json() : { names: [] };

  return {
    owner: repoData.owner?.login ?? parsed.owner,
    name: repoData.name ?? parsed.repo,
    fullName: repoData.full_name ?? `${parsed.owner}/${parsed.repo}`,
    description: repoData.description ?? null,
    stars: repoData.stargazers_count ?? 0,
    forks: repoData.forks_count ?? 0,
    defaultBranch: repoData.default_branch ?? "main",
    license: repoData.license?.name ?? null,
    topics: Array.isArray(topicsData?.names) ? topicsData.names : [],
    languages: Object.keys(languagesData ?? {}).slice(0, 6),
  };
};

export const Route = createFileRoute("/repo-readme")({
  head: () => ({
    meta: [
      { title: "Repo README Generator — github-readme.app" },
      {
        name: "description",
        content: "Generate a premium README.md from any GitHub repository URL with fast AI analysis.",
      },
    ],
  }),
  component: RepoReadmePage,
});

function RepoReadmePage() {
  const [repoUrl, setRepoUrl] = useState("");
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [isComplete, setIsComplete] = useState(false);
  const [isGenerating, setIsGenerating] = useState(false);
  const [progress, setProgress] = useState(0);
  const [stepIndex, setStepIndex] = useState(0);
  const [submittedUrl, setSubmittedUrl] = useState("");
  const [repoSummary, setRepoSummary] = useState<RepoSummary | null>(null);
  const [generatedReadme, setGeneratedReadme] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [showEditor, setShowEditor] = useState(true);

  const steps = useMemo(() => analysisSteps, []);

  const buildTemplateReadme = (summary: RepoSummary) => {
    const [owner, repo] = summary.fullName.split("/");
    const safeOwner = owner || summary.owner || "USERNAME";
    const safeRepo = repo || summary.name || "REPO";
    const name = summary.name || "Project Name";
    const description = summary.description || "One-line catchy description of your project";

    return repoTemplate
      .replaceAll("USERNAME/REPO", `${safeOwner}/${safeRepo}`)
      .replaceAll("USERNAME", safeOwner)
      .replaceAll("REPO", safeRepo)
      .replace("Project Name", name)
      .replace("One-line catchy description of your project", description);
  };

  const runGeneration = useCallback(async (rawUrl: string) => {
    try {
      const summary = await fetchRepoSummary(rawUrl);
      setRepoSummary(summary);
      const templated = buildTemplateReadme(summary).trim();
      setGeneratedReadme(templated);
      setIsComplete(true);
    } catch (err) {
      const message = err instanceof Error ? err.message : "Failed to generate README.";
      setError(message);
    } finally {
      setIsGenerating(false);
    }
  }, []);

  useEffect(() => {
    if (!isAnalyzing) return;

    setProgress(5);
    setStepIndex(0);

    const stepTimer = window.setInterval(() => {
      setStepIndex((prev) => (prev + 1) % steps.length);
    }, 1200);

    const progressTimer = window.setInterval(() => {
      setProgress((prev) => (prev >= 96 ? 96 : prev + 4));
    }, 160);

    const finishTimer = window.setTimeout(() => {
      setIsAnalyzing(false);
      setProgress(100);
      setIsGenerating(true);
      void runGeneration(submittedUrl);
    }, 5200);

    return () => {
      window.clearInterval(stepTimer);
      window.clearInterval(progressTimer);
      window.clearTimeout(finishTimer);
    };
  }, [isAnalyzing, steps.length, submittedUrl, runGeneration]);

  const onAnalyze = (event: React.FormEvent) => {
    event.preventDefault();
    if (!repoUrl.trim()) return;
    setError(null);
    setIsComplete(false);
    setIsGenerating(false);
    setGeneratedReadme("");
    setRepoSummary(null);
    setShowEditor(true);
    setSubmittedUrl(repoUrl.trim());
    setIsAnalyzing(true);
  };


  return (
    <main className="min-h-screen">
      <Navbar />
      <section className="mx-auto max-w-7xl px-6 py-16">
        <motion.div initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }} className="max-w-3xl">
          <div className="inline-flex items-center gap-2 rounded-full border border-border/60 bg-card/40 px-3 py-1 text-xs text-muted-foreground">
            <Sparkles className="h-3.5 w-3.5" />
            Repo README Generator
          </div>
          <h1 className="mt-5 text-4xl font-bold tracking-tight md:text-5xl font-display">
            Turn any repo into a <span className="text-gradient">polished README</span>
          </h1>
          <p className="mt-4 text-sm text-muted-foreground md:text-base">
            Paste a GitHub repository URL, run a quick analysis, and generate a structured README for your Repository.
          </p>
        </motion.div>

        <div className="mt-10 grid gap-8 lg:grid-cols-[1.1fr_0.9fr]">
          <form onSubmit={onAnalyze} className="glass rounded-3xl p-6 md:p-8">
            <div className="flex items-center gap-3 text-sm font-medium">
              <GitBranch className="h-4 w-4 text-muted-foreground" />
              Repository URL
            </div>
            <div className="mt-4 flex flex-col gap-3 sm:flex-row">
              <div className="relative flex-1">
                <Link2 className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
                <input
                  value={repoUrl}
                  onChange={(event) => setRepoUrl(event.target.value)}
                  placeholder="https://github.com/user/project"
                  className="w-full rounded-xl border border-border/60 bg-background/40 px-4 py-3 pl-10 text-sm outline-none focus:border-[oklch(0.7_0.24_295)]"
                />
              </div>
              <button
                type="submit"
                disabled={!repoUrl.trim() || isAnalyzing || isGenerating}
                className="inline-flex h-12 items-center justify-center gap-2 rounded-xl bg-gradient-neon px-5 text-sm font-medium text-background shadow-[var(--shadow-glow)] transition-transform hover:scale-[1.02] disabled:cursor-not-allowed disabled:opacity-60"
              >
                {isAnalyzing || isGenerating ? (
                  <>
                    <Loader2 className="h-4 w-4 animate-spin" />
                    {isAnalyzing ? "Analyzing" : "Generating"}
                  </>
                ) : (
                  "Analyze Repo"
                )}
              </button>
            </div>

            {error && (
              <div className="mt-4 rounded-2xl border border-destructive/40 bg-destructive/10 px-4 py-3 text-xs text-destructive">
                {error}
              </div>
            )}

          </form>

          <div className="glass rounded-3xl p-6 md:p-8">
            <div className="flex items-center justify-between">
              <div className="text-xs uppercase tracking-[0.2em] text-muted-foreground">Live analysis</div>
              {isComplete && !isAnalyzing && (
                <span className="rounded-full bg-gradient-neon px-3 py-1 text-[10px] font-semibold text-background">
                  Complete
                </span>
              )}
            </div>

            <div className="mt-6 space-y-4">
              {steps.map((step, index) => {
                const isActive = isAnalyzing && index === stepIndex;
                const isDone = isComplete || (!isAnalyzing && progress === 100 && index <= stepIndex);

                return (
                  <div
                    key={step.title}
                    className={`rounded-2xl border px-4 py-3 transition-colors ${
                      isActive
                        ? "border-transparent bg-gradient-neon text-background"
                        : isDone
                        ? "border-border/60 bg-card/60"
                        : "border-border/40 bg-card/30"
                    }`}
                  >
                    <div className="text-sm font-medium">{step.title}</div>
                    <div className={`mt-1 text-xs ${isActive ? "text-background/80" : "text-muted-foreground"}`}>
                      {step.detail}
                    </div>
                  </div>
                );
              })}
            </div>

            <div className="mt-6">
              <div className="flex items-center justify-between text-xs text-muted-foreground">
                <span>
                  {isAnalyzing
                    ? "Analyzing repository"
                    : isGenerating
                    ? "Generating README"
                    : isComplete
                    ? "Analysis ready"
                    : "Idle"}
                </span>
                <span>{progress}%</span>
              </div>
              <div className="mt-2 h-2 overflow-hidden rounded-full bg-border/40">
                <div
                  className="h-full bg-gradient-neon transition-all duration-300"
                  style={{ width: `${progress}%` }}
                />
              </div>
            </div>

            <div className="mt-6 rounded-2xl border border-border/60 bg-background/40 p-4 text-xs text-muted-foreground">
              {isComplete ? (
                <div>
                  Analysis complete. README template ready.
                </div>
              ) : isGenerating ? (
                <div>
                  Building README from the template.
                </div>
              ) : (
                <div>
                  Run analysis to preview the steps before generation.
                </div>
              )}
            </div>

            {repoSummary && (
              <div className="mt-6 rounded-2xl border border-border/60 bg-background/40 p-4">
                <div className="flex flex-wrap items-center gap-3 text-sm font-medium">
                  <span className="inline-flex items-center gap-2">
                    <FileText className="h-4 w-4 text-muted-foreground" />
                    {repoSummary.fullName}
                  </span>
                  {repoSummary.description && (
                    <span className="text-xs text-muted-foreground">{repoSummary.description}</span>
                  )}
                </div>
                <div className="mt-4 grid gap-3 text-xs text-muted-foreground sm:grid-cols-2">
                  <div className="flex items-center gap-2">
                    <Star className="h-4 w-4" />
                    {repoSummary.stars.toLocaleString()} stars
                  </div>
                  <div className="flex items-center gap-2">
                    <GitFork className="h-4 w-4" />
                    {repoSummary.forks.toLocaleString()} forks
                  </div>
                  <div className="flex items-center gap-2">
                    <Code2 className="h-4 w-4" />
                    {repoSummary.languages.length ? repoSummary.languages.join(", ") : "Languages pending"}
                  </div>
                  <div className="flex items-center gap-2">
                    <Tag className="h-4 w-4" />
                    {repoSummary.topics.length ? repoSummary.topics.join(", ") : "Topics pending"}
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>

        {generatedReadme && (
          <div className="mt-10 glass rounded-3xl border border-border/60 p-6 md:p-8">
            <div className="flex flex-wrap items-center justify-between gap-3">
              <div className="text-xs uppercase tracking-[0.2em] text-muted-foreground">Generated README</div>
              <div className="flex flex-wrap items-center gap-2">
                <button
                  type="button"
                  onClick={() => setShowEditor((prev) => !prev)}
                  className="inline-flex h-9 items-center justify-center rounded-lg border border-border/60 bg-card/40 px-3 text-xs font-medium hover:bg-card/70"
                >
                  {showEditor ? "Hide Editor" : "Edit Markdown"}
                </button>
                <button
                  type="button"
                  onClick={() => setGeneratedReadme(buildTemplateReadme(repoSummary ?? {
                    owner: "USERNAME",
                    name: "Project Name",
                    fullName: "USERNAME/REPO",
                    description: "One-line catchy description of your project",
                    stars: 0,
                    forks: 0,
                    defaultBranch: "main",
                    license: null,
                    topics: [],
                    languages: [],
                  }))}
                  className="inline-flex h-9 items-center justify-center rounded-lg border border-border/60 bg-card/40 px-3 text-xs font-medium hover:bg-card/70"
                >
                  Reset Template
                </button>
                <button
                  type="button"
                  onClick={async () => {
                    await navigator.clipboard.writeText(generatedReadme);
                  }}
                  className="inline-flex h-9 items-center justify-center rounded-lg border border-border/60 bg-card/40 px-3 text-xs font-medium hover:bg-card/70"
                >
                  Copy Code
                </button>
                <button
                  type="button"
                  onClick={() => {
                    const blob = new Blob([generatedReadme], { type: "text/markdown;charset=utf-8" });
                    const url = URL.createObjectURL(blob);
                    const link = document.createElement("a");
                    link.href = url;
                    link.download = "README.md";
                    document.body.appendChild(link);
                    link.click();
                    link.remove();
                    URL.revokeObjectURL(url);
                  }}
                  className="inline-flex h-9 items-center justify-center rounded-lg bg-gradient-neon px-4 text-xs font-semibold text-background shadow-[var(--shadow-glow)]"
                >
                  Export README
                </button>
              </div>
            </div>
            <div className={`mt-6 grid gap-6 ${showEditor ? "lg:grid-cols-[1fr_1fr]" : "lg:grid-cols-[1fr]"}`}>
              {showEditor && (
                <div className="rounded-2xl border border-border/60 bg-background/50 p-4">
                  <div className="mb-3 text-xs uppercase tracking-[0.2em] text-muted-foreground">Edit Markdown</div>
                  <textarea
                    value={generatedReadme}
                    onChange={(event) => setGeneratedReadme(event.target.value)}
                    className="h-[520px] w-full resize-none rounded-xl border border-border/60 bg-background/40 p-4 font-mono text-xs text-foreground outline-none focus:border-[oklch(0.7_0.24_295)]"
                  />
                </div>
              )}
              <div className="rounded-2xl border border-border/60 bg-background/50 p-6">
                <div className="mb-3 text-xs uppercase tracking-[0.2em] text-muted-foreground">Preview</div>
                <MarkdownPreview source={generatedReadme} />
              </div>
            </div>
          </div>
        )}
      </section>
      <Footer />
    </main>
  );
}
