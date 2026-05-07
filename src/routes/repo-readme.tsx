import { createFileRoute } from "@tanstack/react-router";
import { useState, useMemo } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { toast } from "sonner";
import {
  Copy,
  Download,
  Eye,
  Code2,
  ArrowRight,
  RotateCcw,
  GitBranch,
  Globe,
  Loader2,
  ChevronLeft,
  Package,
} from "lucide-react";
import { Navbar } from "@/components/Navbar";
import { RepoForm } from "@/components/RepoForm";
import { SectionToggles } from "@/components/SectionToggles";
import { MarkdownPreview } from "@/components/MarkdownPreview";
import { TagInput } from "@/components/FormElements";
import { RepoFormState, emptyRepoForm } from "@/lib/repoTypes";
import { buildRepoReadme } from "@/lib/buildRepoReadme";
import { detectRepoType, getSectionsForType, REPO_SECTIONS } from "@/lib/repoTemplates";

export const Route = createFileRoute("/repo-readme")({
  head: () => ({
    meta: [
      { title: "Best Repository README Generator — github-readme.app" },
      { name: "description", content: "Create professional repository READMEs for FREE. Automated tech stack detection, file structure visualization, and one-click export." },
    ],
  }),
  component: RepoReadmePage,
});

function parseRepoInput(input: string): { owner: string; repo: string } | null {
  const simple = input.match(/^([^/\s]+)\/([^/\s]+)$/);
  if (simple) return { owner: simple[1], repo: simple[2] };
  const url = input.match(/github\.com\/([^/\s]+)\/([^/\s]+)/);
  if (url) return { owner: url[1], repo: url[2].replace(/\.git$/, "") };
  return null;
}

