"use client";
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Plus } from "lucide-react";

const faqs = [
  {
    q: "Is github-readme.app free?",
    a: "Yes. Building, previewing, and exporting your README is completely free. No account needed.",
  },
  {
    q: "Do you store my data?",
    a: "Drafts are saved to your browser's local storage only. We never send your form data to any server.",
  },
  {
    q: "How does GitHub auto-fill work?",
    a: "We call the public GitHub API with the username you enter to fetch your name, bio, avatar, and public profile fields. No authentication required.",
  },
  {
    q: "Can I edit the markdown directly?",
    a: "Absolutely. Toggle to the Markdown tab and edit freely. Your changes will be preserved when exporting.",
  },
  {
    q: "Will it work on mobile?",
    a: "The generator is desktop-first for the best experience, but the landing page and templates work great on any screen.",
  },
];

export function FAQ() {
  const [open, setOpen] = useState<number | null>(0);
  return (
    <section className="relative py-24" id="faq">
      <div className="mx-auto max-w-3xl px-6">
        <div className="text-center">
          <div className="text-xs uppercase tracking-[0.2em] text-muted-foreground">FAQ</div>
          <h2 className="mt-3 text-4xl font-bold tracking-tight md:text-5xl font-display">
            Questions, <span className="text-gradient">answered</span>
          </h2>
        </div>
        <div className="mt-12 space-y-3">
          {faqs.map((f, i) => {
            const isOpen = open === i;
            return (
              <div key={i} className="glass rounded-xl">
                <button
                  className="flex w-full items-center justify-between gap-4 p-5 text-left"
                  onClick={() => setOpen(isOpen ? null : i)}
                >
                  <span className="font-medium">{f.q}</span>
                  <Plus className={`h-4 w-4 transition-transform ${isOpen ? "rotate-45" : ""}`} />
                </button>
                <AnimatePresence initial={false}>
                  {isOpen && (
                    <motion.div
                      initial={{ height: 0, opacity: 0 }}
                      animate={{ height: "auto", opacity: 1 }}
                      exit={{ height: 0, opacity: 0 }}
                      className="overflow-hidden"
                    >
                      <div className="px-5 pb-5 text-sm text-muted-foreground leading-relaxed">{f.a}</div>
                    </motion.div>
                  )}
                </AnimatePresence>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
