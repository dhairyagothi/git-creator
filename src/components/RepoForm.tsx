import { Info, ExternalLink, Image as ImageIcon, Star, Key, Server, FolderTree, Folder, FileText, Users, Heart, Cpu } from "lucide-react";
import type { RepoFormState } from "@/lib/repoTypes";
import { Label, Input, TagInput, Section, ListEditor, ApiEndpointsEditor } from "@/components/FormElements";
import { useState } from "react"; // ← ADDED

interface RepoFormProps {
  form: RepoFormState;
  onChange: (patch: Partial<RepoFormState>) => void;
  activeSections: string[];
}

function Field({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div>
      <Label>{label}</Label>
      {children}
    </div>
  );
}

export function RepoForm({ form, onChange, activeSections }: RepoFormProps) {
  const has = (id: string) => activeSections.includes(id);
  const upd = (patch: Partial<RepoFormState>) => onChange(patch);

  // ---- AI AUTO-GENERATION STATE & HANDLER ----
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  const handleAutoGenerate = async () => {
    if (!form.repoOwner || !form.repoName) {
      alert("Please enter the Repo Owner and Repo Name first.");
      return;
    }
    const repoUrl = `https://github.com/${form.repoOwner}/${form.repoName}`;
    setIsAnalyzing(true);
    try {
      const res = await fetch("/api/analyze-repo", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ repoUrl }),
      });
      if (!res.ok) throw new Error(await res.text());
      const data = await res.json();
      // Populate form fields with AI response (only if not empty)
      upd({
        tagline: data.tagline || form.tagline,
        description: data.description || form.description,
        features: data.features?.length ? data.features : form.features,
        techStack: data.techStack?.length ? data.techStack : form.techStack,
      });
    } catch (err) {
      alert("Auto-generation failed: " + (err as Error).message);
    } finally {
      setIsAnalyzing(false);
    }
  };
  // --------------------------------------------

  return (
    <div className="space-y-3 pb-20">
      <Section icon={Info} title="Basic Info" defaultOpen>
        <Field label="Project Tagline">
          <Input value={form.tagline} onChange={v => upd({ tagline: v })}
            placeholder="One-line catchy description"/>
        </Field>

        {/* ---- AI AUTO-GENERATE BUTTON ---- */}
        <div className="mt-1 mb-3">
          <button
            type="button"
            onClick={handleAutoGenerate}
            disabled={isAnalyzing}
            className="inline-flex items-center gap-1 text-xs font-medium text-blue-600 hover:text-blue-800 disabled:opacity-50 transition-colors"
          >
            {isAnalyzing ? "⏳ Analyzing repo..." : "✨ Auto‑generate from Repo"}
          </button>
          <p className="text-[10px] text-muted-foreground mt-0.5">
            Reads your GitHub repo and fills in the description, features, and tech stack using AI.
          </p>
        </div>
        {/* --------------------------------- */}

        <Field label="Primary Language">
          <Input value={form.language} onChange={v => upd({ language: v })}/>
        </Field>
      </Section>

      {/* Demo Links */}
      {has("demo") && (
        <Section icon={ExternalLink} title="Live Demo" defaultOpen>
          <Field label="Live URL">
            <Input value={form.liveUrl} onChange={v => upd({ liveUrl: v })} placeholder="https://..."/>
          </Field>
          <Field label="Demo Video URL">
            <Input value={form.videoUrl} onChange={v => upd({ videoUrl: v })} placeholder="https://youtube.com/..."/>
          </Field>
        </Section>
      )}

      {/* Screenshots */}
      {has("screenshots") && (
        <Section icon={ImageIcon} title="Screenshots" defaultOpen={false}>
          <Field label="Screenshot URL">
            <Input value={form.screenshotUrl} onChange={v => upd({ screenshotUrl: v })} placeholder="https://..."/>
          </Field>
        </Section>
      )}

      {/* Features */}
      {has("features") && (
        <Section icon={Star} title="Features" defaultOpen>
          <ListEditor
            items={form.features}
            onChange={v => upd({ features: v })}
            placeholder="Add a key feature..."
          />
        </Section>
      )}

      {/* Tech Stack */}
      {has("techStack") && (
        <Section icon={Cpu} title="Tech Stack" defaultOpen>
          <TagInput
            tags={form.techStack}
            onChange={v => upd({ techStack: v })}
            placeholder="React, Tailwind, Node.js..."
          />
        </Section>
      )}

      {/* Env Vars */}
      {has("envVars") && (
        <Section icon={Key} title="Environment Variables" defaultOpen={false}>
          <p className="text-xs text-muted-foreground mb-2">
            Add variable names only (not values). e.g. <code>DATABASE_URL</code>
          </p>
          <TagInput
            tags={form.envVars}
            onChange={v => upd({ envVars: v })}
            placeholder="DATABASE_URL, JWT_SECRET..."
          />
        </Section>
      )}

      {/* API Endpoints */}
      {has("apiEndpoints") && (
        <Section icon={Server} title="API Endpoints" defaultOpen={false}>
          <ApiEndpointsEditor
            endpoints={form.apiEndpoints}
            onChange={v => upd({ apiEndpoints: v })}
          />
        </Section>
      )}

      {/* Repo structure */}
      {has("structure") && (
        <Section icon={FolderTree} title="Repository Structure" defaultOpen={false}>
          <div className="rounded-lg border border-border/60 bg-card/30 p-3 font-mono text-xs">
            <div className="text-muted-foreground mb-2">📁 {form.repoName}/</div>
            {form.repoStructure.map(item => (
              <div key={item.name} className="flex items-center gap-2 py-0.5 pl-4">
                {item.type === "dir"
                  ? <Folder className="h-3 w-3 text-blue-400 shrink-0"/>
                  : <FileText className="h-3 w-3 text-muted-foreground shrink-0"/>
                }
                <span className={item.type === "dir" ? "text-blue-400" : "text-foreground/80"}>
                  {item.name}{item.type === "dir" ? "/" : ""}
                </span>
              </div>
            ))}
            <p className="text-[10px] text-muted-foreground mt-2 pl-4">
              Auto-fetched from GitHub API
            </p>
          </div>
        </Section>
      )}

      {/* Contributors */}
      {has("contributors") && (
        <Section icon={Users} title="Contributors" defaultOpen={false}>
          <p className="text-xs text-muted-foreground">
            A dynamic contributors map will be generated using <code>contrib.rocks</code> based on your repository's actual contributors.
          </p>
        </Section>
      )}

      {/* Footer */}
      {has("footer") && (
        <Section icon={Heart} title="Footer Note" defaultOpen={false}>
          <p className="text-xs text-muted-foreground">
            A professional footer will be added with a "Star the repo" call-to-action and a "Made with love" note.
          </p>
        </Section>
      )}
    </div>
  );
}