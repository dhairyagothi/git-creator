# git-creator 🚀

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=220&section=header&text=git-creator&fontSize=65&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Modern%20GitHub%20Profile%20README%20Generator&descAlignY=60" width="100%"/>

  <p align="center">
    <strong>Build a stunning GitHub profile in minutes.</strong>
    <br />
    30+ Premium Templates • Live Preview • GitHub Auto-Fill • One-Click Export
  </p>

  <p align="center">
    <a href="https://github-readme.tech"><strong>Explore the App »</strong></a>
    <br />
    <br />
    <a href="https://github.com/dhairyagothi/git-creator/issues">Report Bug</a>
    ·
    <a href="https://github.com/dhairyagothi/git-creator/issues">Request Feature</a>
  </p>
</div>

---

## 🌟 Features

- **30+ Premium Templates** — Modern, Animated, Minimal, Student, Open Source, and more.
- **GitHub Data Integration** — Instantly fetch your profile stats, bio, and top languages.
- **Dynamic Social Badges** — Standardized Shields.io badges for LinkedIn, Instagram, X, etc.
- **Live Markdown Editor** — Real-time preview with support for manual markdown tweaks.
- **Modular Sections** — Toggle sections like Streak Stats, Trophies, Activity Graph, and Spotify.
- **One-Click Export** — Download your `README.md` or copy to clipboard instantly.
- **Rich Tech Stack Icons** — Integrated with SkillIcons for beautiful tool displays.

## 🛠 Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Framework** | [TanStack Start](https://tanstack.com/start) + React 19 |
| **Styling** | [Tailwind CSS v4](https://tailwindcss.com) + Vanilla CSS |
| **Animation** | [Framer Motion](https://www.framer.com/motion) |
| **Icons** | [Lucide](https://lucide.dev) + [React Icons](https://react-icons.github.io/react-icons/) |
| **State** | [Zustand](https://zustand.docs.pmnd.rs) |
| **Markdown** | [Shields.io](https://shields.io) + [GitHub Readme Stats](https://github.com/anuraghazra/github-readme-stats) |

## 📂 Template Library

Our library features **30+ premium templates** categorized for every type of developer. You can find all the raw markdown files in the [`md-templates/`](./md-templates) directory.

### Categories Available:
- **🎨 Minimal & Elegant**: Clean designs for a professional look.
- **✨ Animated & Dynamic**: Using SVG animations and interactive elements.
- **🚀 Full-Stack & Engineering**: Comprehensive layouts with tech stacks and project grids.
- **🎓 Student & Learner**: Track your journey, learning progress, and goals.
- **🌐 Open Source & Community**: Showcase your contributions, stats, and maintainer status.
- **🧬 Specialized**: AI/Data Science, Web3/Crypto, and Portfolio-first designs.

> [!TIP]
> Each template is built to be **highly modular**. Our engine automatically detects the `<!-- SECTION:xx -->` tags in these files to inject your dynamic GitHub data!

## 📁 Project Structure

```text
git-creator/
├── md-templates/      # 📂 ALL Markdown templates are stored here (.md)
├── src/
│   ├── components/    # Reusable UI components
│   ├── lib/           # Core builder logic & utilities
│   └── routes/        # TanStack Router file-based pages
├── public/            # Static assets
└── package.json       # Dependencies & scripts
```

## 🚀 Getting Started

### Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/dhairyagothi/git-creator.git
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run development server:
   ```bash
   npm run dev
   ```

## 🤝 Contributing

We love contributions! If you want to add a new template, simply:
1. Create a new `.md` file in the [`md-templates/`](./md-templates) directory.
2. Follow the standard section formatting.
3. Open a Pull Request!

Check out [CONTRIBUTING.md](./CONTRIBUTING.md) for more details.

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">
  <sub>Built with ❤️ by <a href="https://github.com/dhairyagothi">Dhairya Gothi</a></sub>
</div>
