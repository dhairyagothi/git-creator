import { Link } from "@tanstack/react-router";
import { Sparkles } from "lucide-react";

export function Footer() {
  return (
    <footer className="relative mt-10 border-t border-border/40">
      <div className="mx-auto grid max-w-7xl gap-10 px-6 py-14 md:grid-cols-4">
        <div>
          <Link to="/" className="flex items-center gap-2">
            <span className="inline-flex h-8 w-8 items-center justify-center rounded-lg bg-gradient-neon shadow-[var(--shadow-glow)]">
              <Sparkles className="h-4 w-4 text-background" />
            </span>
            <span className="font-bold tracking-tight">github-readme<span className="text-gradient">.tech</span></span>
          </Link>
          <p className="mt-3 text-sm text-muted-foreground max-w-xs">
            The fastest way to ship a beautiful GitHub profile README.
          </p>
        </div>
        <FooterCol title="Product" links={[
          { to: "/user-datails", label: "Generator" },
          { to: "/templates", label: "Templates" },
        ]} />
        <FooterCol title="Resources" links={[
          { to: "/#features", label: "Features" },
          { to: "/#faq", label: "FAQ" },
        ]} />
        <FooterCol title="Legal" links={[
          { to: "/", label: "Privacy" },
          { to: "/", label: "Terms" },
        ]} />
      </div>
      <div className="border-t border-border/40">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-5 text-xs text-muted-foreground">
          <div>© {new Date().getFullYear()} github-readme.tech</div>
          <div>Made by Dhairya with ❤️ Made in Bharat </div>
        </div>
      </div>
    </footer>
  );
}

function FooterCol({ title, links }: { title: string; links: { to: string; label: string }[] }) {
  return (
    <div>
      <div className="text-sm font-semibold">{title}</div>
      <ul className="mt-3 space-y-2">
        {links.map((l) => (
          <li key={l.label}>
            <a href={l.to} className="text-sm text-muted-foreground hover:text-foreground transition-colors">
              {l.label}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
}
