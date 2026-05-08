import { useState } from "react";
import { Info, X, ExternalLink, Copy, Download } from "lucide-react";
import { FiGithub } from "react-icons/fi";
import { motion, AnimatePresence } from "framer-motion";

export function InfoButton() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="relative">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className={`inline-flex h-8 w-8 items-center justify-center rounded-lg border transition-all ${
          isOpen 
            ? "border-[oklch(0.7_0.24_295)] bg-[oklch(0.7_0.24_295)] text-background shadow-[var(--shadow-glow)]" 
            : "border-border/60 bg-card/40 text-muted-foreground hover:bg-card hover:text-foreground"
        }`}
        title="Help & Info"
      >
        {isOpen ? <X className="h-4 w-4" /> : <Info className="h-4 w-4" />}
      </button>

      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, scale: 0.95, y: 10 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: 10 }}
            className="absolute right-0 top-10 z-50 w-72 overflow-hidden rounded-2xl border border-border/50 bg-background/95 p-5 shadow-2xl backdrop-blur-xl"
          >
              <div className="space-y-4">
                <div className="flex items-center gap-2 font-semibold text-foreground">
                  <Info className="h-4 w-4 text-[oklch(0.78_0.18_295)]" />
                  <span>Help & Next Steps</span>
                </div>

                <div className="space-y-3 text-sm">
                  <div className="flex gap-3">
                    <div className="mt-1 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-orange-500/10 text-orange-500">
                      <ExternalLink className="h-3 w-3" />
                    </div>
                    <p className="text-muted-foreground leading-snug">
                      Preview contains <span className="text-foreground font-medium">dynamic images</span> and icons. They may take a moment to load from external servers.
                    </p>
                  </div>

                  <div className="flex gap-3">
                    <div className="mt-1 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-blue-500/10 text-blue-500">
                      <Copy className="h-3 w-3" />
                    </div>
                    <p className="text-muted-foreground leading-snug">
                      You can directly <span className="text-foreground font-medium">copy markdown</span> text or <span className="text-foreground font-medium">download .md</span> files using the toolbar buttons.
                    </p>
                  </div>

                  <div className="flex gap-3">
                    <div className="mt-1 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-green-500/10 text-green-500">
                      <FiGithub className="h-3 w-3" />
                    </div>
                    <p className="text-muted-foreground leading-snug">
                      <span className="text-foreground font-medium">Next steps:</span> Go to GitHub, create a new file (README.md), and paste the content!
                    </p>
                  </div>
                </div>

                <button
                  onClick={() => setIsOpen(false)}
                  className="w-full rounded-xl bg-muted/50 py-2 text-xs font-medium transition-colors hover:bg-muted"
                >
                  Got it!
                </button>
              </div>
              
              {/* Arrow */}
            </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
