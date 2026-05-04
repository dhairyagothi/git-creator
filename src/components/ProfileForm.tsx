import { useState } from "react";
import { toast } from "sonner";
import { Loader2, Search, Plus, Trash2 } from "lucide-react";
import { useAppStore } from "@/lib/store";
import { getTemplate } from "@/lib/templates";
import { AUTO_PLACEHOLDER_KEYS, getPlaceholderLabel } from "@/lib/templateFields";
import { Field, Input, Textarea } from "./FormPrimitives";
import { TagInput } from "./TagInput";

async function fetchGithubUser(username: string) {
  const res = await fetch(`https://api.github.com/users/${encodeURIComponent(username)}`);
  if (!res.ok) throw new Error("Profile not found");
  return res.json() as Promise<{
    name?: string;
    bio?: string;
    avatar_url?: string;
    location?: string;
    blog?: string;
    twitter_username?: string;
  }>;
}

export function ProfileForm() {
  const { form, template, updateForm, updateSocial, updateTemplateField } = useAppStore();
  const [loading, setLoading] = useState(false);
  const templateConfig = getTemplate(template);
  const templatePlaceholders = templateConfig.kind === "markdown" ? templateConfig.placeholders ?? [] : [];
  const templateFields = templatePlaceholders.filter((key) => !AUTO_PLACEHOLDER_KEYS.has(key));
  const isLongField = (key: string) => /SUMMARY|DESC|BIO|QUOTE|THREAD|REPORTS|DATA/.test(key);

  const onFetch = async () => {
    if (!form.username) {
      toast.error("Enter a GitHub username first");
      return;
    }
    setLoading(true);
    try {
      const data = await fetchGithubUser(form.username);
      updateForm({
        displayName: data.name || form.displayName,
        bio: data.bio || form.bio,
        avatarUrl: data.avatar_url || form.avatarUrl,
        location: data.location || form.location,
      });
      if (data.blog) updateSocial("website", data.blog);
      if (data.twitter_username) updateSocial("twitter", data.twitter_username);
      toast.success(`Profile loaded for @${form.username}`);
    } catch (e) {
      toast.error("Could not fetch profile. Check the username.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6">
      <Section title="GitHub">
        <Field label="GitHub username" hint="Used for stats & auto-fill">
          <div className="flex gap-2">
            <Input
              value={form.username}
              onChange={(e) => updateForm({ username: e.target.value.replace(/\s/g, "") })}
              placeholder="octocat"
            />
            <button
              onClick={onFetch}
              disabled={loading}
              className="inline-flex h-10 items-center gap-1.5 rounded-lg bg-gradient-neon px-3 text-xs font-medium text-background shadow-[var(--shadow-glow)] transition-transform hover:scale-[1.03] disabled:opacity-60"
            >
              {loading ? <Loader2 className="h-3.5 w-3.5 animate-spin" /> : <Search className="h-3.5 w-3.5" />}
              Fetch
            </button>
          </div>
        </Field>
      </Section>

      <Section title="Identity">
        <div className="grid gap-4 md:grid-cols-2">
          <Field label="Display name">
            <Input value={form.displayName} onChange={(e) => updateForm({ displayName: e.target.value })} placeholder="Alex Doe" />
          </Field>
          <Field label="Tagline">
            <Input value={form.tagline} onChange={(e) => updateForm({ tagline: e.target.value })} placeholder="Building things on the internet" />
          </Field>
        </div>
        <div className="grid gap-4 md:grid-cols-2">
          <Field label="Role">
            <Input value={form.role} onChange={(e) => updateForm({ role: e.target.value })} placeholder="Full stack developer" />
          </Field>
          <Field label="Focus">
            <Input value={form.focus} onChange={(e) => updateForm({ focus: e.target.value })} placeholder="Design systems, DX" />
          </Field>
        </div>
        <Field label="Bio / intro">
          <Textarea rows={3} value={form.bio} onChange={(e) => updateForm({ bio: e.target.value })} placeholder="Short intro about yourself..." />
        </Field>
        <div className="grid gap-4 md:grid-cols-2">
          <Field label="Location">
            <Input value={form.location} onChange={(e) => updateForm({ location: e.target.value })} placeholder="Berlin, Germany" />
          </Field>
          <Field label="City">
            <Input value={form.city} onChange={(e) => updateForm({ city: e.target.value })} placeholder="Berlin" />
          </Field>
        </div>
        <div className="grid gap-4 md:grid-cols-2">
          <Field label="Country">
            <Input value={form.country} onChange={(e) => updateForm({ country: e.target.value })} placeholder="Germany" />
          </Field>
          <Field label="Contact email">
            <Input type="email" value={form.email} onChange={(e) => updateForm({ email: e.target.value })} placeholder="hi@example.com" />
          </Field>
        </div>
      </Section>

      <Section title="Professional">
        <div className="grid gap-4 md:grid-cols-2">
          <Field label="Title">
            <Input value={form.title} onChange={(e) => updateForm({ title: e.target.value })} placeholder="Senior Software Engineer" />
          </Field>
          <Field label="Company">
            <Input value={form.company} onChange={(e) => updateForm({ company: e.target.value })} placeholder="Acme Corp" />
          </Field>
        </div>
        <div className="grid gap-4 md:grid-cols-2">
          <Field label="Experience (years)">
            <Input value={form.experienceYears} onChange={(e) => updateForm({ experienceYears: e.target.value })} placeholder="5" />
          </Field>
          <Field label="Resume URL">
            <Input value={form.resumeUrl} onChange={(e) => updateForm({ resumeUrl: e.target.value })} placeholder="https://..." />
          </Field>
        </div>
      </Section>

      <Section title="Education">
        <div className="grid gap-4 md:grid-cols-2">
          <Field label="University">
            <Input value={form.university} onChange={(e) => updateForm({ university: e.target.value })} placeholder="Stanford University" />
          </Field>
          <Field label="Major">
            <Input value={form.major} onChange={(e) => updateForm({ major: e.target.value })} placeholder="Computer Science" />
          </Field>
        </div>
        <div className="grid gap-4 md:grid-cols-2">
          <Field label="Academic year">
            <Input value={form.academicYear} onChange={(e) => updateForm({ academicYear: e.target.value })} placeholder="2026" />
          </Field>
          <Field label="Scholar ID">
            <Input value={form.scholarId} onChange={(e) => updateForm({ scholarId: e.target.value })} placeholder="Google Scholar ID" />
          </Field>
        </div>
      </Section>

      <Section title="Currently">
        <div className="grid gap-4 md:grid-cols-2">
          <Field label="Working on">
            <Input value={form.currentlyWorkingOn} onChange={(e) => updateForm({ currentlyWorkingOn: e.target.value })} placeholder="A side project..." />
          </Field>
          <Field label="Learning">
            <Input value={form.currentlyLearning} onChange={(e) => updateForm({ currentlyLearning: e.target.value })} placeholder="Rust, distributed systems" />
          </Field>
        </div>
        <Field label="Contribution goals">
          <Input value={form.contributionGoals} onChange={(e) => updateForm({ contributionGoals: e.target.value })} placeholder="500 commits this year" />
        </Field>
      </Section>

      <Section title="Stack">
        <Field label="Tech stack" hint="Press Enter to add">
          <TagInput value={form.techStack} onChange={(v) => updateForm({ techStack: v })} placeholder="React, TypeScript, Node..." />
        </Field>
        <Field label="Tools" hint="Editors, infra, design tools">
          <TagInput value={form.tools} onChange={(v) => updateForm({ tools: v })} placeholder="Docker, Figma, AWS..." />
        </Field>
      </Section>

      <Section title="Projects">
        <div className="space-y-2">
          {form.projects.map((p, i) => (
            <div key={i} className="grid gap-2 rounded-lg border border-border/60 bg-background/30 p-3 md:grid-cols-[1fr_2fr_1fr_auto]">
              <Input
                value={p.name}
                onChange={(e) => {
                  const next = [...form.projects];
                  next[i] = { ...p, name: e.target.value };
                  updateForm({ projects: next });
                }}
                placeholder="Project name"
              />
              <Input
                value={p.description}
                onChange={(e) => {
                  const next = [...form.projects];
                  next[i] = { ...p, description: e.target.value };
                  updateForm({ projects: next });
                }}
                placeholder="Short description"
              />
              <Input
                value={p.url}
                onChange={(e) => {
                  const next = [...form.projects];
                  next[i] = { ...p, url: e.target.value };
                  updateForm({ projects: next });
                }}
                placeholder="https://..."
              />
              <button
                onClick={() => updateForm({ projects: form.projects.filter((_, idx) => idx !== i) })}
                className="inline-flex h-10 w-10 items-center justify-center rounded-lg border border-border/60 hover:bg-destructive/20 hover:text-destructive transition-colors"
                aria-label="Remove project"
              >
                <Trash2 className="h-4 w-4" />
              </button>
            </div>
          ))}
          <button
            onClick={() => updateForm({ projects: [...form.projects, { name: "", description: "", url: "" }] })}
            className="inline-flex items-center gap-1.5 rounded-lg border border-dashed border-border/60 px-3 py-2 text-xs text-muted-foreground hover:bg-card/40 hover:text-foreground transition-colors"
          >
            <Plus className="h-3.5 w-3.5" /> Add project
          </button>
        </div>
      </Section>

      <Section title="Social links">
        <div className="grid gap-4 md:grid-cols-2">
          <Field label="Twitter / X handle"><Input value={form.socials.twitter} onChange={(e) => updateSocial("twitter", e.target.value.replace(/^@/, ""))} placeholder="username" /></Field>
          <Field label="LinkedIn handle"><Input value={form.socials.linkedin} onChange={(e) => updateSocial("linkedin", e.target.value)} placeholder="username" /></Field>
          <Field label="Website"><Input value={form.socials.website} onChange={(e) => updateSocial("website", e.target.value)} placeholder="https://..." /></Field>
          <Field label="YouTube"><Input value={form.socials.youtube} onChange={(e) => updateSocial("youtube", e.target.value)} placeholder="channel" /></Field>
          <Field label="DEV.to"><Input value={form.socials.devto} onChange={(e) => updateSocial("devto", e.target.value)} placeholder="username" /></Field>
          <Field label="Instagram"><Input value={form.socials.instagram} onChange={(e) => updateSocial("instagram", e.target.value)} placeholder="username" /></Field>
        </div>
      </Section>

      {templateFields.length > 0 && (
        <Section title="Template fields">
          <div className="grid gap-4 md:grid-cols-2">
            {templateFields.map((key) => (
              <Field key={key} label={getPlaceholderLabel(key)}>
                {isLongField(key) ? (
                  <Textarea
                    rows={3}
                    value={form.templateFields?.[key] ?? ""}
                    onChange={(e) => updateTemplateField(key, e.target.value)}
                    placeholder={key.replace(/_/g, " ")}
                  />
                ) : (
                  <Input
                    value={form.templateFields?.[key] ?? ""}
                    onChange={(e) => updateTemplateField(key, e.target.value)}
                    placeholder={key.replace(/_/g, " ")}
                  />
                )}
              </Field>
            ))}
          </div>
        </Section>
      )}

      <Section title="Extras">
        <Field label="Fun facts" hint="Press Enter to add">
          <TagInput value={form.funFacts} onChange={(v) => updateForm({ funFacts: v })} placeholder="I can solve a Rubik's cube..." />
        </Field>
        <Field label="Achievements">
          <TagInput value={form.achievements} onChange={(v) => updateForm({ achievements: v })} placeholder="Hackathon winner..." />
        </Field>
        <Field label="Favorite quote">
          <Input value={form.quote} onChange={(e) => updateForm({ quote: e.target.value })} placeholder="Stay hungry, stay foolish." />
        </Field>
      </Section>
    </div>
  );
}

function Section({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="glass rounded-xl p-5">
      <div className="mb-4 flex items-center gap-2">
        <span className="h-1.5 w-1.5 rounded-full bg-gradient-neon" />
        <h3 className="text-xs font-semibold uppercase tracking-[0.15em] text-muted-foreground">{title}</h3>
      </div>
      <div className="space-y-4">{children}</div>
    </div>
  );
}
