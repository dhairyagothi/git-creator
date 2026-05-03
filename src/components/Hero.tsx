import { motion } from "framer-motion";
import { Link } from "@tanstack/react-router";
import { ArrowRight, Wand2 } from "lucide-react";
import { UserCounter } from "./UserCounter";

export function Hero() {
  return (
    <section className="relative pt-20 pb-32">
      <div className="mx-auto max-w-7xl px-6">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7 }}
          className="mx-auto max-w-3xl text-center"
        >
          <div className="inline-flex items-center gap-2 rounded-full border border-border/60 bg-card/40 px-3 py-1 text-xs text-muted-foreground">
            <span className="h-1.5 w-1.5 rounded-full bg-gradient-neon" />
            New: Animated profile templates
          </div>
          <h1 className="mt-6 text-5xl font-bold leading-[1.05] tracking-tight md:text-7xl font-display">
            Craft a{" "}
            <span className="text-gradient">stunning</span>
            <br />
            GitHub profile README
          </h1>
          <p className="mt-6 text-lg text-muted-foreground md:text-xl">
            Pick a template, fill in a few fields, and export a polished{" "}
            <span className="font-mono text-foreground">README.md</span> in under 60 seconds.
          </p>

          <div className="mt-10 flex flex-col items-center justify-center gap-3 sm:flex-row">
            <Link
              to="/generator"
              className="group inline-flex h-12 items-center gap-2 rounded-xl bg-gradient-neon px-6 font-medium text-background shadow-[var(--shadow-glow)] transition-transform hover:scale-[1.03]"
            >
              <Wand2 className="h-4 w-4" />
              Start Generating
              <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />
            </Link>
            <Link
              to="/templates"
              className="inline-flex h-12 items-center gap-2 rounded-xl border border-border/60 bg-card/40 px-6 font-medium text-foreground hover:bg-card/70 transition-colors"
            >
              View Templates
            </Link>
          </div>

          <div className="mt-12 flex justify-center">
            <UserCounter />
          </div>
        </motion.div>

        <FloatingPreview />
      </div>
    </section>
  );
}

function FloatingPreview() {
  return (
    <div className="relative mx-auto mt-20 max-w-5xl">
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
