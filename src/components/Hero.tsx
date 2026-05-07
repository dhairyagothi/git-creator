import { motion } from "framer-motion";
import { Link } from "@tanstack/react-router";
import { ArrowRight, GitBranch, Sparkles, Wand2 } from "lucide-react";
import { incrementGenerateCount } from "@/lib/metrics";
import Aurora from "./Aurora";
import GradientText from "./GradientText";

export function Hero() {
  return (
    <section className="relative -mt-16 pt-36 pb-32 isolate">
      <div className="absolute inset-0 -z-10 overflow-hidden">
        <Aurora
          colorStops={["#7cff67", "#B497CF", "#5227FF"]}
          blend={0.5}
          amplitude={1.0}
          speed={1}
        />
      </div>
      <div className="mx-auto max-w-7xl px-6 relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7 }}
          className="mx-auto max-w-3xl text-center"
        >
          <div className="inline-flex items-center gap-2 rounded-full border border-border/60 bg-card/40 px-3 py-1 text-xs text-muted-foreground">
            <span className="h-1.5 w-1.5 rounded-full bg-gradient-neon" />
            100% Free README Generator
          </div>
          <h1 className="mt-6 text-5xl font-bold leading-[1.05] tracking-tight md:text-7xl font-display flex flex-col items-center">
            <span>
              Craft a <span className="text-gradient">stunning</span>
            </span>
            <div className="mt-2 text-center text-[clamp(2rem,6vw,4.5rem)] leading-tight">
              <GradientText
                colors={["#5227FF", "#FF9FFC", "#B497CF"]}
                animationSpeed={8}
                showBorder={false}
                className="text-center font-bold tracking-tight"
              >
                GitHub profile<br/>README
              </GradientText>
            </div>
          </h1>
          <p className="mt-6 text-lg text-muted-foreground md:text-lg max-w-2xl mx-auto">
            Build a professional profile in under 60 seconds for <b>FREE</b>. 
            Pick a premium template, auto-fill your stats, and export instantly.
          </p>

          <div className="mt-10 flex flex-col items-center justify-center gap-3 sm:flex-row">
            <Link
              to="/user-details"
              onClick={() => incrementGenerateCount()}
              className="group inline-flex h-12 items-center gap-2 rounded-xl bg-gradient-neon px-6 font-medium text-background shadow-[var(--shadow-glow)] transition-transform hover:scale-[1.03]"
            >
              <Wand2 className="h-4 w-4" />
              Profile README Generator
               <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />
            </Link>
            <Link
              to="/repo-readme"
              className="group inline-flex h-12 items-center gap-2 rounded-xl bg-gradient-neon px-6 font-medium text-background shadow-[var(--shadow-glow)] transition-transform hover:scale-[1.03]"
            >
              <GitBranch className="h-4 w-4" />
              Repo README Generator
               <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />
            </Link>
          </div>
          <div className="mt-4 flex items-center justify-center">
            <Link
              to="/templates"
              className="group inline-flex h-10 items-center gap-2 rounded-full border border-border/60 bg-card/40 px-5 text-sm font-medium text-foreground hover:bg-card/70 transition-colors"
            >
              Profile README Templates  
              <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />
            </Link>
          </div>


        </motion.div>

        <FloatingPreview />
        <RepoAiShowcase />
      </div>
    </section>
  );
}

