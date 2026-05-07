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


export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "Best GitHub Profile README Generator — github-readme.app" },
      {
        name: "description",
        content: "Build a stunning GitHub profile README in seconds for FREE. Pick from 100+ premium templates, auto-fill your stats, and stand out from the crowd.",
      },
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
  const [count, setCount] = useState(0);

  useEffect(() => {
    setCount(getGenerateCount());
  }, []);

  return (
    <section className="py-5">
      <div className="mx-auto max-w-7xl px-6">
        <div className="flex flex-col gap-6">
          
          <div className="glass flex-1 rounded-3xl p-8">
            <div className="flex h-full flex-col justify-between gap-6">
              <div>
                <div className="text-xs uppercase tracking-[0.2em] text-muted-foreground">No of READMEs Generated</div>
                <div className="mt-2 text-4xl font-bold text-gradient">
                  {count.toLocaleString()}
                </div>
                <p className="mt-2 text-xs text-muted-foreground">if you loved it, leave a review! 💖</p>
              </div>
              <div className="space-y-2">
                <a
                  href="https://github.com/dhairyagothi/git-creator/issues/1"
                  target="_blank"
                  rel="noreferrer"
                  className="inline-flex items-center justify-center rounded-xl bg-gradient-neon px-4 py-2 text-sm font-medium text-background shadow-[var(--shadow-glow)] transition-transform hover:scale-[1.02]"
                >
                  Give Review
                </a>
              </div>
            </div>
          </div>
          <div className="glass flex-1 rounded-3xl p-8">
            <div className="text-xs uppercase tracking-[0.2em] text-muted-foreground">Connect with me</div>
            <h2 className="mt-3 text-3xl font-bold tracking-tight md:text-4xl font-display">
              Let’s build together
            </h2>
            <p className="mt-3 text-sm text-muted-foreground">
              Found this helpful? Follow the journey, share feedback, and help make it better.
            </p>
            <div className="mt-5 flex flex-wrap gap-3">
              <a
                href="https://github.com/dhairyagothi"
                target="_blank"
                rel="noreferrer"
                className="inline-flex items-center justify-center rounded-lg border border-border/60 bg-card/40 px-4 py-2 text-sm font-medium hover:bg-card/70 transition-colors"
              >
                GitHub
              </a>
              <a
                href="https://www.linkedin.com/in/dhairya-gothi/"
                target="_blank"
                rel="noreferrer"
                className="inline-flex items-center justify-center rounded-lg border border-border/60 bg-card/40 px-4 py-2 text-sm font-medium hover:bg-card/70 transition-colors"
              >
                LinkedIn
              </a>
              <a
                href="https://www.dhairyagothiportfolio.live/"
                target="_blank"
                rel="noreferrer"
                className="inline-flex items-center justify-center rounded-lg border border-border/60 bg-card/40 px-4 py-2 text-sm font-medium hover:bg-card/70 transition-colors"
              >
                Portfolio
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
