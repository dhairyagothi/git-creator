import { useState, useCallback, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  User, MapPin, Mail, Code2, Briefcase, BookOpen, Link2,
  Plus, X, ChevronDown, Wrench, Folder, Quote, Star,
  Sparkles, GraduationCap, Globe, MessageCircle,
  Video, FileText, Hash, Cpu,
} from "lucide-react";
import { useAppStore } from "@/lib/store";
import { getTemplate, getTemplatePlaceholders } from "@/lib/templates";
import { AUTO_PLACEHOLDER_KEYS, getPlaceholderLabel, SOCIAL_OPTIONS, type SocialOption } from "@/lib/templateFields";
import type { FormState } from "@/lib/types";

/* ── helpers ───────────────────────────────────────────────────────────── */

function useFormField<K extends keyof FormState>(key: K) {
  const value = useAppStore((s) => s.form[key]);
  const updateForm = useAppStore((s) => s.updateForm);
  const set = useCallback((v: FormState[K]) => updateForm({ [key]: v } as Partial<FormState>), [key, updateForm]);
  return [value, set] as const;
}

/* ── sub-components ─────────────────────────────────────────────────────── */

import { Label, Input, TagInput, Section } from "@/components/FormElements";

function Textarea({
  value, onChange, placeholder, rows = 3,
}: {
  value: string; onChange: (v: string) => void; placeholder?: string; rows?: number;
}) {
  return (
    <textarea
      value={value}
      onChange={(e) => onChange(e.target.value)}
      placeholder={placeholder}
      rows={rows}
      className="w-full resize-none rounded-lg border border-border/60 bg-background/50 px-3 py-2 text-sm text-foreground placeholder:text-muted-foreground/50 outline-none transition-colors focus:border-[oklch(0.7_0.24_295)] focus:bg-background/80"
    />
  );
}

function ProjectsEditor() {
  const [projects, setProjects] = useFormField("projects");

  const update = (i: number, field: "name" | "description" | "url", val: string) => {
    const next = [...projects];
    next[i] = { ...next[i], [field]: val };
    setProjects(next);
  };

  const add = () => setProjects([...projects, { name: "", description: "", url: "" }]);
  const remove = (i: number) => setProjects(projects.filter((_, idx) => idx !== i));

  return (
    <div className="space-y-3">
      {projects.map((p, i) => (
        <motion.div
          key={i}
          initial={{ opacity: 0, y: -8 }}
          animate={{ opacity: 1, y: 0 }}
          className="relative rounded-lg border border-border/60 bg-card/30 p-3 space-y-2"
        >
          <button
            onClick={() => remove(i)}
            className="absolute right-2 top-2 flex h-6 w-6 items-center justify-center rounded-md text-muted-foreground hover:text-foreground hover:bg-card transition-colors"
          >
            <X className="h-3.5 w-3.5" />
          </button>
          <div className="pr-7">
            <Label>Project Name</Label>
            <Input value={p.name} onChange={(v) => update(i, "name", v)} placeholder={`Project ${i + 1}`} />
          </div>
          <div>
            <Label>Description</Label>
            <Input value={p.description} onChange={(v) => update(i, "description", v)} placeholder="Short description..." />
          </div>
          <div>
            <Label>URL / Link</Label>
            <Input value={p.url} onChange={(v) => update(i, "url", v)} placeholder="https://github.com/..." />
          </div>
        </motion.div>
      ))}
      {projects.length < 6 && (
        <button
          onClick={add}
          className="flex w-full items-center justify-center gap-2 rounded-lg border border-dashed border-border/60 py-2 text-xs text-muted-foreground hover:border-[oklch(0.7_0.24_295)]/50 hover:text-foreground transition-colors"
        >
          <Plus className="h-3.5 w-3.5" /> Add Project
        </button>
      )}
    </div>
  );
}