function FloatingPreview() {
  return (
    <div className="relative mx-auto mt-10 max-w-5xl">
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, delay: 0.2 }}
        className="glass relative overflow-hidden rounded-2xl p-2 shadow-[var(--shadow-elegant)]"
      >
        <div className="flex items-center gap-1.5 px-3 py-2">
          <span className="h-2.5 w-2.5 rounded-full bg-rose-500/70" />
          <span className="h-2.5 w-2.5 rounded-full bg-amber-400/70" />
          <span className="h-2.5 w-2.5 rounded-full bg-emerald-400/70" />
          <span className="ml-3 font-mono text-xs text-muted-foreground">README.md</span>
        </div>
        <div className="grid gap-4 rounded-xl bg-background/60 p-8 md:grid-cols-2">
          <div>
            <div className="text-xs text-muted-foreground font-mono"># Hi, I'm Alex 👋</div>
            <div className="mt-3 h-3 w-3/4 rounded bg-foreground/20" />
            <div className="mt-2 h-3 w-2/3 rounded bg-foreground/10" />
            <div className="mt-6 flex flex-wrap gap-1.5">
              {["TypeScript", "React", "Node", "Rust", "Go"].map((t) => (
                <span key={t} className="rounded bg-gradient-neon px-2 py-0.5 text-[10px] font-mono text-background">
                  {t}
                </span>
              ))}
            </div>
            <div className="mt-6 grid grid-cols-2 gap-2">
              <div className="h-16 rounded-lg border border-border/40 bg-card/40 animate-shimmer" />
              <div className="h-16 rounded-lg border border-border/40 bg-card/40 animate-shimmer" />
            </div>
          </div>
          <div className="hidden md:block">
            <div className="h-full rounded-lg border border-border/40 bg-card/40 p-4 font-mono text-[11px] leading-relaxed text-muted-foreground">
              <div className="text-[oklch(0.78_0.18_200)]">## 📊 GitHub Stats</div>
              <div className="mt-2">⭐ 2,847 stars earned</div>
              <div>🔥 142 day streak</div>
              <div>🏆 12 trophies unlocked</div>
              <div className="mt-3 text-[oklch(0.72_0.28_340)]">## 🚀 Tech Stack</div>
              <div className="mt-1">React • Next.js • TypeScript</div>
              <div>Node.js • Postgres • Redis</div>
              <div>Docker • AWS • Tailwind</div>
            </div>
          </div>
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, x: -20, y: 30 }}
        animate={{ opacity: 1, x: 0, y: 0 }}
        transition={{ duration: 0.8, delay: 0.5 }}
        className="absolute -bottom-6 -left-6 hidden md:block glass rounded-xl p-4"
      >
        <div className="flex items-center gap-3">
          <div className="h-10 w-10 rounded-full bg-gradient-neon" />
          <div>
            <div className="text-xs text-muted-foreground">Auto-fetched</div>
            <div className="text-sm font-medium">@octocat</div>
          </div>
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, x: 20, y: 30 }}
        animate={{ opacity: 1, x: 0, y: 0 }}
        transition={{ duration: 0.8, delay: 0.6 }}
        className="absolute -top-6 -right-6 hidden md:block glass rounded-xl p-4"
      >
        <div className="font-mono text-xs text-muted-foreground">Exported</div>
        <div className="font-mono text-sm">README.md</div>
      </motion.div>
    </div>
  );
}

function RepoAiShowcase() {
  return (
    <div className="relative mx-auto mt-10 max-w-5xl">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, delay: 0.25 }}
        className="glass relative overflow-hidden rounded-3xl border border-border/60 p-8 shadow-[var(--shadow-elegant)]"
      >
        <div className="absolute inset-0 opacity-40">
          <div className="absolute -left-12 -top-12 h-40 w-40 rounded-full bg-[radial-gradient(circle,rgba(124,255,103,0.35),transparent_70%)] blur-2xl" />
          <div className="absolute -bottom-16 right-6 h-48 w-48 rounded-full bg-[radial-gradient(circle,rgba(82,39,255,0.35),transparent_70%)] blur-2xl" />
        </div>
        <div className="relative grid gap-6 md:grid-cols-[1.1fr_0.9fr]">
          <div>
            <div className="inline-flex items-center gap-2 rounded-full border border-border/60 bg-card/50 px-3 py-1 text-xs text-muted-foreground">
              <Sparkles className="h-3.5 w-3.5" />
              AI Repo README
            </div>
            <h3 className="mt-5 text-3xl font-bold tracking-tight md:text-4xl font-display">
              AI Repo README in seconds
            </h3>
            <p className="mt-3 text-sm text-muted-foreground md:text-base">
              Analyzing code, dependencies, and docs live.
            </p>
            <div className="mt-6 flex flex-wrap gap-2 text-xs text-muted-foreground">
              {["Languages", "Dependencies", "Features", "Install", "Usage", "Contributing"].map((chip) => (
                <span key={chip} className="rounded-full border border-border/60 bg-card/40 px-3 py-1">
                  {chip}
                </span>
              ))}
            </div>
          </div>
          <div className="relative">
            <div className="rounded-2xl border border-border/60 bg-background/50 p-4 font-mono text-xs text-muted-foreground">
              <div className="flex items-center justify-between text-[10px] uppercase tracking-[0.2em] text-muted-foreground">
                <span>Analysis stream</span>
                <span className="rounded-full bg-gradient-neon px-2 py-0.5 text-[9px] font-semibold text-background">
                  Live
                </span>
              </div>
              <div className="mt-4 space-y-3">
                {[
                  "Detected React + Vite project",
                  "Found 12 dependencies",
                  "Summarized core features",
                  "Drafting README outline",
                ].map((line) => (
                  <div key={line} className="flex items-center gap-2">
                    <span className="h-1.5 w-1.5 rounded-full bg-[oklch(0.78_0.18_200)]" />
                    <span>{line}</span>
                  </div>
                ))}
              </div>
              <div className="mt-5 h-2 overflow-hidden rounded-full bg-border/40">
                <div className="h-full w-4/5 animate-shimmer bg-gradient-neon" />
              </div>
            </div>
          </div>
        </div>
      </motion.div>
    </div>
  );
}
