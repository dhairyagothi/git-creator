import { createFileRoute, useNavigate } from "@tanstack/react-router";
import { useMemo, useState } from "react";
import { motion } from "framer-motion";
import { Code2, ArrowRight, Loader2 } from "lucide-react";
import { z } from "zod";
import { Navbar } from "@/components/Navbar";
import { useAppStore } from "@/lib/store";

const PREFILL_KEY = "gra_prefill_v1";

const searchSchema = z.object({
  template: z.string().optional(),
});

export const Route = createFileRoute("/user-datails")({
  validateSearch: searchSchema,
  head: () => ({
    meta: [
      { title: "GitHub Profile — github-readme.app" },
      { name: "description", content: "Fetch your GitHub profile details to pre-fill your README." },
    ],
  }),
  component: UserDetailsPage,
});

function UserDetailsPage() {
  const navigate = useNavigate();
  const { template } = Route.useSearch();
  const { form, updateForm } = useAppStore();
  const [username, setUsername] = useState(form.username || "");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const canSubmit = useMemo(() => !!username.trim() && !loading, [username, loading]);

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!username.trim()) {
      setError("Please enter your GitHub username.");
      return;
    }

    setError(null);
    setLoading(true);

    try {
      const res = await fetch(`https://api.github.com/users/${encodeURIComponent(username.trim())}`);
      if (!res.ok) {
        if (res.status === 403) {
          throw new Error("GitHub rate limit reached. Try again later.");
        }
        if (res.status === 404) {
          throw new Error("Profile not found");
        }
        throw new Error("GitHub API error");
      }
      const data = await res.json() as {
        name?: string;
        bio?: string;
        avatar_url?: string;
        location?: string;
        blog?: string;
        twitter_username?: string;
        public_repos?: number;
        followers?: number;
      };

      const reposRes = await fetch(
        `https://api.github.com/users/${encodeURIComponent(username.trim())}/repos?per_page=100&sort=updated`,
      );
      const repos = reposRes.ok ? await reposRes.json() as Array<{ stargazers_count?: number; language?: string | null }> : [];

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

      const nextSocials = {
        ...form.socials,
        website: data.blog || form.socials.website,
        twitter: data.twitter_username || form.socials.twitter,
      };

      const patch = {
        username: username.trim(),
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
        socials: nextSocials,
      };

      updateForm(patch);
      localStorage.setItem(PREFILL_KEY, JSON.stringify({ form: patch }));

      navigate({
        to: "/generator",
        search: template ? { template, username: username.trim() } : { username: username.trim() },
      });
    } catch (err) {
      const message = err instanceof Error ? err.message : "Could not load that profile.";
      setError(message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen">
      <Navbar />
      <section className="relative mx-auto flex min-h-[calc(100vh-96px)] max-w-6xl items-center justify-center px-6 pb-20 pt-10">
        <div className="absolute inset-0 -z-10">
          <div className="absolute left-1/2 top-16 h-64 w-64 -translate-x-1/2 rounded-full bg-[radial-gradient(circle,rgba(120,255,103,0.35),transparent_70%)] blur-2xl" />
          <div className="absolute right-10 top-32 h-72 w-72 rounded-full bg-[radial-gradient(circle,rgba(82,39,255,0.35),transparent_70%)] blur-3xl" />
          <div className="absolute bottom-16 left-10 h-72 w-72 rounded-full bg-[radial-gradient(circle,rgba(255,159,252,0.28),transparent_70%)] blur-3xl" />
        </div>

        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="glass relative w-full max-w-2xl overflow-hidden rounded-3xl border border-border/50 p-8 shadow-[var(--shadow-elegant)]"
        >
          <div className="absolute right-0 top-0 h-24 w-24 rounded-full bg-gradient-neon opacity-20 blur-2xl" />
          <div className="flex items-center gap-4">
            <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-card/70">
              <Code2 className="h-6 w-6 text-foreground" />
            </div>
            <div>
              <div className="text-xs uppercase tracking-[0.2em] text-muted-foreground">GitHub Profile</div>
              <h1 className="mt-2 text-2xl font-semibold">Please enter your GitHub username</h1>
            </div>
          </div>

          <p className="mt-4 text-sm text-muted-foreground">
            provide your GitHub username to fetch your profile details and pre-fill your README. You can edit everything later in the generator.
          </p>

          <form onSubmit={onSubmit} className="mt-8 space-y-4">
            <div>
              <label className="mb-2 block text-xs font-medium text-foreground/80">GitHub username</label>
              <div className="relative">
                <span className="absolute left-3 top-1/2 -translate-y-1/2 text-sm text-muted-foreground">@</span>
                <input
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  placeholder="dhairyagothi"
                  className="w-full rounded-xl border border-border/60 bg-background/60 py-3 pl-9 pr-4 text-sm text-foreground outline-none transition-colors focus:border-[oklch(0.7_0.24_295)]"
                />
              </div>
              {error && <p className="mt-2 text-xs text-destructive">{error}</p>}
            </div>

            <button
              type="submit"
              disabled={!canSubmit}
              className="group inline-flex w-full items-center justify-center gap-2 rounded-xl bg-gradient-neon px-4 py-3 text-sm font-medium text-background shadow-[var(--shadow-glow)] transition-transform hover:scale-[1.02] disabled:opacity-60"
            >
              {loading ? <Loader2 className="h-4 w-4 animate-spin" /> : <ArrowRight className="h-4 w-4" />}
              {loading ? "Fetching profile..." : "Continue to Generator"}
            </button>
          </form>
        </motion.div>
      </section>
    </main>
  );
}
