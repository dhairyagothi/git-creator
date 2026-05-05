import { useState, useCallback, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  User, MapPin, Mail, Code2, Briefcase, BookOpen, Link2,
  Plus, X, ChevronDown, Folder, Quote, Star,
  Sparkles, GraduationCap, Globe, FileText, Hash, Cpu,
} from "lucide-react";
import { useAppStore } from "@/lib/store";
import { getTemplate, getTemplatePlaceholders } from "@/lib/templates";
import { AUTO_PLACEHOLDER_KEYS, getPlaceholderLabel } from "@/lib/templateFields";
import type { FormState } from "@/lib/types";

/* ── helpers ───────────────────────────────────────────────────────────── */

function useFormField<K extends keyof FormState>(key: K) {
  const value = useAppStore((s) => s.form[key]);
  const updateForm = useAppStore((s) => s.updateForm);
  const set = useCallback((v: FormState[K]) => updateForm({ [key]: v } as Partial<FormState>), [key, updateForm]);
  return [value, set] as const;
}

/* ── sub-components ─────────────────────────────────────────────────────── */

function Label({ children, required }: { children: React.ReactNode; required?: boolean }) {
  return (
    <label className="mb-1.5 block text-xs font-medium text-foreground/80">
      {children}
      {required && <span className="ml-1 text-[oklch(0.7_0.24_295)]">*</span>}
    </label>
  );
}

function Input({
  value, onChange, placeholder, type = "text", className = "",
}: {
  value: string; onChange: (v: string) => void; placeholder?: string;
  type?: string; className?: string;
}) {
  return (
    <input
      type={type}
      value={value}
      onChange={(e) => onChange(e.target.value)}
      placeholder={placeholder}
      className={`w-full rounded-lg border border-border/60 bg-background/50 px-3 py-2 text-sm text-foreground placeholder:text-muted-foreground/50 outline-none transition-colors focus:border-[oklch(0.7_0.24_295)] focus:bg-background/80 ${className}`}
    />
  );
}

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

