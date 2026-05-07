import { Link, useRouterState } from "@tanstack/react-router";
import { GitBranch, Sparkles, Star } from "lucide-react";

export function Navbar() {
  const path = useRouterState({ select: (s) => s.location.pathname });
  const link = (to: string, label: string) => (
    <Link
      to={to}
      className={`relative text-sm font-medium transition-colors hover:text-foreground group py-1 ${
        path === to ? "text-foreground" : "text-muted-foreground"
      }`}
    >
      {label}
      <span className={`absolute -bottom-1 left-0 h-0.5 bg-gradient-neon transition-all duration-300 ${
        path === to ? "w-full" : "w-0 group-hover:w-full"
      }`}></span>
    </Link>
  );

  return (
    <header className="relative top-0 left-0 right-0 z-50 bg-transparent border-b border-transparent transition-all duration-300 hover:bg-black/40 hover:backdrop-blur-xl hover:border-white/5">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-6">
        <Link to="/" className="flex items-center gap-2 font-display">
          <span className="inline-flex h-8 w-8 items-center justify-center rounded-lg bg-gradient-neon shadow-[var(--shadow-glow)]">
            <Sparkles className="h-4 w-4 text-background" />
          </span>
          <span className="font-bold tracking-tight">
            github-readme<span className="text-gradient">.app</span>
          </span>
        </Link>
        <nav className="hidden items-center gap-7 md:flex">
          {link("/", "Home")}
          {link("/templates", "Templates")}
          <a href="/#faq" className="relative text-sm font-medium text-muted-foreground transition-colors hover:text-foreground group py-1">
            FAQ
            <span className="absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-neon transition-all duration-300 group-hover:w-full"></span>
          </a>
        </nav>
        <div className="flex items-center gap-3">
          <a
            href="https://github.com/dhairyagothi/git-creator"
            target="_blank"
            rel="noreferrer"
            className="inline-flex h-9 items-center gap-2 rounded-lg bg-gradient-neon px-4 text-sm font-medium text-background shadow-[var(--shadow-glow)] transition-transform hover:scale-[1.03]"
          >
            <Star className="h-4 w-4" fill="currentColor" />
            Star on GitHub
          </a>
        </div>
      </div>
    </header>
  );
}
