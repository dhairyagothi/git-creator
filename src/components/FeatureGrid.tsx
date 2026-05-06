import { motion } from "framer-motion";
import { Layers, Eye, GitBranch, Pencil, Download, Save } from "lucide-react";
import { TEMPLATES } from "@/lib/templates";

const templateCount = TEMPLATES.length;
const features = [
  { icon: Layers, title: `${templateCount} Premium Templates`, desc: "From minimal to animated — pick the one that matches your vibe." },
  { icon: Eye, title: "Live Preview", desc: "See your README rendered exactly as it will appear on GitHub." },
  { icon: GitBranch, title: "GitHub Auto-Fill", desc: "Enter your username and we'll pre-fill your name, bio, and avatar." },
  { icon: Pencil, title: "Markdown Editor", desc: "Edit the markdown directly with a clean, syntax-aware editor." },
  { icon: Download, title: "One-Click Export", desc: "Copy to clipboard or download as README.md instantly." },
  { icon: Save, title: "Autosave Drafts", desc: "Never lose your work — drafts save to your browser automatically." },
];

export function FeatureGrid() {
  return (
    <section className="relative py-10" id="features">
      <div className="mx-auto max-w-7xl px-6">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-100px" }}
          className="mx-auto max-w-2xl text-center"
        >
          <div className="text-xs uppercase tracking-[0.2em] text-muted-foreground">Why developers love it</div>
          <h2 className="mt-3 text-4xl font-bold tracking-tight md:text-5xl font-display">
            Everything you need.<br /><span className="text-gradient">Nothing you don't.</span>
          </h2>
        </motion.div>

        <div className="mt-16 grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {features.map((f, i) => (
            <motion.div
              key={f.title}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-50px" }}
              transition={{ delay: i * 0.05, duration: 0.5 }}
              whileHover={{ y: -6 }}
              className="glass group relative overflow-hidden rounded-2xl p-6"
            >
              <div className="absolute inset-0 -z-10 opacity-0 group-hover:opacity-100 transition-opacity bg-gradient-to-br from-[oklch(0.7_0.24_295)/0.08] via-transparent to-[oklch(0.78_0.2_200)/0.08]" />
              <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-gradient-neon shadow-[var(--shadow-glow)]">
                <f.icon className="h-5 w-5 text-background" />
              </div>
              <h3 className="mt-5 text-lg font-semibold">{f.title}</h3>
              <p className="mt-2 text-sm text-muted-foreground leading-relaxed">{f.desc}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