function RepoReadmePage() {
  const [step, setStep] = useState<"url" | "details" | "editor">("url");
  const [repoInput, setRepoInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [fetchedData, setFetchedData] = useState<RepoFormState | null>(null);
  const [form, setForm] = useState<RepoFormState>(emptyRepoForm);
  const [sections, setSections] = useState<string[]>([]);
  const [manualMarkdown, setManualMarkdown] = useState<string | null>(null);
  const [tab, setTab] = useState<"preview" | "edit">("preview");

  const updateForm = (patch: Partial<RepoFormState>) => {
    setForm((prev) => ({ ...prev, ...patch }));
  };

  const generated = useMemo(() => buildRepoReadme(form, sections), [form, sections]);
  const markdown = manualMarkdown ?? generated;

  const handleFetch = async (e: React.FormEvent) => {
    e.preventDefault();
    const parsed = parseRepoInput(repoInput);
    if (!parsed) {
      setError("Please enter a valid owner/repo or GitHub URL.");
      return;
    }
    setLoading(true);
    setError(null);
    try {
      const { owner, repo } = parsed;
      const [repoRes, langsRes, topicsRes, contentsRes] = await Promise.all([
        fetch(`https://api.github.com/repos/${owner}/${repo}`),
        fetch(`https://api.github.com/repos/${owner}/${repo}/languages`),
        fetch(`https://api.github.com/repos/${owner}/${repo}/topics`, {
          headers: { Accept: "application/vnd.github.mercy-preview+json" }
        }),
        fetch(`https://api.github.com/repos/${owner}/${repo}/contents`),
      ]);
      if (!repoRes.ok) throw new Error(repoRes.status === 404 ? "Repository not found" : "GitHub API error");
      const repoData = await repoRes.json();
      const langs = langsRes.ok ? await langsRes.json() : {};
      const topicsData = topicsRes.ok ? await topicsRes.json() : { names: [] };
      const contents = contentsRes.ok ? await contentsRes.json() : [];
      const filenames: string[] = Array.isArray(contents) ? contents.map((f: any) => f.name) : [];
      const pm = filenames.includes("package.json") ? "npm"
        : filenames.includes("requirements.txt") || filenames.includes("pyproject.toml") ? "pip"
          : filenames.includes("Cargo.toml") ? "cargo"
            : filenames.includes("go.mod") ? "go"
              : filenames.includes("pom.xml") || filenames.includes("build.gradle") ? "maven"
                : "npm";
      const structure = Array.isArray(contents)
        ? contents
          .sort((a: any, b: any) => a.type === "dir" ? -1 : 1)
          .map((f: any) => ({ name: f.name, type: f.type as "file" | "dir" }))
        : [];
      const topLangs = Object.keys(langs).slice(0, 6);
      const hasBackend = filenames.some(f => ["server.js", "app.py", "main.go", "src/main.rs", "index.ts"].includes(f))
        || topicsData.names?.some((t: string) => ["backend", "api", "server", "express", "fastapi", "django"].includes(t.toLowerCase()));
      const res: RepoFormState = {
        ...emptyRepoForm,
        repoName: repoData.name,
        repoOwner: owner,
        description: repoData.description || "",
        stars: repoData.stargazers_count,
        forks: repoData.forks_count,
        issues: repoData.open_issues_count,
        license: repoData.license?.spdx_id || "MIT",
        language: repoData.language || "",
        topics: topicsData.names || [],
        techStack: topLangs,
        packageManager: pm as any,
        hasBackend,
        hasDocker: filenames.includes("Dockerfile") || filenames.includes("docker-compose.yml"),
        hasTesting: filenames.some(f => f.includes("test") || f.includes("spec") || f === "jest.config.js" || f === "pytest.ini"),
        repoStructure: structure,
        tagline: repoData.description || "",
        liveUrl: repoData.homepage || "",
      };
      res.repoType = detectRepoType(res);
      setFetchedData(res);
      setForm(res);
      setStep("details");
      toast.success("Repository analyzed!");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  const proceedToEditor = () => {
    setSections(getSectionsForType(form.repoType));
    setStep("editor");
  };

  const copyMd = async () => {
    try {
      await navigator.clipboard.writeText(markdown);
      toast.success("Markdown copied to clipboard");
    } catch {
      toast.error("Could not copy");
    }
  };

  const downloadMd = () => {
    const blob = new Blob([markdown], { type: "text/markdown;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "README.md";
    a.click();
    URL.revokeObjectURL(url);
    toast.success("README.md downloaded");
  };

  return (
    <main className="min-h-screen">
      <Navbar />

      <AnimatePresence mode="wait">
        {step === "url" && (
          <section key="url" className="relative mx-auto flex min-h-[calc(100vh-96px)] max-w-6xl items-center justify-center px-6">
            <div className="absolute inset-0 -z-10">
              <div className="absolute left-1/2 top-16 h-64 w-64 -translate-x-1/2 rounded-full bg-[radial-gradient(circle,rgba(120,255,103,0.35),transparent_70%)] blur-2xl" />
              <div className="absolute right-10 top-32 h-72 w-72 rounded-full bg-[radial-gradient(circle,rgba(82,39,255,0.35),transparent_70%)] blur-3xl" />
            </div>
            <motion.div
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -30 }}
              className="glass relative w-full max-w-2xl overflow-hidden rounded-3xl border border-border/50 p-8 shadow-2xl"
            >
              <div className="flex items-center gap-4 mb-6">
                <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-card/70 border border-border/60">
                  <GitBranch className="h-6 w-6 text-foreground" />
                </div>
                <div>
                  <div className="text-xs uppercase tracking-[0.2em] text-muted-foreground">Repo README</div>
                  <h1 className="text-2xl font-semibold">Enter your GitHub repository</h1>
                </div>
              </div>
              <p className="text-sm text-muted-foreground mb-6">
                Paste your repo URL or enter <code className="bg-card px-1.5 py-0.5 rounded border border-border/40">owner/repo</code>.
              </p>
              <form onSubmit={handleFetch} className="space-y-4">
                <div>
                  <div className="relative">
                    <Globe className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
                    <input
                      value={repoInput}
                      onChange={e => setRepoInput(e.target.value)}
                      placeholder="  https://github.com/user/repo"
                      className="w-full rounded-xl border border-border/60 bg-background/60 py-3 pl-10 pr-4 text-sm outline-none transition-colors focus:border-[oklch(0.7_0.24_295)]"
                    />
                  </div>
                  {error && <p className="mt-2 text-xs text-destructive px-1">{error}</p>}
                </div>
                <button
                  type="submit"
                  disabled={!repoInput.trim() || loading}
                  className="group inline-flex w-full items-center justify-center gap-2 rounded-xl bg-gradient-neon px-4 py-3 text-sm font-medium text-background shadow-[var(--shadow-glow)] transition-transform hover:scale-[1.02] disabled:opacity-60"
                >
                  {loading ? <Loader2 className="h-4 w-4 animate-spin" /> : <ArrowRight className="h-4 w-4" />}
                  {loading ? "Analyzing repository..." : "Analyze Repository"}
                </button>
              </form>
            </motion.div>
          </section>
        )}

        {step === "details" && fetchedData && (
          <section key="details" className="relative mx-auto flex min-h-[calc(100vh-96px)] max-w-4xl items-center justify-center px-6 py-10">
            <motion.div
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -30 }}
              className="glass w-full rounded-3xl border border-border/50 p-8 space-y-8 shadow-2xl"
            >
              <div className="flex items-start gap-4 rounded-xl border border-border/40 bg-card/30 p-5">
                <div className="h-12 w-12 rounded-xl bg-background/50 flex items-center justify-center border border-border/60">
                  <Globe className="h-6 w-6 text-muted-foreground shrink-0" />
                </div>
                <div className="flex-1 min-w-0">
                  <div className="font-semibold text-xl">{fetchedData.repoOwner}/{fetchedData.repoName}</div>
                  <div className="text-sm text-muted-foreground mt-1 line-clamp-2">{fetchedData.description}</div>
                  <div className="flex flex-wrap gap-3 mt-3 text-xs font-medium text-muted-foreground">
                    <span className="flex items-center gap-1.5"><Package className="h-3.5 w-3.5" /> {fetchedData.language}</span>
                    <span className="flex items-center gap-1.5">⭐ {fetchedData.stars.toLocaleString()}</span>
                  </div>
                </div>
                <button onClick={() => setStep("url")} className="p-2 hover:bg-card rounded-lg transition-colors">
                  <RotateCcw className="h-4 w-4 text-muted-foreground" />
                </button>
              </div>

              <div className="space-y-4">
                <label className="block text-sm font-semibold text-foreground/80">What type of project is this?</label>
                <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
                  {[
                    { id: "frontend", label: "Frontend", icon: "🖥️" },
                    { id: "fullstack", label: "Full Stack", icon: "⚡" },
                    { id: "backend", label: "Backend / API", icon: "⚙️" },
                    { id: "library", label: "Library / SDK", icon: "📦" },
                    { id: "cli", label: "CLI Tool", icon: "💻" },
                    { id: "ai", label: "AI / ML", icon: "🤖" },
                    { id: "web3", label: "Web3", icon: "⛓️" },
                    { id: "mobile", label: "Mobile", icon: "📱" },
                  ].map(type => (
                    <button
                      key={type.id}
                      onClick={() => setForm(f => ({ ...f, repoType: type.id as any }))}
                      className={`flex flex-col items-center justify-center rounded-2xl border p-4 text-xs font-semibold transition-all ${form.repoType === type.id
                          ? "border-[oklch(0.7_0.24_295)] bg-[oklch(0.7_0.24_295)]/10 text-foreground ring-1 ring-[oklch(0.7_0.24_295)]/30"
                          : "border-border/60 bg-background/40 text-muted-foreground hover:border-border/80 hover:text-foreground"
                        }`}
                    >
                      <div className="text-2xl mb-2">{type.icon}</div>
                      {type.label}
                    </button>
                  ))}
                </div>
              </div>

              <div className="space-y-3">
                <label className="block text-sm font-semibold text-foreground/80">Tech Stack</label>
                <TagInput
                  tags={form.techStack}
                  onChange={tags => setForm(f => ({ ...f, techStack: tags }))}
                  placeholder="React, Node.js, PostgreSQL..."
                />
              </div>

              <div className="space-y-3">
                <label className="block text-sm font-semibold text-foreground/80">Package Manager</label>
                <div className="flex flex-wrap gap-2">
                  {["npm", "yarn", "pnpm", "pip", "cargo", "go", "maven"].map(pm => (
                    <button
                      key={pm}
                      onClick={() => setForm(f => ({ ...f, packageManager: pm as any }))}
                      className={`rounded-xl border px-4 py-2 text-xs font-mono font-bold uppercase tracking-wider transition-all ${form.packageManager === pm
                          ? "border-[oklch(0.7_0.24_295)] bg-[oklch(0.7_0.24_295)]/10 text-[oklch(0.78_0.18_295)]"
                          : "border-border/60 bg-background/40 text-muted-foreground hover:border-border"
                        }`}
                    >
                      {pm}
                    </button>
                  ))}
                </div>
              </div>

              <button
                onClick={proceedToEditor}
                className="inline-flex w-full items-center justify-center gap-2 rounded-xl bg-gradient-neon px-4 py-4 text-sm font-bold text-background shadow-[var(--shadow-glow)] transition-transform hover:scale-[1.01]"
              >
                Generate README <ArrowRight className="h-4 w-4" />
              </button>
            </motion.div>
          </section>
        )}

        {step === "editor" && (
          <motion.div
            key="editor"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="mx-auto max-w-[1600px] px-4 py-6"
          >
            <div className="grid gap-4 lg:grid-cols-[260px_minmax(0,1fr)_minmax(0,1fr)]">
              {/* LEFT: Sidebar */}
              <aside className="flex flex-col gap-4 lg:sticky lg:top-20 lg:h-[calc(100vh-140px)]">
                {/* Back button */}
                <button
                  onClick={() => setStep("details")}
                  className="flex items-center gap-2 text-xs text-muted-foreground hover:text-foreground transition-colors"
                >
                  <ChevronLeft className="h-3.5 w-3.5" /> Back to details
                </button>

                {/* Repo info mini card */}
                <div className="glass rounded-xl p-3 border border-border/50">
                  <div className="flex items-center gap-2">
                    <Globe className="h-4 w-4 text-muted-foreground" />
                    <span className="text-sm font-medium truncate">{form.repoOwner}/{form.repoName}</span>
                  </div>
                  <div className="mt-1 flex gap-2 text-[11px] text-muted-foreground">
                    <span>⭐ {form.stars}</span>
                    <span className="capitalize">{form.repoType}</span>
                    <span>{form.language}</span>
                  </div>
                </div>

                {/* Section toggles */}
                <div className="glass flex min-h-0 flex-1 flex-col rounded-xl p-4 border border-border/50">
                  <div className="mb-3 text-xs font-semibold uppercase tracking-[0.15em] text-muted-foreground">
                    Sections
                  </div>
                  <div className="min-h-0 flex-1 overflow-auto pr-1">
                    <SectionToggles
                      sections={sections}
                      onChange={setSections}
                      availableSections={REPO_SECTIONS}
                    />
                  </div>
                </div>
              </aside>

              {/* CENTER: Form */}
              <section className="min-w-0 space-y-4">
                <RepoForm
                  form={form}
                  onChange={updateForm}
                  activeSections={sections}
                />
              </section>

              {/* RIGHT: Preview */}
              <section className="min-w-0">
                <div className="glass sticky top-20 rounded-xl border border-border/50 overflow-hidden shadow-2xl">
                  <div className="flex items-center justify-between border-b border-border/40 p-2 bg-card/30">
                    <div className="flex rounded-lg bg-background/50 p-1">
                      <TabBtn active={tab === "preview"} onClick={() => setTab("preview")}>
                        <Eye className="h-3.5 w-3.5" /> Preview
                      </TabBtn>
                      <TabBtn active={tab === "edit"} onClick={() => setTab("edit")}>
                        <Code2 className="h-3.5 w-3.5" /> Markdown
                      </TabBtn>
                    </div>
                    <div className="flex items-center gap-1.5">
                      <ToolbarBtn onClick={copyMd} title="Copy"><Copy className="h-3.5 w-3.5" /></ToolbarBtn>
                      <ToolbarBtn onClick={downloadMd} title="Download"><Download className="h-3.5 w-3.5" /></ToolbarBtn>
                    </div>
                  </div>

                  <motion.div
                    key={tab}
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.15 }}
                    className="h-[calc(100vh-220px)] overflow-auto p-6 bg-background/20"
                  >
                    {tab === "preview" ? (
                      <MarkdownPreview source={markdown} />
                    ) : (
                      <textarea
                        value={markdown}
                        onChange={(e) => setManualMarkdown(e.target.value)}
                        spellCheck={false}
                        className="h-full w-full resize-none bg-transparent font-mono text-[12px] leading-relaxed outline-none"
                      />
                    )}
                  </motion.div>
                </div>
              </section>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </main>
  );
}

function TabBtn({ active, onClick, children }: { active: boolean; onClick: () => void; children: React.ReactNode }) {
  return (
    <button
      onClick={onClick}
      className={`inline-flex items-center gap-1.5 rounded-md px-3 py-1.5 text-xs font-medium transition-all ${active ? "bg-gradient-neon text-background shadow-lg shadow-neon/20" : "text-muted-foreground hover:text-foreground"
        }`}
    >
      {children}
    </button>
  );
}

function ToolbarBtn({ children, onClick, title }: { children: React.ReactNode; onClick: () => void; title: string }) {
  return (
    <button
      onClick={onClick}
      title={title}
      className="inline-flex h-8 w-8 items-center justify-center rounded-lg border border-border/60 bg-card/40 text-muted-foreground transition-colors hover:bg-card hover:text-foreground"
    >
      {children}
    </button>
  );
}
