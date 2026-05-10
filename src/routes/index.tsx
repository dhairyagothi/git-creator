import { createFileRoute } from "@tanstack/react-router";
import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Navbar } from "@/components/Navbar";
import { Hero } from "@/components/Hero";
import { FeatureGrid } from "@/components/FeatureGrid";
import { TemplateShowcase } from "@/components/TemplateShowcase";
import { FAQ } from "@/components/FAQ";
import { Footer } from "@/components/Footer";
import { getGenerateCount } from "@/lib/metrics";
import { supabase } from "@/lib/supabase";
import { FiUsers, FiTrendingUp, FiActivity, FiStar } from "react-icons/fi";


export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "github-readme.tech — Best GitHub Profile README Generator" },
      {
        name: "description",
        content: "Create a stunning GitHub profile README in seconds for FREE. 100+ premium templates, auto-fill stats, and live editor. The ultimate builder for developers.",
      },
      { property: "og:title", content: "github-readme.tech — Best GitHub Profile README Generator" },
      { property: "og:description", content: "Create a stunning GitHub profile README in seconds for FREE. 100+ premium templates, auto-fill stats, and live editor." },
      { property: "og:url", content: "https://github-readme.tech" },
      { property: "og:image", content: "https://github-readme.tech/og-image.png" },
    ],
  }),
  component: Index,
});

function Index() {
  return (
    <main>
      <Navbar />
      <Hero />
      <FeatureGrid />
      <TemplateShowcase />
      <SocialProof />
      <FAQ />
      <ConnectWithMe />
      <ReviewCallout />
      <Footer />
    </main>
  );
}

