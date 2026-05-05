import { useEffect, useMemo, useState } from "react";
import { motion } from "framer-motion";
import { toast } from "sonner";
import {
  Copy,
  Download,
  RotateCcw,
  Save,
  Eye,
  Code2,
  Sparkles,
} from "lucide-react";
import { useAppStore } from "@/lib/store";
import { buildReadme } from "@/lib/buildReadme";
import { getTemplate } from "@/lib/templates";
import { TemplatePicker } from "./TemplatePicker";
import { SectionToggles } from "./SectionToggles";
import { ProfileForm } from "./ProfileForm";
import { MarkdownPreview } from "./MarkdownPreview";

const DRAFT_KEY = "gra_draft_v1";
const PREFILL_KEY = "gra_prefill_v1";

export function GeneratorWorkspace() {
  const store = useAppStore();
  const { template, sections, form, manualMarkdown, setTemplate, setSections, setManualMarkdown, reset, load } = store;
  const [tab, setTab] = useState<"preview" | "edit">("preview");
  const templateConfig = getTemplate(template);

  // Load draft on mount
  useEffect(() => {
    try {
      const raw = localStorage.getItem(DRAFT_KEY);
      if (raw) {
        const data = JSON.parse(raw);
        load(data);
        toast.success("Draft restored", { duration: 2000 });
      }
    } catch {}
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    try {
      const raw = localStorage.getItem(PREFILL_KEY);
      if (raw) {
        const data = JSON.parse(raw) as { form?: Partial<typeof form> };
        if (data?.form) {
          load({
            form: {
              ...form,
              ...data.form,
              templateFields: {
                ...form.templateFields,
                ...data.form.templateFields,
              },
            },
          });
          setManualMarkdown(null);
        }
        localStorage.removeItem(PREFILL_KEY);
      }
    } catch {}
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Autosave
  useEffect(() => {
    const id = setTimeout(() => {
      try {
        localStorage.setItem(
          DRAFT_KEY,
          JSON.stringify({ template, sections, form, manualMarkdown }),
        );
      } catch {}
    }, 600);
    return () => clearTimeout(id);
  }, [template, sections, form, manualMarkdown]);

  const generated = useMemo(
    () => buildReadme(form, template, sections),
    [form, template, sections],
  );
  const markdown = manualMarkdown ?? generated;

  // Keyboard shortcuts
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (!(e.metaKey || e.ctrlKey)) return;
      if (e.key === "s") {
        e.preventDefault();
        saveDraft();
      } else if (e.shiftKey && e.key.toLowerCase() === "c") {
        e.preventDefault();
        copyMd();
      } else if (e.shiftKey && e.key.toLowerCase() === "r") {
        e.preventDefault();
        resetAll();
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [markdown]);

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

  const saveDraft = () => {
    try {
      localStorage.setItem(DRAFT_KEY, JSON.stringify({ template, sections, form, manualMarkdown }));
      toast.success("Draft saved");
    } catch {
      toast.error("Could not save draft");
    }
  };

  const resetAll = () => {
    if (!confirm("Reset everything? This cannot be undone.")) return;
    localStorage.removeItem(DRAFT_KEY);
    reset();
    setTab("preview");
    toast.success("Reset complete");
  };

  return (
    <div className="mx-auto max-w-[1600px] px-4 py-6">
      <div className="grid gap-4 lg:grid-cols-[280px_minmax(0,1fr)_minmax(0,1fr)]">
        {/* LEFT */}
        <aside className="flex flex-col gap-4 lg:sticky lg:top-20 lg:h-[calc(100vh-140px)]">
          <div className="glass flex min-h-0 flex-1 flex-col rounded-xl p-4">
            <div className="mb-3 flex items-center gap-2 text-xs font-semibold uppercase tracking-[0.15em] text-muted-foreground">
              <Sparkles className="h-3.5 w-3.5" /> Templates
            </div>
            <div className="min-h-0 flex-1 overflow-auto pr-1">
              <TemplatePicker value={template} onChange={setTemplate} compact />
            </div>
          </div>
          <div className="glass flex min-h-0 flex-1 flex-col rounded-xl p-4">
            <div className="mb-3 text-xs font-semibold uppercase tracking-[0.15em] text-muted-foreground">
              Sections
            </div>
            <div className="min-h-0 flex-1 overflow-auto pr-1">
              <SectionToggles sections={sections} onChange={setSections} />
            </div>
          </div>
        </aside>

        {/* CENTER */}
        <section className="min-w-0 space-y-4">
          <ProfileForm />
        </section>

        {/* RIGHT */}
        <section className="min-w-0">
          <div className="glass sticky top-20 rounded-xl">
            <div className="flex items-center justify-between border-b border-border/40 p-2">
              <div className="flex rounded-lg bg-background/50 p-1">
                <TabBtn active={tab === "preview"} onClick={() => setTab("preview")}>
                  <Eye className="h-3.5 w-3.5" /> Preview
                </TabBtn>
                <TabBtn active={tab === "edit"} onClick={() => setTab("edit")}>
                  <Code2 className="h-3.5 w-3.5" /> Markdown
                </TabBtn>
              </div>
              <div className="flex items-center gap-1.5">
                <ToolbarBtn onClick={copyMd} title="Copy (⌘⇧C)"><Copy className="h-3.5 w-3.5" /></ToolbarBtn>
                <ToolbarBtn onClick={downloadMd} title="Download README.md"><Download className="h-3.5 w-3.5" /></ToolbarBtn>
                <ToolbarBtn onClick={saveDraft} title="Save draft (⌘S)"><Save className="h-3.5 w-3.5" /></ToolbarBtn>
                <ToolbarBtn onClick={resetAll} title="Reset (⌘⇧R)"><RotateCcw className="h-3.5 w-3.5" /></ToolbarBtn>
              </div>
            </div>
            <motion.div
              key={tab}
              initial={{ opacity: 0, y: 6 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.15 }}
              className="max-h-[calc(100vh-160px)] overflow-auto p-5"
            >
              {tab === "preview" ? (
                <MarkdownPreview source={markdown} />
              ) : (
                <>
                  {manualMarkdown === null && (
                    <div className="mb-2 flex items-center justify-between rounded-md border border-border/60 bg-card/40 px-3 py-2 text-xs text-muted-foreground">
                      <span>Editing the markdown will switch to manual mode.</span>
                      <button
                        className="text-foreground hover:underline"
                        onClick={() => setManualMarkdown(generated)}
                      >
                        Enter manual mode
                      </button>
                    </div>
                  )}
                  {manualMarkdown !== null && (
                    <div className="mb-2 flex items-center justify-between rounded-md border border-border/60 bg-card/40 px-3 py-2 text-xs">
                      <span className="text-muted-foreground">Manual mode — form changes won't auto-update.</span>
                      <button
                        className="text-[oklch(0.78_0.18_200)] hover:underline"
                        onClick={() => {
                          if (confirm("Discard manual edits and re-sync from form?")) setManualMarkdown(null);
                        }}
                      >
                        Sync from form
                      </button>
                    </div>
                  )}
                  <textarea
                    value={markdown}
                    onChange={(e) => setManualMarkdown(e.target.value)}
                    spellCheck={false}
                    className="h-[calc(100vh-260px)] w-full resize-none rounded-lg border border-border/60 bg-background/60 p-4 font-mono text-[12.5px] leading-relaxed outline-none focus:border-[oklch(0.7_0.24_295)]"
                  />
                </>
              )}
            </motion.div>
          </div>
        </section>
      </div>
    </div>
  );
}

function TabBtn({
  active, onClick, children,
}: { active: boolean; onClick: () => void; children: React.ReactNode }) {
  return (
    <button
      onClick={onClick}
      className={`inline-flex items-center gap-1.5 rounded-md px-3 py-1.5 text-xs font-medium transition-colors ${
        active ? "bg-gradient-neon text-background shadow-[var(--shadow-glow)]" : "text-muted-foreground hover:text-foreground"
      }`}
    >
      {children}
    </button>
  );
}

function ToolbarBtn({
  children, onClick, title,
}: { children: React.ReactNode; onClick: () => void; title: string }) {
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