function TagInput({
  tags, onChange, placeholder,
}: {
  tags: string[]; onChange: (tags: string[]) => void; placeholder?: string;
}) {
  const [input, setInput] = useState("");
  const inputRef = useRef<HTMLInputElement>(null);

  const add = (raw: string) => {
    const items = raw.split(",").map((s) => s.trim()).filter(Boolean);
    const next = [...new Set([...tags, ...items])];
    onChange(next);
    setInput("");
  };

  const remove = (i: number) => onChange(tags.filter((_, idx) => idx !== i));

  return (
    <div
      className="min-h-[40px] w-full cursor-text rounded-lg border border-border/60 bg-background/50 px-2 py-1.5 transition-colors focus-within:border-[oklch(0.7_0.24_295)] focus-within:bg-background/80"
      onClick={() => inputRef.current?.focus()}
    >
      <div className="flex flex-wrap gap-1.5">
        {tags.map((t, i) => (
          <span
            key={i}
            className="inline-flex items-center gap-1 rounded-md bg-[oklch(0.7_0.24_295)]/15 px-2 py-0.5 text-xs text-[oklch(0.78_0.18_295)] border border-[oklch(0.7_0.24_295)]/30"
          >
            {t}
            <button
              onClick={(e) => { e.stopPropagation(); remove(i); }}
              className="opacity-60 hover:opacity-100 transition-opacity"
            >
              <X className="h-3 w-3" />
            </button>
          </span>
        ))}
        <input
          ref={inputRef}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => {
            if ((e.key === "Enter" || e.key === ",") && input.trim()) {
              e.preventDefault();
              add(input);
            } else if (e.key === "Backspace" && !input && tags.length) {
              remove(tags.length - 1);
            }
          }}
          onBlur={() => { if (input.trim()) add(input); }}
          placeholder={tags.length ? "" : placeholder}
          className="min-w-[120px] flex-1 bg-transparent text-sm text-foreground placeholder:text-muted-foreground/50 outline-none"
        />
      </div>
    </div>
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

function Section({
  icon: Icon, title, badge, children, defaultOpen = true,
}: {
  icon: React.ElementType; title: string; badge?: string;
  children: React.ReactNode; defaultOpen?: boolean;
}) {
  const [open, setOpen] = useState(defaultOpen);
  return (
    <div className="rounded-xl border border-border/40 bg-card/20 overflow-hidden">
      <button
        onClick={() => setOpen((v) => !v)}
        className="flex w-full items-center gap-2.5 px-4 py-3 text-left hover:bg-card/30 transition-colors"
      >
        <div className="flex h-6 w-6 items-center justify-center rounded-md bg-gradient-to-br from-[oklch(0.7_0.24_295)]/20 to-[oklch(0.65_0.28_200)]/20">
          <Icon className="h-3.5 w-3.5 text-[oklch(0.78_0.18_295)]" />
        </div>
        <span className="flex-1 text-sm font-semibold">{title}</span>
        {badge && (
          <span className="rounded-full bg-[oklch(0.7_0.24_295)]/15 px-2 py-0.5 text-[10px] font-medium text-[oklch(0.78_0.18_295)]">
            {badge}
          </span>
        )}
        <ChevronDown
          className={`h-4 w-4 text-muted-foreground transition-transform duration-200 ${open ? "rotate-180" : ""}`}
        />
      </button>
      <AnimatePresence initial={false}>
        {open && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.2, ease: "easeInOut" }}
            className="overflow-hidden"
          >
            <div className="space-y-4 px-4 pb-4">{children}</div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

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
  const { template, form, updateForm, updateSocial } = useAppStore();
  const templateConfig = getTemplate(template);
  const placeholders = getTemplatePlaceholders(template);

  const needs = (keys: string[]) =>
    templateConfig.kind === "builder" || keys.some((k) => placeholders.includes(k));

  const upd = (key: keyof FormState) => (val: string) => updateForm({ [key]: val } as Partial<FormState>);
  const upd2 = (key: keyof FormState) => (val: string[]) => updateForm({ [key]: val } as Partial<FormState>);

  return (
    <div className="space-y-3">
      <Section icon={User} title="Identity" defaultOpen>
        <Field label="GitHub Username" required>
          <div className="relative">
            <span className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground text-sm select-none">@</span>
            <Input
              value={form.username}
              onChange={upd("username")}
              placeholder="octocat"
              className="pl-7"
            />
          </div>
        </Field>

        {needs(["YOUR_NAME"]) && (
          <Field label="Display Name">
            <Input value={form.displayName} onChange={upd("displayName")} placeholder="John Doe" />
          </Field>
        )}

        <Field label="Tagline">
          <Input value={form.tagline} onChange={upd("tagline")} placeholder="Building things on the internet" />
        </Field>

        {needs(["YOUR_ROLE", "YOUR_TITLE"]) && (
          <Row cols={2}>
            <Field label="Role">
              <Input value={form.role} onChange={upd("role")} placeholder="Full Stack Developer" />
            </Field>
            <Field label="Title">
              <Input value={form.title} onChange={upd("title")} placeholder="Senior Engineer" />
            </Field>
          </Row>
        )}

        {needs(["YOUR_COMPANY"]) && (
          <Field label="Company">
            <div className="relative">
              <Briefcase className="absolute left-3 top-1/2 -translate-y-1/2 h-3.5 w-3.5 text-muted-foreground" />
              <Input value={form.company} onChange={upd("company")} placeholder="Acme Corp" className="pl-8" />
            </div>
          </Field>
        )}

        {needs(["YOUR_FOCUS", "YOUR_RESEARCH_AREA"]) && (
          <Field label="Focus / Specialty">
            <Input value={form.focus} onChange={upd("focus")} placeholder="Web performance, DX, open source..." />
          </Field>
        )}

        {needs(["YOUR_BIO"]) && (
          <Field label="Bio">
            <Textarea value={form.bio} onChange={upd("bio")} placeholder="A few words about yourself..." />
          </Field>
        )}

        {templateConfig.kind === "builder" && (
          <Field label="Bio">
            <Textarea value={form.bio} onChange={upd("bio")} placeholder="A few words about yourself..." />
          </Field>
        )}
      </Section>

      {needs(["YOUR_LOCATION", "YOUR_CITY", "YOUR_COUNTRY", "YOUR_EMAIL"]) && (
        <Section icon={MapPin} title="Location & Contact">
          {needs(["YOUR_CITY", "YOUR_COUNTRY"]) ? (
            <Row cols={2}>
              <Field label="City">
                <Input value={form.city} onChange={upd("city")} placeholder="San Francisco" />
              </Field>
              <Field label="Country">
                <Input value={form.country} onChange={upd("country")} placeholder="USA" />
              </Field>
            </Row>
          ) : (
            <Field label="Location">
              <div className="relative">
                <MapPin className="absolute left-3 top-1/2 -translate-y-1/2 h-3.5 w-3.5 text-muted-foreground" />
                <Input value={form.location} onChange={upd("location")} placeholder="San Francisco, USA" className="pl-8" />
              </div>
            </Field>
          )}

          {needs(["YOUR_EMAIL"]) && (
            <Field label="Email">
              <div className="relative">
                <Mail className="absolute left-3 top-1/2 -translate-y-1/2 h-3.5 w-3.5 text-muted-foreground" />
                <Input type="email" value={form.email} onChange={upd("email")} placeholder="you@example.com" className="pl-8" />
              </div>
            </Field>
          )}
        </Section>
      )}

      {needs(["YOUR_PROJECT", "YOUR_LEARNING", "YOUR_CURRENTLY_LEARNING", "YOUR_GOAL"]) && (
        <Section icon={BookOpen} title="Currently">
          {needs(["YOUR_PROJECT", "YOUR_CURRENT_FOCUS"]) && (
            <Field label="Working On">
              <Input value={form.currentlyWorkingOn} onChange={upd("currentlyWorkingOn")} placeholder="A cool open source project..." />
            </Field>
          )}
          {needs(["YOUR_LEARNING", "YOUR_CURRENTLY_LEARNING"]) && (
            <Field label="Currently Learning">
              <Input value={form.currentlyLearning} onChange={upd("currentlyLearning")} placeholder="Rust, WebAssembly, AI..." />
            </Field>
          )}
          {needs(["YOUR_GOAL"]) && (
            <Field label="Contribution Goals">
              <Input value={form.contributionGoals} onChange={upd("contributionGoals")} placeholder="Contribute to 10 OSS projects this year" />
            </Field>
          )}
        </Section>
      )}

      {needs(["YOUR_TOPICS", "YOUR_SKILLS", "YOUR_TECH_1", "YOUR_TECH_2"]) && (
        <Section icon={Code2} title="Tech Stack">
          <Field label="Languages & Frameworks">
            <TagInput
              tags={form.techStack}
              onChange={upd2("techStack")}
              placeholder="React, TypeScript, Python… (comma or Enter)"
            />
            <p className="mt-1.5 text-[11px] text-muted-foreground">Comma-separated or press Enter to add each item.</p>
          </Field>
          <Field label="Tools & DevOps">
            <TagInput
              tags={form.tools}
              onChange={upd2("tools")}
              placeholder="Docker, AWS, Git, Figma…"
            />
          </Field>
        </Section>
      )}

      {needs(["YOUR_PROJECT_1", "YOUR_PROJECT_2", "YOUR_OSS_PROJECT_1", "YOUR_PROJECT_1_DESC", "YOUR_PROJECT_2_DESC", "YOUR_PROJECT_3_DESC", "YOUR_PROJECT_4_DESC"]) && (
        <Section icon={Folder} title="Projects" defaultOpen={false}>
          <ProjectsEditor />
        </Section>
      )}

      {needs(["YOUR_UNIVERSITY", "YOUR_MAJOR", "YOUR_YEAR"]) && (
        <Section icon={GraduationCap} title="Education">
          <Field label="University / School">
            <Input value={form.university} onChange={upd("university")} placeholder="MIT" />
          </Field>
          <Row cols={2}>
            <Field label="Major / Field">
              <Input value={form.major} onChange={upd("major")} placeholder="Computer Science" />
            </Field>
            <Field label="Year / Level">
              <Input value={form.academicYear} onChange={upd("academicYear")} placeholder="3rd Year" />
            </Field>
          </Row>
        </Section>
      )}

      {needs(["YOUR_YEARS", "YOUR_RESUME_URL", "YOUR_SCHOLAR_ID"]) && (
        <Section icon={Cpu} title="Experience">
          <Row cols={2}>
            <Field label="Years of Experience">
              <Input value={form.experienceYears} onChange={upd("experienceYears")} placeholder="5" />
            </Field>
          </Row>
          {needs(["YOUR_RESUME_URL"]) && (
            <Field label="Resume URL">
              <div className="relative">
                <FileText className="absolute left-3 top-1/2 -translate-y-1/2 h-3.5 w-3.5 text-muted-foreground" />
                <Input value={form.resumeUrl} onChange={upd("resumeUrl")} placeholder="https://..." className="pl-8" />
              </div>
            </Field>
          )}
          {needs(["YOUR_SCHOLAR_ID"]) && (
            <Field label="Google Scholar ID">
              <Input value={form.scholarId} onChange={upd("scholarId")} placeholder="abc123XYZ" />
            </Field>
          )}
        </Section>
      )}

      <Section icon={Link2} title="Social Links" defaultOpen={false}>
        {([
          { key: "twitter", icon: Hash, label: "Twitter / X", prefix: "@", placeholder: "username" },
          { key: "linkedin", icon: Link2, label: "LinkedIn", prefix: "in/", placeholder: "username" },
          { key: "website", icon: Globe, label: "Website / Portfolio", prefix: "", placeholder: "https://yoursite.com" },
          { key: "youtube", icon: Hash, label: "YouTube", prefix: "@", placeholder: "channel" },
          { key: "devto", icon: Hash, label: "DEV.to", prefix: "@", placeholder: "username" },
          { key: "instagram", icon: Hash, label: "Instagram", prefix: "@", placeholder: "username" },
        ] as const).map(({ key, icon: Icon, label, prefix, placeholder }) => (
          <div key={key}>
            <Label>{label}</Label>
            <div className="relative flex items-center">
              <Icon className="absolute left-3 h-3.5 w-3.5 text-muted-foreground" />
              {prefix && (
                <span className="absolute left-8 text-sm text-muted-foreground select-none">{prefix}</span>
              )}
              <input
                value={form.socials[key]}
                onChange={(e) => updateSocial(key, e.target.value)}
                placeholder={placeholder}
                className={`w-full rounded-lg border border-border/60 bg-background/50 py-2 pr-3 text-sm text-foreground placeholder:text-muted-foreground/50 outline-none transition-colors focus:border-[oklch(0.7_0.24_295)] focus:bg-background/80 ${
                  prefix ? (prefix.length > 2 ? "pl-14" : "pl-9") : "pl-9"
                }`}
              />
            </div>
          </div>
        ))}
      </Section>

      {needs([
        "YOUR_QUOTE", "YOUR_FUN_FACT", "YOUR_FUN_FACT_1", "YOUR_FUN_FACT_2", "YOUR_FUN_FACT_3", "YOUR_FUN_FACT_4",
        "YOUR_ACHIEVEMENT_1", "YOUR_ACHIEVEMENT_2", "YOUR_ACHIEVEMENT_3", "YOUR_ACHIEVEMENT_4",
        "YOUR_GIF_1", "YOUR_GIF_2"
      ]) && (
        <Section icon={Star} title="Extras" defaultOpen={false}>
          {needs(["YOUR_QUOTE"]) && (
            <Field label="Favorite Quote">
              <div className="relative">
                <Quote className="absolute left-3 top-3 h-3.5 w-3.5 text-muted-foreground" />
                <Textarea
                  value={form.quote}
                  onChange={upd("quote")}
                  placeholder="A quote that inspires you..."
                />
              </div>
            </Field>
          )}
          {needs(["YOUR_FUN_FACT", "YOUR_FUN_FACT_1", "YOUR_FUN_FACT_2", "YOUR_FUN_FACT_3", "YOUR_FUN_FACT_4"]) && (
            <Field label="Fun Facts">
              <ListEditor
                items={form.funFacts}
                onChange={upd2("funFacts")}
                placeholder="I can solve a Rubik's cube in 30s..."
              />
            </Field>
          )}
          {needs(["YOUR_ACHIEVEMENT_1", "YOUR_ACHIEVEMENT_2", "YOUR_ACHIEVEMENT_3", "YOUR_ACHIEVEMENT_4"]) && (
            <Field label="Achievements">
              <ListEditor
                items={form.achievements}
                onChange={upd2("achievements")}
                placeholder="Speaker at ReactConf 2024..."
              />
            </Field>
          )}
          {needs(["YOUR_GIF_1", "YOUR_GIF_2"]) && (
            <Field label="GIF URLs">
              <ListEditor
                items={form.gifs}
                onChange={upd2("gifs")}
                placeholder="https://media.giphy.com/media/.../giphy.gif"
              />
            </Field>
          )}
        </Section>
      )}

      {templateConfig.kind === "markdown" && (
        <TemplateSpecificFields placeholders={placeholders} />
      )}
    </div>
  );
}