function SocialProof() {
  const quotes = [
    { name: "Maya • @maya_dev", text: "Replaced an hour of fiddling with markdown with 60 seconds. Beautiful tool." },
    { name: "Jordan • Senior SWE", text: "Best looking README generator I've used. The animated template is unreal." },
    { name: "Riya • OSS Maintainer", text: "Finally a generator that doesn't feel like a 2014 form. Premium feel." },
    { name: "Akhil • @akhilcodes", text: "Simple inputs, gorgeous output. This is the README builder I wanted." },
    { name: "Noah • DevRel", text: "Instantly polished profile with zero fiddling. Love the flow." },
  ];
  const [active, setActive] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      setActive((prev) => (prev + 1) % quotes.length);
    }, 3500);
    return () => clearInterval(id);
  }, [quotes.length]);

  const current = quotes[active];

  return (
    <section className="py-5">
      <div className="mx-auto max-w-7xl px-6">
        <div className="text-center text-xs uppercase tracking-[0.2em] text-muted-foreground">Loved by developers</div>
        <div className="relative mt-10 overflow-hidden">
          <div className="absolute inset-0 -z-10 opacity-40">
            <div className="absolute left-8 top-6 h-24 w-24 rounded-full bg-[radial-gradient(circle,rgba(124,255,103,0.25),transparent_70%)] blur-2xl" />
            <div className="absolute right-10 bottom-4 h-28 w-28 rounded-full bg-[radial-gradient(circle,rgba(82,39,255,0.25),transparent_70%)] blur-2xl" />
          </div>
          <div className="mx-auto flex max-w-3xl flex-col items-center gap-4">
            <AnimatePresence mode="wait">
              <motion.div
                key={current.name}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -20 }}
                transition={{ duration: 0.4 }}
                className="glass w-full rounded-2xl p-6 text-center"
              >
                <p className="text-sm leading-relaxed">"{current.text}"</p>
                <div className="mt-4 text-xs text-muted-foreground">{current.name}</div>
              </motion.div>
            </AnimatePresence>
            <div className="flex items-center gap-2">
              {quotes.map((q, i) => (
                <button
                  key={q.name}
                  onClick={() => setActive(i)}
                  className={`h-2 w-2 rounded-full transition-all ${
                    i === active ? "bg-[oklch(0.78_0.18_200)] w-5" : "bg-border"
                  }`}
                  aria-label={`Show testimonial ${i + 1}`}
                />
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function ConnectWithMe() {
  const [stats, setStats] = useState({ profileCount: 0, repoCount: 0, recent: [] as any[] });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchStats() {
      try {
        // Fetch Profile count
        const { count: profileCount, error: pError } = await supabase
          .from('generations')
          .select('*', { count: 'exact', head: true })
          .eq('type', 'profile');

        // Fetch Repo count
        const { count: repoCount, error: rError } = await supabase
          .from('generations')
          .select('*', { count: 'exact', head: true })
          .eq('type', 'repo');

        // Fetch recent 3 generations
        const { data: recent, error: recentError } = await supabase
          .from('generations')
          .select('username, type, created_at')
          .order('created_at', { ascending: false })
          .limit(3);

        if (!pError && !rError && !recentError) {
          setStats({ 
            profileCount: profileCount || 0,
            repoCount: repoCount || 0,
            recent: recent || [] 
          });
        }
      } catch (err) {
        console.error("Failed to fetch stats:", err);
      } finally {
        setLoading(false);
      }
    }
    fetchStats();
  }, []);

  return (
    <section className="py-20 relative overflow-hidden">
      <div className="absolute inset-0 -z-10">
        <div className="absolute left-1/2 top-0 h-[500px] w-[500px] -translate-x-1/2 rounded-full bg-[radial-gradient(circle,rgba(124,255,103,0.05),transparent_70%)] blur-3xl" />
      </div>

      <div className="mx-auto max-w-7xl px-6">
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          
          {/* Stats Card */}
          <div className="glass group rounded-3xl p-8 border border-border/40 hover:border-[oklch(0.78_0.18_200)]/40 transition-colors">
            <div className="flex h-full flex-col justify-between">
              <div>
                <div className="flex items-center gap-2 text-xs uppercase tracking-[0.2em] text-muted-foreground">
                  <FiTrendingUp className="text-[oklch(0.78_0.18_200)]" /> Usage Analytics
                </div>
                
                <div className="mt-8 space-y-6">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      <div className="h-10 w-10 rounded-xl bg-primary/10 flex items-center justify-center text-primary border border-primary/20">
                        👤
                      </div>
                      <div className="text-sm font-semibold">Profiles</div>
                    </div>
                    <div className="text-2xl font-bold font-display">
                      {loading ? "..." : stats.profileCount.toLocaleString()}
                    </div>
                  </div>

                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      <div className="h-10 w-10 rounded-xl bg-blue-500/10 flex items-center justify-center text-blue-500 border border-blue-500/20">
                        📦
                      </div>
                      <div className="text-sm font-semibold">Repositories</div>
                    </div>
                    <div className="text-2xl font-bold font-display">
                      {loading ? "..." : stats.repoCount.toLocaleString()}
                    </div>
                  </div>
                </div>

                <div className="mt-8 pt-6 border-t border-border/40">
                  <div className="flex items-center justify-between text-xs text-muted-foreground uppercase tracking-widest font-semibold">
                    <span>Total Generated</span>
                    <span className="text-foreground">{loading ? "..." : (stats.profileCount + stats.repoCount).toLocaleString()}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Recent Activity Card */}
          <div className="glass rounded-3xl p-8 border border-border/40">
            <div className="text-xs uppercase tracking-[0.2em] text-muted-foreground flex items-center gap-2">
              <FiActivity className="text-blue-400" /> Live Activity
            </div>
            <div className="mt-6 space-y-4">
              {loading ? (
                [1,2,3].map(i => <div key={i} className="h-12 w-full animate-pulse rounded-xl bg-card/40" />)
              ) : stats.recent.length > 0 ? (
                stats.recent.map((gen, i) => (
                  <div key={i} className="flex items-center gap-3 p-3 rounded-xl bg-card/30 border border-white/5">
                    <div className="h-8 w-8 rounded-lg bg-gradient-to-br from-white/10 to-transparent flex items-center justify-center text-lg">
                      {gen.type === 'profile' ? '👤' : '📦'}
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="text-xs font-semibold text-foreground truncate">
                        {gen.username}
                      </div>
                      <div className="text-[10px] text-muted-foreground uppercase tracking-wider">
                        {gen.type === 'profile' ? 'Profile README' : 'Repo README'}
                      </div>
                    </div>
                  </div>
                ))
              ) : (
                <p className="text-xs text-muted-foreground italic text-center py-8">No recent activity yet. Be the first!</p>
              )}
            </div>
            <p className="mt-6 text-[10px] text-center text-muted-foreground uppercase tracking-widest opacity-60">
              Real-time updates via Supabase
            </p>
          </div>

          {/* Social Connect Card */}
          <div className="glass rounded-3xl p-8 border border-border/40 md:col-span-2 lg:col-span-1">
            <div className="text-xs uppercase tracking-[0.2em] text-muted-foreground">Creator</div>
            <h2 className="mt-4 text-3xl font-bold tracking-tight font-display">
              Let’s build <span className="text-[oklch(0.78_0.18_200)]">together</span>
            </h2>
            <p className="mt-4 text-sm text-muted-foreground leading-relaxed">
              Found this helpful? Follow the journey on social media or reach out for collaborations.
            </p>
            <div className="mt-8 grid grid-cols-2 gap-3">
              <a
                href="https://github.com/dhairyagothi"
                target="_blank"
                rel="noreferrer"
                className="flex items-center justify-center gap-2 rounded-xl border border-border/60 bg-card/40 py-3 text-xs font-bold hover:bg-card/70 transition-all"
              >
                GitHub
              </a>
              <a
                href="https://www.linkedin.com/in/dhairya-gothi/"
                target="_blank"
                rel="noreferrer"
                className="flex items-center justify-center gap-2 rounded-xl border border-border/60 bg-card/40 py-3 text-xs font-bold hover:bg-card/70 transition-all"
              >
                LinkedIn
              </a>
              <a
                href="https://www.dhairyagothiportfolio.live/"
                target="_blank"
                rel="noreferrer"
                className="col-span-2 flex items-center justify-center gap-2 rounded-xl border border-border/60 bg-card/40 py-3 text-xs font-bold hover:bg-card/70 transition-all"
              >
                View Portfolio
              </a>
            </div>
          </div>

        </div>
      </div>
    </section>
  );
}