function ListEditor({
  items, onChange, placeholder,
}: {
  items: string[]; onChange: (v: string[]) => void; placeholder?: string;
}) {
  const [input, setInput] = useState("");

  const add = () => {
    if (!input.trim()) return;
    onChange([...items, input.trim()]);
    setInput("");
  };

  return (
    <div className="space-y-2">
      {items.map((item, i) => (
        <div key={i} className="flex items-center gap-2">
          <span className="flex-1 rounded-lg border border-border/60 bg-background/50 px-3 py-1.5 text-sm text-foreground">
            {item}
          </span>
          <button
            onClick={() => onChange(items.filter((_, idx) => idx !== i))}
            className="flex h-7 w-7 items-center justify-center rounded-md text-muted-foreground hover:text-foreground hover:bg-card/60 transition-colors"
          >
            <X className="h-3.5 w-3.5" />
          </button>
        </div>
      ))}
      <div className="flex gap-2">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => { if (e.key === "Enter") { e.preventDefault(); add(); } }}
          placeholder={placeholder}
          className="flex-1 rounded-lg border border-border/60 bg-background/50 px-3 py-1.5 text-sm text-foreground placeholder:text-muted-foreground/50 outline-none focus:border-[oklch(0.7_0.24_295)]"
        />
        <button
          onClick={add}
          className="flex h-8 w-8 items-center justify-center rounded-lg border border-border/60 bg-card/40 text-muted-foreground hover:bg-card hover:text-foreground transition-colors"
        >
          <Plus className="h-3.5 w-3.5" />
        </button>
      </div>
    </div>
  );
}

/* ── Section accordion ─────────────────────────────────────────────────── */

/* ── Field row helper ──────────────────────────────────────────────────── */

function Row({ children, cols = 1 }: { children: React.ReactNode; cols?: 1 | 2 }) {
  return (
    <div className={cols === 2 ? "grid grid-cols-2 gap-3" : ""}>
      {children}
    </div>
  );
}

function Field({ label, children, required }: { label: string; children: React.ReactNode; required?: boolean }) {
  return (
    <div>
      <Label required={required}>{label}</Label>
      {children}
    </div>
  );
}

/* ── Template-specific fields ──────────────────────────────────────────── */

function TemplateSpecificFields({ placeholders }: { placeholders: string[] }) {
  const templateFields = useAppStore((s) => s.form.templateFields);
  const updateTemplateField = useAppStore((s) => s.updateTemplateField);

  const custom = placeholders.filter((p) => !AUTO_PLACEHOLDER_KEYS.has(p));
  if (!custom.length) return null;

  // Group them
  const groups: Record<string, string[]> = {};
  custom.forEach((key) => {
    const base = key.replace(/^YOUR_/, "").replace(/_\d+$/, "");
    groups[base] = groups[base] ?? [];
    groups[base].push(key);
  });

  return (
    <Section icon={Sparkles} title="Template Fields" badge={`${custom.length} fields`} defaultOpen>
      <p className="text-xs text-muted-foreground">
        These fields are specific to your chosen template. Fill them in to customize your profile.
      </p>
      {Object.entries(groups).map(([group, keys]) => (
        <div key={group} className="space-y-2">
          {keys.length > 1 && (
            <p className="text-[10px] font-semibold uppercase tracking-widest text-muted-foreground/60">
              {group.replace(/_/g, " ")}
            </p>
          )}
          {keys.map((key) => (
            <div key={key}>
              <Label>{getPlaceholderLabel(key)}</Label>
              <Input
                value={templateFields?.[key] ?? ""}
                onChange={(v) => updateTemplateField(key, v)}
                placeholder={`Enter ${getPlaceholderLabel(key).toLowerCase()}...`}
              />
            </div>
          ))}
        </div>
      ))}
    </Section>
  );
}

/* ── Main ProfileForm ──────────────────────────────────────────────────── */

