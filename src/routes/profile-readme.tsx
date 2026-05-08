import { createFileRoute, useNavigate } from "@tanstack/react-router";
import { useState, useMemo } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { toast } from "sonner";
import { 
  FiGithub, 
  FiArrowRight, 
  FiChevronLeft, 
  FiLayout, 
  FiCheck, 
  FiUser, 
  FiCode, 
  FiBarChart2, 
  FiMail, 
  FiGlobe,
  FiAward,
  FiTerminal,
  FiMusic,
  FiCommand,
  FiBox,
  FiStar,
  FiUsers
} from "react-icons/fi";
import { 
  SiLeetcode, 
  SiSpotify, 
  SiGithub 
} from "react-icons/si";
import { Navbar } from "@/components/Navbar";
import { useAppStore } from "@/lib/store";
import { ALL_SECTIONS, DEFAULT_PROFILE_SECTIONS, type SectionId } from "@/lib/templates";
import { emptyForm } from "@/lib/types";
import { Loader2 } from "lucide-react";

const PREFILL_KEY = "gra_prefill_v1";

export const Route = createFileRoute("/profile-readme")({
  head: () => ({
    meta: [
      { title: "Profile README Onboarding — github-readme.tech" },
      { name: "description", content: "Set up your GitHub profile README with a few simple steps." },
    ],
  }),
  component: ProfileOnboardingPage,
});

const sectionIcons: Record<SectionId, React.ReactNode> = {
  header: <FiLayout />,
  typing: <FiTerminal />,
  socials: <FiMail />,
  techStack: <FiCode />,
  githubStats: <FiBarChart2 />,
  topLangs: <FiBarChart2 />,
  streak: <FiBarChart2 />,
  trophies: <FiAward />,
  activityGraph: <FiBarChart2 />,
  projects: <FiBox />,
  footer: <FiLayout />,
  about: <FiUser />,
  skills: <FiCode />,
  leetcode: <SiLeetcode />,
  spotify: <SiSpotify />,
  snake: <FiCommand />,
  quote: <FiLayout />,
  badges: <FiAward />,
};