function ReviewCallout() {
  return (
    <section className="pb-20">
      <div className="mx-auto max-w-7xl px-6">
        <div className="glass rounded-3xl p-8 border border-border/40 relative overflow-hidden group hover:border-[oklch(0.78_0.18_200)]/40 transition-colors">
          <div className="absolute inset-0 -z-10 bg-[radial-gradient(circle_at_top_right,rgba(124,255,103,0.05),transparent_40%)]" />
          <div className="flex flex-col md:flex-row items-center justify-between gap-8">
            <div className="flex items-center gap-6 text-center md:text-left">
              <div className="h-16 w-16 rounded-2xl bg-[oklch(0.78_0.18_200)]/10 flex items-center justify-center text-3xl shadow-inner border border-[oklch(0.78_0.18_200)]/20">
                <FiStar className="text-[oklch(0.78_0.18_200)] animate-pulse" />
              </div>
              <div className="space-y-1">
                <h3 className="text-2xl font-bold font-display tracking-tight">If you love it, leave a review!</h3>
                <p className="text-muted-foreground text-sm max-w-md">
                  Your feedback fuels our open-source journey. Share your experience and help us make README generation even better.
                </p>
              </div>
            </div>
            <a
              href="https://github.com/dhairyagothi/git-creator/issues/1"
              target="_blank"
              rel="noreferrer"
              className="group relative inline-flex items-center justify-center gap-2 rounded-2xl bg-[oklch(0.78_0.18_200)] px-8 py-4 text-sm font-bold text-black hover:scale-[1.02] active:scale-[0.98] transition-all shadow-[0_0_30px_rgba(124,255,103,0.2)] hover:shadow-[0_0_40px_rgba(124,255,103,0.4)]"
            >
              Write a Review
              <span className="text-lg">✨</span>
            </a>
          </div>
        </div>
      </div>
    </section>
  );
}