export function ProfileForm() {
  const { template, sections, form, updateForm, updateSocial } = useAppStore();
  const templateConfig = getTemplate(template);
  const placeholders = getTemplatePlaceholders(template);

  // Helper to check if a section should be shown in editor
  const isVisible = (id: SectionId) => sections.includes(id);

  // check if placeholder is relevant
  const needs = (keys: string[]) =>
    templateConfig.kind === "builder" || keys.some((k) => placeholders.includes(k));

  const upd = (key: keyof FormState) => (val: string) => updateForm({ [key]: val } as Partial<FormState>);
  const upd2 = (key: keyof FormState) => (val: string[]) => updateForm({ [key]: val } as Partial<FormState>);

  return (
    <div className="space-y-3">
      {/* ── Identity (Header) ── */}
      {isVisible("header") && (
        <Section icon={User} title="Identity" defaultOpen>
          <Field label="GitHub Username" required>
            <div className="flex gap-2">
              <div className="relative flex-1">
                <span className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground text-sm select-none">@</span>
                <Input
                  value={form.username}
                  onChange={upd("username")}
                  placeholder="octocat"
                  className="pl-7"
                />
              </div>
              <button
                onClick={async () => {
                  const normalizedUsername = form.username.trim().replace(/^@+/, "");
                  if (!normalizedUsername) return;
                  try {
                    const res = await fetch(`https://api.github.com/users/${encodeURIComponent(normalizedUsername)}`);
                    if (!res.ok) return;
                    const data = await res.json() as any;
                    
                    const reposRes = await fetch(`https://api.github.com/users/${encodeURIComponent(normalizedUsername)}/repos?per_page=100&sort=stars`);
                    const repos = reposRes.ok ? await reposRes.json() as any[] : [];
                    
                    const nonForks = repos.filter(r => !r.fork);
                    const topProjects = nonForks
                      .sort((a, b) => (b.stargazers_count ?? 0) - (a.stargazers_count ?? 0))
                      .slice(0, 4)
                      .map(r => ({
                        name: r.name,
                        description: r.description || "",
                        url: r.html_url
                      }));

                    let totalStars = 0;
                    const langCounts: Record<string, number> = {};
                    repos.forEach((repo) => {
                      totalStars += repo.stargazers_count ?? 0;
                      if (repo.language) {
                        langCounts[repo.language] = (langCounts[repo.language] ?? 0) + 1;
                      }
                    });
                    const topLanguages = Object.entries(langCounts)
                      .sort((a, b) => b[1] - a[1])
                      .slice(0, 6)
                      .map(([lang]) => lang);

                    updateForm({
                      username: normalizedUsername,
                      displayName: data.name || form.displayName,
                      bio: data.bio || form.bio,
                      avatarUrl: data.avatar_url || form.avatarUrl,
                      location: data.location || form.location,
                      githubStats: {
                        totalStars,
                        publicRepos: data.public_repos ?? form.githubStats.publicRepos,
                        followers: data.followers ?? form.githubStats.followers,
                        topLanguages,
                      },
                      projects: topProjects.length ? topProjects : form.projects,
                      socials: {
                        ...form.socials,
                        website: data.blog || form.socials.website,
                        twitter: data.twitter_username || form.socials.twitter,
                      }
                    });
                  } catch (e) {
                    console.error("Failed to fetch profile", e);
                  }
                }}
                className="rounded-lg bg-[oklch(0.7_0.24_295)] px-3 text-sm font-medium text-background hover:opacity-90 disabled:opacity-50"
                disabled={!form.username.trim()}
              >
                Fetch
              </button>
            </div>
          </Field>

          <Row cols={2}>
            <Field label="Display Name">
              <Input value={form.displayName} onChange={upd("displayName")} placeholder="John Doe" />
            </Field>
            <Field label="Tagline">
              <Input value={form.tagline} onChange={upd("tagline")} placeholder="Building things..." />
            </Field>
          </Row>

          <Row cols={2}>
            <Field label="Role">
              <Input value={form.role} onChange={upd("role")} placeholder="Developer" />
            </Field>
            <Field label="Location">
              <Input value={form.location} onChange={upd("location")} placeholder="San Francisco" />
            </Field>
          </Row>

          <Field label="Bio">
            <Textarea value={form.bio} onChange={upd("bio")} placeholder="A few words about yourself..." />
          </Field>
        </Section>
      )}

      {/* ── Typing Section Fields ── */}
      {isVisible("typing") && (
        <Section icon={Code2} title="Typing Animation">
          <p className="text-xs text-muted-foreground mb-3">
            Custom strings for your Typing SVG animation.
          </p>
          <Field label="Current Work">
            <Input value={form.currentlyWorkingOn} onChange={upd("currentlyWorkingOn")} placeholder="Building a SaaS..." />
          </Field>
          <Field label="Learning">
            <Input value={form.currentlyLearning} onChange={upd("currentlyLearning")} placeholder="Rust & AI..." />
          </Field>
        </Section>
      )}

      {/* ── Tech Stack / Skills ── */}
      {(isVisible("techStack") || isVisible("skills")) && (
        <Section icon={Cpu} title={isVisible("skills") ? "Skills" : "Tech Stack"} defaultOpen>
          <Field label="Languages & Frameworks">
            <TagInput
              tags={form.techStack}
              onChange={upd2("techStack")}
              placeholder="React, Node, Python..."
            />
          </Field>
          <Field label="Tools & Platforms">
            <TagInput
              tags={form.tools}
              onChange={upd2("tools")}
              placeholder="Docker, AWS, Git..."
            />
          </Field>
        </Section>
      )}

      {/* ── Projects ── */}
      {isVisible("projects") && (
        <Section icon={Folder} title="Projects" defaultOpen>
          <ProjectsEditor />
        </Section>
      )}

      {/* ── Social Links ── */}
      {isVisible("socials") && (
        <Section icon={Link2} title="Social Links">
          <div className="grid gap-3 sm:grid-cols-2">
            {SOCIAL_OPTIONS.map((opt) => {
              const val = opt.key === "github" ? form.username : form.socials[opt.key] || "";
              // For GitHub, we always show it. For others, only if they have a value.
              // We'll manage "adding" via a separate UI below.
              if (opt.key !== "github" && !val) return null;

              return (
                <div key={opt.key} className="group relative">
                  <div className="flex items-center justify-between mb-1.5">
                    <Label>{opt.label}</Label>
                    {opt.key !== "github" && (
                      <button 
                        onClick={() => updateSocial(opt.key, "")}
                        className="p-1 text-muted-foreground hover:text-destructive transition-colors"
                        title="Remove"
                      >
                        <X className="h-3.5 w-3.5" />
                      </button>
                    )}
                  </div>
                  <div className="relative">
                    <div 
                      className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 flex items-center justify-center opacity-70"
                      style={{ color: `#${opt.color}` }}
                    >
                      <Globe className="h-3.5 w-3.5" />
                    </div>
                    <input
                      value={val}
                      onChange={(e) => {
                        if (opt.key === "github") updateForm({ username: e.target.value });
                        else updateSocial(opt.key, e.target.value);
                      }}
                      placeholder={opt.prefix ? "username / email" : "profile link or username"}
                      className="w-full rounded-lg border border-border/60 bg-background/50 py-2 pl-9 pr-3 text-sm outline-none transition-colors focus:border-[oklch(0.7_0.24_295)]"
                    />
                  </div>
                </div>
              );
            })}
          </div>

          <div className="mt-4 border-t border-border/40 pt-4">
            <label className="mb-2 block text-xs font-medium text-muted-foreground uppercase tracking-wider">Add Social Platform</label>
            <div className="flex flex-wrap gap-2">
              {SOCIAL_OPTIONS.filter(opt => opt.key !== "github" && !form.socials[opt.key]).map(opt => (
                <button
                  key={opt.key}
                  onClick={() => updateSocial(opt.key, " ")} // set to a space to "activate" it
                  className="inline-flex items-center gap-1.5 rounded-full border border-border/60 bg-card/40 px-3 py-1.5 text-xs font-medium text-muted-foreground hover:border-border/80 hover:text-foreground transition-all"
                >
                  <Plus className="h-3 w-3" />
                  {opt.label}
                </button>
              ))}
            </div>
          </div>
        </Section>
      )}

      {/* ── Quote ── */}
      {isVisible("quote") && (
        <Section icon={Quote} title="Quote">
          <Field label="Favorite Quote">
            <Textarea value={form.quote} onChange={upd("quote")} placeholder="Your inspiration..." />
          </Field>
        </Section>
      )}

      {/* ── LeetCode (Optional) ── */}
      {isVisible("leetcode") && (
        <Section icon={Code2} title="LeetCode">
          <Field label="LeetCode Username">
            <Input 
              value={form.socials.leetcode} 
              onChange={(v) => updateSocial("leetcode", v)} 
              placeholder="Username" 
            />
          </Field>
        </Section>
      )}

      {/* ── Spotify (Optional) ── */}
      {isVisible("spotify") && (
        <Section icon={Star} title="Spotify">
          <Field label="Spotify User ID">
            <Input 
              value={form.socials.spotify} 
              onChange={(v) => updateSocial("spotify", v)} 
              placeholder="Your ID..." 
            />
          </Field>
        </Section>
      )}

      {/* ── Extra Fields for Templates ── */}
      {templateConfig.kind === "markdown" && (
        <TemplateSpecificFields placeholders={placeholders} />
      )}
    </div>
  );
}