function ProfileOnboardingPage() {
  const navigate = useNavigate();
  const { form: storeForm, updateForm, setSections, reset } = useAppStore();
  
  const [step, setStep] = useState<"username" | "sections" | "details">("username");
  const [username, setUsername] = useState(storeForm.username || "");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [fetchedData, setFetchedData] = useState<any>(null);
  
  const [selectedSections, setSelectedSections] = useState<SectionId[]>(DEFAULT_PROFILE_SECTIONS);
  const [form, setForm] = useState(emptyForm);

  const handleFetch = async (e: React.FormEvent) => {
    e.preventDefault();
    const normalizedUsername = username.trim().replace(/^@+/, "");
    if (!normalizedUsername) {
      setError("Please enter your GitHub username.");
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const res = await fetch(`https://api.github.com/users/${encodeURIComponent(normalizedUsername)}`);
      if (!res.ok) {
        if (res.status === 404) throw new Error("Profile not found");
        throw new Error("GitHub API error");
      }
      const data = await res.json();
      
      const reposRes = await fetch(`https://api.github.com/users/${encodeURIComponent(normalizedUsername)}/repos?per_page=100&sort=stars`);
      const repos = reposRes.ok ? await reposRes.json() : [];
      
      const nonForks = repos.filter((r: any) => !r.fork);
      const topProjects = nonForks
        .sort((a: any, b: any) => (b.stargazers_count ?? 0) - (a.stargazers_count ?? 0))
        .slice(0, 4)
        .map((r: any) => ({
          name: r.name,
          description: r.description || "",
          url: r.html_url
        }));

      let totalStars = 0;
      const langCounts: Record<string, number> = {};
      repos.forEach((repo: any) => {
        totalStars += repo.stargazers_count ?? 0;
        if (repo.language) {
          langCounts[repo.language] = (langCounts[repo.language] ?? 0) + 1;
        }
      });

      const topLanguages = Object.entries(langCounts)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 6)
        .map(([lang]) => lang);

      const nextForm = {
        ...emptyForm,
        username: normalizedUsername,
        displayName: data.name || normalizedUsername,
        bio: data.bio || "",
        avatarUrl: data.avatar_url || "",
        location: data.location || "",
        githubStats: {
          totalStars,
          publicRepos: data.public_repos || 0,
          followers: data.followers || 0,
          topLanguages,
        },
        projects: topProjects,
        socials: {
          ...emptyForm.socials,
          twitter: data.twitter_username || "",
          website: data.blog || "",
        }
      };

      setFetchedData(data);
      setForm(nextForm);
      setStep("sections");
      toast.success("Profile data fetched!");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  const toggleSection = (id: SectionId) => {
    setSelectedSections(prev => {
      const isEnabling = !prev.includes(id);
      let next = isEnabling ? [...prev, id] : prev.filter(s => s !== id);
      
      if (isEnabling && id === "about") {
        next = next.filter(s => s !== "about");
        next.splice(Math.min(3, next.length), 0, "about");
      }
      
      return next;
    });
  };

  const onGenerate = () => {
    updateForm(form);
    setSections(selectedSections);
    
    // Save to prefill key for GeneratorWorkspace to pick up
    localStorage.setItem(PREFILL_KEY, JSON.stringify({
      form: form,
      sections: selectedSections
    }));

    navigate({ to: "/generator" });
  };

  const ProfilePreview = () => (
    <motion.div
      initial={{ opacity: 0, x: -20 }}
      animate={{ opacity: 1, x: 0 }}
      className="glass mb-8 flex w-full max-w-xl items-center gap-4 rounded-2xl border border-border/50 p-4 shadow-xl"
    >
      <img src={form.avatarUrl} alt={form.username} className="h-16 w-16 rounded-xl border-2 border-primary/20 shadow-lg" />
      <div className="flex-1 min-w-0">
        <h3 className="font-bold text-foreground truncate">{form.displayName || form.username}</h3>
        <p className="text-sm text-muted-foreground truncate">@{form.username}</p>
        {form.bio && <p className="mt-1 text-xs text-muted-foreground line-clamp-1">{form.bio}</p>}
      </div>
      <div className="flex flex-col gap-1 items-end">
        <div className="flex items-center gap-1.5 text-[10px] font-medium text-muted-foreground">
          <FiStar className="h-3 w-3 text-amber-400" />
          {form.githubStats.totalStars}
        </div>
        <div className="flex items-center gap-1.5 text-[10px] font-medium text-muted-foreground">
          <FiUsers className="h-3 w-3 text-primary" />
          {form.githubStats.followers}
        </div>
      </div>
    </motion.div>
  );

  return (
    <main className="min-h-screen bg-background">
      <Navbar />

      <div className="relative mx-auto flex min-h-[calc(100vh-96px)] max-w-6xl flex-col items-center justify-center px-6 py-12">
        {/* Background blobs */}
        <div className="absolute inset-0 -z-10 overflow-hidden">
          <div className="absolute left-1/2 top-1/4 h-96 w-96 -translate-x-1/2 rounded-full bg-[radial-gradient(circle,rgba(120,255,103,0.15),transparent_70%)] blur-3xl" />
          <div className="absolute right-0 bottom-1/4 h-96 w-96 rounded-full bg-[radial-gradient(circle,rgba(82,39,255,0.15),transparent_70%)] blur-3xl" />
        </div>

        {step !== "username" && <ProfilePreview />}

        <AnimatePresence mode="wait">
          {step === "username" && (
            <motion.div
              key="username"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              className="glass w-full max-w-xl rounded-3xl border border-border/50 p-8 shadow-2xl"
            >
              <div className="flex items-center gap-4 mb-8">
                <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-card border border-border/60">
                  <FiGithub className="h-7 w-7" />
                </div>
                <div>
                  <h1 className="text-2xl font-bold">Find Your Profile</h1>
                  <p className="text-sm text-muted-foreground">Enter your GitHub Username to get started</p>
                </div>
              </div>

              <form onSubmit={handleFetch} className="space-y-6">
                <div>
                  <label className="block text-sm font-medium mb-2">GitHub Username</label>
                  <div className="relative">
                    <span className="absolute left-4 top-1/2 -translate-y-1/2 text-muted-foreground">@</span>
                    <input
                      autoFocus
                      value={username}
                      onChange={e => setUsername(e.target.value)}
                      placeholder="dhairyagothi"
                      className="w-full rounded-xl border border-border/60 bg-background/50 py-4 pl-10 pr-4 text-lg outline-none transition-all focus:border-primary focus:ring-2 focus:ring-primary/20"
                    />
                  </div>
                  {error && <p className="mt-2 text-sm text-destructive">{error}</p>}
                </div>

                <motion.button
                  whileHover={{ scale: 1.01 }}
                  whileTap={{ scale: 0.99 }}
                  type="submit"
                  disabled={!username.trim() || loading}
                  className="flex w-full items-center justify-center gap-2 rounded-xl bg-gradient-neon py-4 text-lg font-bold text-background transition-all disabled:opacity-50"
                >
                  {loading ? <Loader2 className="h-6 w-6 animate-spin" /> : <>Next <FiArrowRight /></>}
                </motion.button>
              </form>
            </motion.div>
          )}

          {step === "sections" && (
            <motion.div
              key="sections"
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.95 }}
              className="glass w-full max-w-4xl rounded-3xl border border-border/50 p-8 shadow-2xl"
            >
              <div className="flex items-center justify-between mb-8">
                <button 
                  onClick={() => setStep("username")}
                  className="flex items-center gap-2 text-sm text-muted-foreground hover:text-foreground transition-colors"
                >
                  <FiChevronLeft /> Back
                </button>
                <div className="text-center flex-1">
                  <h1 className="text-2xl font-bold">Pick your sections</h1>
                  <p className="text-sm text-muted-foreground">Select what you want to show in your README</p>
                </div>
                <div className="w-16" /> {/* Spacer */}
              </div>

              <div className="grid grid-cols-2 gap-4 sm:grid-cols-3 md:grid-cols-4">
                {ALL_SECTIONS.map((section) => (
                  <motion.button
                    key={section.id}
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                    onClick={() => toggleSection(section.id)}
                    className={`relative flex flex-col items-center justify-center rounded-2xl border p-6 transition-all ${
                      selectedSections.includes(section.id)
                        ? "border-primary bg-primary/10 text-foreground ring-2 ring-primary/20"
                        : "border-border/60 bg-card/40 text-muted-foreground hover:border-border hover:bg-card/60"
                    }`}
                  >
                    <div className="text-3xl mb-3">
                      {sectionIcons[section.id] || <FiLayout />}
                    </div>
                    <span className="text-sm font-semibold">{section.label}</span>
                    {selectedSections.includes(section.id) && (
                      <motion.div 
                        initial={{ scale: 0 }}
                        animate={{ scale: 1 }}
                        className="absolute right-3 top-3 rounded-full bg-primary p-1 text-[10px] text-background"
                      >
                        <FiCheck />
                      </motion.div>
                    )}
                  </motion.button>
                ))}
              </div>

              <motion.button
                whileHover={{ scale: 1.01 }}
                whileTap={{ scale: 0.99 }}
                onClick={() => setStep("details")}
                className="mt-10 flex w-full items-center justify-center gap-2 rounded-xl bg-gradient-neon py-4 text-lg font-bold text-background transition-all"
              >
                Next <FiArrowRight />
              </motion.button>
            </motion.div>
          )}

          {step === "details" && (
            <motion.div
              key="details"
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -20 }}
              className="glass w-full max-w-2xl rounded-3xl border border-border/50 p-8 shadow-2xl"
            >
              <div className="flex items-center justify-between mb-8">
                <button 
                  onClick={() => setStep("sections")}
                  className="flex items-center gap-2 text-sm text-muted-foreground hover:text-foreground transition-colors"
                >
                  <FiChevronLeft /> Back
                </button>
                <div className="text-center flex-1">
                  <h1 className="text-2xl font-bold">Personalize it</h1>
                  <p className="text-sm text-muted-foreground">Add some flair to your profile</p>
                </div>
                <div className="w-16" /> {/* Spacer */}
              </div>

              <div className="space-y-6 max-h-[60vh] overflow-y-auto pr-2 custom-scrollbar">
                <div className="grid gap-6">
                  <div>
                    <label className="block text-sm font-medium mb-2">Display Name</label>
                    <input
                      value={form.displayName}
                      onChange={e => setForm(f => ({ ...f, displayName: e.target.value }))}
                      className="w-full rounded-xl border border-border/60 bg-background/50 py-3 px-4 outline-none transition-all focus:border-primary"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium mb-2">Tagline</label>
                    <input
                      value={form.tagline}
                      onChange={e => setForm(f => ({ ...f, tagline: e.target.value }))}
                      placeholder="Building things on the internet"
                      className="w-full rounded-xl border border-border/60 bg-background/50 py-3 px-4 outline-none transition-all focus:border-primary"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium mb-2">Bio</label>
                    <textarea
                      value={form.bio}
                      onChange={e => setForm(f => ({ ...f, bio: e.target.value }))}
                      rows={3}
                      className="w-full rounded-xl border border-border/60 bg-background/50 py-3 px-4 outline-none transition-all focus:border-primary resize-none"
                    />
                  </div>
                  
                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <label className="block text-sm font-medium mb-2">Role</label>
                      <input
                        value={form.role}
                        onChange={e => setForm(f => ({ ...f, role: e.target.value }))}
                        placeholder="Full Stack Developer"
                        className="w-full rounded-xl border border-border/60 bg-background/50 py-3 px-4 outline-none transition-all focus:border-primary"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-medium mb-2">Company / School</label>
                      <input
                        value={form.company}
                        onChange={e => setForm(f => ({ ...f, company: e.target.value }))}
                        className="w-full rounded-xl border border-border/60 bg-background/50 py-3 px-4 outline-none transition-all focus:border-primary"
                      />
                    </div>
                  </div>

                  {selectedSections.includes("socials") && (
                    <div className="pt-4 border-t border-border/30">
                      <h3 className="text-sm font-bold uppercase tracking-wider text-muted-foreground mb-4">Social Links</h3>
                      <div className="grid grid-cols-2 gap-4">
                        <div className="relative">
                          <FiGlobe className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground" />
                          <input
                            value={form.socials.website}
                            onChange={e => setForm(f => ({ ...f, socials: { ...f.socials, website: e.target.value } }))}
                            placeholder="Website"
                            className="w-full rounded-xl border border-border/60 bg-background/50 py-2.5 pl-10 pr-4 text-sm outline-none transition-all focus:border-primary"
                          />
                        </div>
                        <div className="relative">
                          <FiGithub className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground" />
                          <input
                            disabled
                            value={form.username}
                            className="w-full rounded-xl border border-border/60 bg-muted/20 py-2.5 pl-10 pr-4 text-sm outline-none opacity-60"
                          />
                        </div>
                      </div>
                    </div>
                  )}
                </div>
              </div>

              <motion.button
                whileHover={{ scale: 1.01 }}
                whileTap={{ scale: 0.99 }}
                onClick={onGenerate}
                className="mt-10 flex w-full items-center justify-center gap-2 rounded-xl bg-gradient-neon py-4 text-lg font-bold text-background transition-all"
              >
                Generate README <FiArrowRight />
              </motion.button>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </main>
  );
}
