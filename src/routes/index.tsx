import { createFileRoute } from "@tanstack/react-router";
import { Navbar } from "@/components/Navbar";
import { Hero } from "@/components/Hero";
import { FeatureGrid } from "@/components/FeatureGrid";
import { TemplateShowcase } from "@/components/TemplateShowcase";
import { FAQ } from "@/components/FAQ";
import { Footer } from "@/components/Footer";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "github-readme.app — Build a stunning GitHub profile README" },
      {
        name: "description",
        content: "Generate, preview, edit, and export a beautiful GitHub profile README in minutes.",
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
      <Footer />
    </main>
  );
}

function SocialProof() {
  const quotes = [
    { name: "Maya • @maya_dev", text: "Replaced an hour of fiddling with markdown with 60 seconds. Beautiful tool." },
    { name: "Jordan • Senior SWE", text: "Best looking README generator I've used. The animated template is unreal." },
    { name: "Riya • OSS Maintainer", text: "Finally a generator that doesn't feel like a 2014 form. Premium feel." },
  ];
  return (
    <section className="py-20">
      <div className="mx-auto max-w-7xl px-6">
        <div className="text-center text-xs uppercase tracking-[0.2em] text-muted-foreground">Loved by developers</div>
        <div className="mt-10 grid gap-4 md:grid-cols-3">
          {quotes.map((q) => (
            <div key={q.name} className="glass rounded-2xl p-6">
              <p className="text-sm leading-relaxed">"{q.text}"</p>
              <div className="mt-4 text-xs text-muted-foreground">{q.name}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
