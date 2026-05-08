import { createFileRoute, Link } from "@tanstack/react-router";
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Search, Star, X } from "lucide-react";
import { Navbar } from "@/components/Navbar";
import { Footer } from "@/components/Footer";
import { TEMPLATES } from "@/lib/templates";
import { incrementGenerateCount } from "@/lib/metrics";

export const Route = createFileRoute("/templates")({
  head: () => ({
    meta: [
      { title: "Premium GitHub README Templates — github-readme.tech" },
      { name: "description", content: "Explore premium GitHub profile README templates for FREE. Minimal, animated, data-driven, and persona-specific designs to make your profile stand out." },
    ],
  }),
  component: TemplatesPage,
});

const tags = [
  "all",
  "popular",
  "minimal",
  "animated",
  "fullstack",
  "student",
  "opensource",
  "data-ai",
  "web3",
  "professional",
  "space",
  "cyberpunk",
  "pastel",
  "ocean",
  "sunset",
  "forest",
  "fire",
  "retro",
  "aurora",
  "matrix",
];

function TemplatesPage() {
  const [q, setQ] = useState("");
  const [tag, setTag] = useState<string>("all");

  const filtered = TEMPLATES.filter((t) => {
    const matchesQ =
      !q ||
      t.name.toLowerCase().includes(q.toLowerCase()) ||
      t.description.toLowerCase().includes(q.toLowerCase());
    const matchesTag = tag === "all" || t.tags.includes(tag);
    return matchesQ && matchesTag;
  });

  return (
    <main>
      <Navbar />
      <section className="mx-auto max-w-7xl px-6 py-16">
        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
          <div className="text-xs uppercase tracking-[0.2em] text-muted-foreground">Templates</div>
          <h1 className="mt-3 text-5xl font-bold tracking-tight md:text-6xl font-display">
            Pick your <span className="text-gradient">style</span>
          </h1>
          <p className="mt-4 max-w-2xl text-muted-foreground">
            {TEMPLATES.length} starting points crafted for different developer personas. All fully customizable.
          </p>
        </motion.div>

        <div className="mt-12 space-y-8">
          <div className="flex flex-col gap-6 md:flex-row md:items-end md:justify-between">
            <div className="relative max-w-md flex-1">
              <Search className="absolute left-4 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground/60" />
              <input
                value={q}
                onChange={(e) => setQ(e.target.value)}
                placeholder="Search by name, role or tech..."
                className="w-full rounded-2xl border border-border/40 bg-card/30 backdrop-blur-sm px-4 py-3 pl-11 text-sm outline-none transition-all focus:border-[oklch(0.7_0.24_295)] focus:ring-4 focus:ring-[oklch(0.7_0.24_295)]/10"
              />
            </div>
            
            <div className="flex items-center gap-2 text-sm text-muted-foreground">
              <span className="font-medium text-foreground">{filtered.length}</span>
              <span>matching templates</span>
            </div>
          </div>

          <div className="flex flex-wrap gap-2 pt-2">
            {tags.map((t) => {
              const count = t === "all" 
                ? TEMPLATES.length 
                : TEMPLATES.filter(temp => temp.tags.includes(t)).length;
              
              if (count === 0 && t !== "all") return null;

              return (
                <button
                  key={t}
                  onClick={() => setTag(t)}
                  className={`group relative flex items-center gap-2 rounded-xl border px-4 py-2 text-xs font-medium transition-all ${
                    tag === t
                      ? "border-[oklch(0.7_0.24_295)] bg-[oklch(0.7_0.24_295)]/10 text-[oklch(0.78_0.18_295)] shadow-[0_0_20px_-5px_oklch(0.7_0.24_295)]"
                      : "border-border/40 bg-card/20 text-muted-foreground hover:border-border/80 hover:text-foreground"
                  }`}
                >
                  <span className="capitalize">{t.replace("-", " ")}</span>
                  <span className={`flex h-4 min-w-[1rem] items-center justify-center rounded-full px-1 text-[9px] font-bold ${
                    tag === t ? "bg-[oklch(0.7_0.24_295)] text-background" : "bg-muted text-muted-foreground group-hover:bg-border"
                  }`}>
                    {count}
                  </span>
                </button>
              );
            })}
          </div>
        </div>

        <div className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
          <AnimatePresence mode="popLayout">
            {filtered.map((t, i) => (
              <motion.div
                key={t.id}
                layout
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0, scale: 0.9 }}
                transition={{ duration: 0.2, delay: i * 0.02 }}
                className="group relative"
              >
                <div className="glass relative h-full overflow-hidden rounded-3xl border border-border/50 bg-card/20 p-5 transition-all hover:border-[oklch(0.7_0.24_295)]/50 hover:bg-card/40 hover:shadow-[0_20px_40px_-15px_rgba(0,0,0,0.3)]">
                  {/* Preview Area */}
                  <div className={`relative h-40 overflow-hidden rounded-2xl bg-gradient-to-br ${t.accent}`}>
                    <div className="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')] opacity-20" />
                    {t.tags.includes("popular") && (
                      <div className="absolute left-3 top-3 flex items-center gap-1 rounded-full bg-background/80 px-2.5 py-1 text-[10px] font-bold text-foreground backdrop-blur-md">
                        <Star className="h-3 w-3 fill-yellow-400 text-yellow-400" />
                        Popular
                      </div>
                    )}
                  </div>

                  {/* Info Area */}
                  <div className="mt-5">
                    <div className="flex items-start justify-between">
                      <h3 className="font-bold text-lg tracking-tight">{t.name}</h3>
                    </div>
                    <p className="mt-2 text-sm text-muted-foreground line-clamp-2 leading-relaxed">
                      {t.description}
                    </p>
                    
                    <div className="mt-4 flex flex-wrap gap-1.5">
                      {t.tags.filter(tag => tag !== "popular").map((tg) => (
                        <span key={tg} className="rounded-lg border border-border/40 bg-background/40 px-2 py-0.5 text-[10px] font-medium text-muted-foreground capitalize">
                          {tg.replace("-", " ")}
                        </span>
                      ))}
                    </div>
                  </div>

                  <Link
                    to="/profile-readme"
                    search={{ template: t.id }}
                    onClick={() => incrementGenerateCount()}
                    className="mt-6 flex w-full items-center justify-center gap-2 rounded-xl bg-foreground px-4 py-3 text-sm font-bold text-background transition-all hover:bg-foreground/90 active:scale-95"
                  >
                    Use this template
                  </Link>
                </div>
              </motion.div>
            ))}
          </AnimatePresence>

          {!filtered.length && (
            <motion.div 
              initial={{ opacity: 0 }} 
              animate={{ opacity: 1 }}
              className="col-span-full py-24 text-center"
            >
              <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-2xl border border-border/50 bg-card/20">
                <Search className="h-8 w-8 text-muted-foreground/40" />
              </div>
              <h3 className="mt-4 text-xl font-semibold">No templates found</h3>
              <p className="mt-2 text-muted-foreground">Try adjusting your search or filters to find what you're looking for.</p>
              <button 
                onClick={() => { setQ(""); setTag("all"); }}
                className="mt-6 text-sm font-bold text-[oklch(0.7_0.24_295)] hover:underline"
              >
                Clear all filters
              </button>
            </motion.div>
          )}
        </div>
      </section>
      <Footer />
    </main>
  );
}
