import { useState } from "react";
import { motion } from "framer-motion";
import { Check } from "lucide-react";
import { TEMPLATES, type TemplateId } from "@/lib/templates";

const categories = [
  "all", "minimal", "animated", "fullstack", "student", "opensource", "data-ai", "web3", "professional", 
  "space", "cyberpunk", "pastel", "ocean", "sunset", "forest", "fire", "retro", "aurora", "matrix"
];

export function TemplatePicker({
  value,
  onChange,
  compact = false,
}: {
  value: TemplateId;
  onChange: (id: TemplateId) => void;
  compact?: boolean;
}) {
  const [cat, setCat] = useState("all");
  const visible = TEMPLATES.filter(t => cat === "all" || t.tags.includes(cat));

  return (
    <div className="space-y-4">
      <div className="flex items-center gap-2 overflow-x-auto pb-2 [-ms-overflow-style:none] [scrollbar-width:none] [&::-webkit-scrollbar]:hidden">
        {categories.map((c) => (
          <button
            key={c}
            onClick={() => setCat(c)}
            className={`shrink-0 rounded-full px-3 py-1 text-xs font-medium capitalize transition-colors border ${
              cat === c
                ? "bg-[oklch(0.7_0.24_295)]/20 text-[oklch(0.78_0.18_295)] border-[oklch(0.7_0.24_295)]/30"
                : "bg-card/40 text-muted-foreground border-border/40 hover:bg-card hover:text-foreground"
            }`}
          >
            {c}
          </button>
        ))}
      </div>
      <div className={compact ? "space-y-2" : "grid gap-4 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4"}>
        {visible.map((t) => {
        const active = value === t.id;
        return (
          <motion.button
            key={t.id}
            whileHover={{ y: -3 }}
            onClick={() => onChange(t.id)}
            className={`group relative overflow-hidden rounded-xl text-left transition-all ${
              active
                ? "ring-2 ring-[oklch(0.7_0.24_295)] glow-ring"
                : "ring-1 ring-border/50 hover:ring-border"
            } glass ${compact ? "p-3" : "p-4"}`}
          >
            {!compact && (
              <div className={`h-24 rounded-lg bg-gradient-to-br ${t.accent} relative overflow-hidden mb-3`}>
                <div className="absolute inset-0 grid-bg opacity-30" />
              </div>
            )}
            <div className="flex items-start justify-between gap-2">
              <div className="min-w-0 flex-1">
                <div className="flex items-center gap-2">
                  <h4 className={`font-medium truncate ${compact ? "text-sm" : ""}`}>{t.name}</h4>
                  {active && (
                    <span className="inline-flex h-4 w-4 shrink-0 items-center justify-center rounded-full bg-gradient-neon">
                      <Check className="h-2.5 w-2.5 text-background" />
                    </span>
                  )}
                </div>
                {!compact && (
                  <p className="mt-1 text-xs text-muted-foreground line-clamp-2">{t.description}</p>
                )}
                <div className="mt-2 flex flex-wrap gap-1">
                  {t.tags.map((tag) => (
                    <span
                      key={tag}
                      className="rounded-full border border-border/60 bg-card/40 px-1.5 py-0.5 text-[10px] text-muted-foreground"
                    >
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          </motion.button>
        );
      })}
      </div>
    </div>
  );
}
