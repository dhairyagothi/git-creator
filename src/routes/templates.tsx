import { createFileRoute, Link } from "@tanstack/react-router";
import { useState } from "react";
import { motion } from "framer-motion";
import { Search } from "lucide-react";
import { Navbar } from "@/components/Navbar";
import { Footer } from "@/components/Footer";
import { TEMPLATES } from "@/lib/templates";
import { incrementGenerateCount } from "@/lib/metrics";

export const Route = createFileRoute("/templates")({
  head: () => ({
    meta: [
      { title: "Premium GitHub README Templates — github-readme.app" },
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

        <div className="mt-10 flex flex-col gap-3 md:flex-row md:items-center md:justify-between">
          <div className="relative max-w-sm flex-1">
            <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
            <input
              value={q}
              onChange={(e) => setQ(e.target.value)}
              placeholder="Search templates..."
              className="w-full rounded-lg border border-border/60 bg-background/40 px-3 py-2.5 pl-9 text-sm outline-none focus:border-[oklch(0.7_0.24_295)]"
            />
          </div>
          <div className="flex gap-1.5">
            {tags.map((t) => (
              <button
                key={t}
                onClick={() => setTag(t)}
                className={`rounded-full border px-3 py-1.5 text-xs capitalize transition-colors ${
                  tag === t
                    ? "border-transparent bg-gradient-neon text-background"
                    : "border-border/60 text-muted-foreground hover:text-foreground"
                }`}
              >
                {t}
              </button>
            ))}
          </div>
        </div>

        <div className="mt-10 grid gap-6 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
          {filtered.map((t, i) => (
            <motion.div
              key={t.id}
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.04 }}
              whileHover={{ y: -6 }}
              className="glass group relative overflow-hidden rounded-2xl p-5"
            >
              <div className={`h-32 rounded-xl bg-gradient-to-br ${t.accent} relative overflow-hidden`}>
                <div className="absolute inset-0 grid-bg opacity-30" />
              </div>
              <div className="mt-4 flex items-center gap-2">
                <h3 className="font-semibold">{t.name}</h3>
                {t.tags.includes("popular") && (
                  <span className="rounded-full bg-gradient-neon px-2 py-0.5 text-[10px] font-medium text-background">
                    popular
                  </span>
                )}
              </div>
              <p className="mt-1 text-sm text-muted-foreground line-clamp-2">{t.description}</p>
              <div className="mt-3 flex flex-wrap gap-1">
                {t.tags.map((tg) => (
                  <span key={tg} className="rounded-full border border-border/60 px-2 py-0.5 text-[10px] text-muted-foreground">
                    {tg}
                  </span>
                ))}
              </div>
              <Link
                to="/user-details"
                search={{ template: t.id }}
                onClick={() => incrementGenerateCount()}
                className="mt-5 inline-flex w-full items-center justify-center gap-1 rounded-lg bg-gradient-neon px-3 py-2 text-sm font-medium text-background transition-transform hover:scale-[1.02]"
              >
                Use template
              </Link>
            </motion.div>
          ))}
          {!filtered.length && (
            <div className="col-span-full py-20 text-center text-muted-foreground">
              No templates match your search.
            </div>
          )}
        </div>
      </section>
      <Footer />
    </main>
  );
}
