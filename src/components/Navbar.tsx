import { Link, useRouterState } from "@tanstack/react-router";
import { Github, Sparkles } from "lucide-react";
import { UserCounter } from "./UserCounter";

export function Navbar() {
  const path = useRouterState({ select: (s) => s.location.pathname });
  const link = (to: string, label: string) => (
    <Link
      to={to}
      className={`text-sm transition-colors hover:text-foreground ${
        path === to ? "text-foreground" : "text-muted-foreground"
      }`}
    >
      {label}
    </Link>
  );

  return (
    <header className="sticky top-0 z-40 border-b border-border/50 backdrop-blur-xl bg-background/60">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-6">
        <Link to="/" className="flex items-center gap-2 font-display">
          <span className="inline-flex h-8 w-8 items-center justify-center rounded-lg bg-gradient-neon shadow-[var(--shadow-glow)]">
            <Sparkles className="h-4 w-4 text-background" />
          </span>
          <span className="font-bold tracking-tight">github-readme<span className="text-gradient">.app</span></span>
        </Link>
        <nav className="hidden items-center gap-7 md:flex">
          {link("/", "Home")}
          {link("/templates", "Templates")}
          {link("/generator", "Generator")}
          <a href="/#faq" className="text-sm text-muted-foreground hover:text-foreground transition-colors">FAQ</a>
        </nav>
        <div className="flex items-center gap-3">
          <UserCounter compact />
          <a
            href="https://github.com"
            target="_blank"
            rel="noreferrer"
            className="hidden md:inline-flex h-9 w-9 items-center justify-center rounded-lg border border-border/60 hover:bg-accent/10 transition-colors"
            aria-label="GitHub"
          >
            <Github className="h-4 w-4" />
          </a>
          <Link
            to="/generator"
            className="inline-flex h-9 items-center rounded-lg bg-gradient-neon px-4 text-sm font-medium text-background shadow-[var(--shadow-glow)] transition-transform hover:scale-[1.03]"
          >
            Start Generating
          </Link>
        </div>
      </div>
    </header>
  );
}
