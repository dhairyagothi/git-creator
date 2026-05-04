# git-creator

A fast, dark-themed web app for generating beautiful GitHub profile READMEs — with live preview, 8 templates, GitHub auto-fill, and one-click export.

![TanStack Start](https://img.shields.io/badge/TanStack_Start-v1-f97316?style=flat-square)
![React](https://img.shields.io/badge/React-19-61dafb?style=flat-square&logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5-3178c6?style=flat-square&logo=typescript)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4-38bdf8?style=flat-square&logo=tailwindcss)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

## Features

- **8 Templates** — Minimal, Animated, Full-Stack, Student, Open Source, Data/AI, Web3, Portfolio
- **GitHub Auto-Fill** — Fetch your name, bio, location, and avatar directly from the GitHub API
- **Live Markdown Preview** — See your README rendered in real time as you type
- **Editable Markdown** — Switch to raw mode to tweak anything by hand
- **One-Click Export** — Download `README.md` instantly
- **Autosave** — Draft saved to `localStorage` so you never lose your work
- **Section Toggles** — Show or hide individual README sections with a click

## Tech Stack

| Layer | Library |
|---|---|
| Framework | [TanStack Start](https://tanstack.com/start) |
| UI | [shadcn/ui](https://ui.shadcn.com) + [Radix UI](https://www.radix-ui.com) |
| Styling | [Tailwind CSS v4](https://tailwindcss.com) |
| Animation | [Framer Motion](https://www.framer.com/motion) |
| Forms | [React Hook Form](https://react-hook-form.com) + [Zod](https://zod.dev) |
| State | [Zustand](https://zustand.docs.pmnd.rs) |
| Markdown | [react-markdown](https://github.com/remarkjs/react-markdown) + [remark-gfm](https://github.com/remarkjs/remark-gfm) |
| Icons | [Lucide](https://lucide.dev) |
| Toasts | [Sonner](https://sonner.emilkowal.ski) |

## Getting Started

### Prerequisites

- Node.js 20+
- npm or bun

### Installation

```bash
git clone https://github.com/dhairyagothi/git-creator.git
cd git-creator
npm install
```

### Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Build

```bash
npm run build
```

### Preview production build

```bash
npm run preview
```

## Project Structure

```
src/
├── components/        # UI components (Navbar, Hero, GeneratorWorkspace, …)
│   └── ui/            # shadcn/ui primitives
├── hooks/             # Custom React hooks
├── lib/
│   ├── buildReadme.ts # Core markdown generation logic
│   ├── templates.ts   # Template definitions
│   ├── store.ts       # Zustand store
│   └── types.ts       # Shared TypeScript types
└── routes/            # TanStack Start file-based routes
    ├── __root.tsx
    ├── index.tsx      # Landing page
    ├── generator.tsx  # README builder workspace
    └── templates.tsx  # Template gallery
```

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a PR.

## License

[MIT](LICENSE) © 2024 Dhairya Gothi
