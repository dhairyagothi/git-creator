import { motion } from "framer-motion";
import { Link } from "@tanstack/react-router";
import { ArrowRight } from "lucide-react";
import { TEMPLATES } from "@/lib/templates";
import { incrementGenerateCount } from "@/lib/metrics";

export function TemplateShowcase() {
  const popular = TEMPLATES.filter((t) => t.tags.includes("popular"));
  const featured = (popular.length ? popular : TEMPLATES).slice(0, 4);
  return (
    <section className="relative py-24" id="templates">
      <div className="mx-auto max-w-7xl px-6">
        <div className="flex items-end justify-between gap-6">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <div className="text-xs uppercase tracking-[0.2em] text-muted-foreground">Templates</div>
            <h2 className="mt-3 text-4xl font-bold tracking-tight md:text-5xl font-display">
              Pick a starting point
            </h2>
          </motion.div>
          <Link
            to="/templates"
            className="hidden md:inline-flex items-center gap-2 text-sm text-muted-foreground hover:text-foreground transition-colors"
          >
            View all <ArrowRight className="h-4 w-4" />
          </Link>
        </div>

        <div className="mt-12 grid gap-6 md:grid-cols-2 lg:grid-cols-4">
          {featured.map((t, i) => (
            <motion.div
              key={t.id}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-50px" }}
              transition={{ delay: i * 0.06 }}
              whileHover={{ y: -6 }}
              className="glass group relative overflow-hidden rounded-2xl p-5"
            >
              <div className={`h-32 rounded-xl bg-gradient-to-br ${t.accent} relative overflow-hidden`}>
                <div className="absolute inset-0 grid-bg opacity-30" />
                <div className="absolute bottom-3 left-3 right-3">
                  <div className="h-2 w-2/3 rounded bg-white/40" />
                  <div className="mt-1.5 h-2 w-1/2 rounded bg-white/30" />
                </div>
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
              <Link
                to="/user-datails"
                search={{ template: t.id } as never}
                onClick={() => incrementGenerateCount()}
                className="mt-4 inline-flex items-center gap-1 text-sm text-foreground hover:text-[oklch(0.82_0.16_200)] transition-colors"
              >
                Use template <ArrowRight className="h-3.5 w-3.5" />
              </Link>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
