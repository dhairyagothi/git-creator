## github-readme.app — Premium GitHub Profile README Builder

A desktop-first, dark-themed SaaS tool for generating beautiful GitHub profile READMEs with live preview, templates, and export.

### Pages & Routes

- `/` — Animated landing (hero, features, template showcase, social proof, FAQ, footer)
- `/generator` — Three-panel workspace (templates + sections | form | live preview/editor)
- `/templates` — Full template gallery with search and filter

### Visual Design

- Dark only: near-black base with deep slate surfaces
- Neon gradient accents (violet → cyan → magenta) on CTAs, headings, focus rings
- Glassmorphism cards: subtle border, backdrop blur, soft inner glow
- Animated background: slow drifting gradient blobs + faint grid overlay
- Typography: tight display headings, mono accents for code/markdown
- Framer Motion: page enter, scroll reveals, hover lift, animated number counter, tab/route transitions, button glow on hover

### Landing Page

- Top nav: logo, links (Templates, Generator, FAQ), animated user counter chip, "Start Generating" button
- Hero: bold headline, subheading, primary CTA (→ /generator), secondary CTA (→ /templates), floating preview cards of sample READMEs
- Live counter card: "12,480+ developers" with animated count-up (locally driven, structured to swap for API later)
- Feature grid (6 tiles): templates, live preview, GitHub auto-fill, markdown editor, one-click export, autosave
- Template showcase strip: 4 featured templates with hover preview
- Social proof row: logos / quotes
- FAQ accordion
- Footer with links and brand

### Generator Workspace (main product)

Three-column desktop layout (collapses to tabs on small screens):

**Left sidebar**
- Template picker (cards with name, tag, preview thumbnail, select button)
- Section toggles (Header, About, Skills, Tech Stack, GitHub Stats, Streak, Top Languages, Projects, Socials, Quote, Badges, Footer) with drag-to-reorder
- Recently used templates

**Center panel — Form**
- GitHub username input with "Fetch profile" button (calls public GitHub API to auto-fill name, bio, avatar, location, blog, twitter); loading skeleton + error toast on failure
- Grouped fields: Identity (display name, tagline, bio), Currently (learning, working on), Stack (tech, tools — tag inputs), Projects (repeatable), Achievements, Socials (twitter, linkedin, website, youtube, dev.to), Contact email, Fun facts, Contribution goals
- Inline validation, tooltips, keyboard shortcuts (⌘C copy, ⌘R reset, ⌘S save)

**Right panel — Preview / Edit**
- Tabs: Preview | Markdown
- Preview renders GitHub-flavored markdown with shields.io badges and github-readme-stats image URLs
- Markdown tab: editable code area with syntax styling
- Toolbar: Copy markdown, Download README.md, Reset, Save draft (localStorage autosave with toast)

### Templates (8)

Minimal Profile, Animated Profile, Full Stack Developer, Student/Beginner, Open Source Contributor, Data/AI Developer, Web3/Blockchain Developer, Professional Portfolio. Each: name, description, tags (popular/minimal/advanced), preview thumb, select action. Searchable + filterable by tag.

### Markdown Generation

Pure function `buildReadme(formState, template, enabledSections)` composes section blocks in chosen order. Sections include header banner, typing SVG (for animated template), about block, skills via shields.io badges, github-readme-stats card URL, streak stats URL, top-langs URL, projects table, socials row, quote block, footer. Editing markdown directly switches state to "manual mode" so form edits don't overwrite user changes (with prompt to re-sync).

### State & Persistence

- Local React state + Zustand-style store (or context) for form, template, sections, markdown
- localStorage autosave (debounced) — restored on load with toast
- User counter: starts from a base seeded value, increments locally on first visit; structured behind a `useUserCount()` hook so a backend can be wired later

### Tech Details

- TanStack Start routes: `index.tsx`, `generator.tsx`, `templates.tsx`, plus `__root.tsx` shell with global animated background
- Components in `src/components/`: `Navbar`, `Hero`, `FeatureGrid`, `TemplateCard`, `TemplateShowcase`, `UserCounter`, `FAQ`, `Footer`, `GeneratorLayout`, `TemplateSidebar`, `SectionToggles`, `ProfileForm`, `TagInput`, `MarkdownPreview`, `MarkdownEditor`, `ExportToolbar`, `GlowButton`, `GlassCard`, `BackgroundBlobs`
- Templates and section builders in `src/lib/templates/` and `src/lib/markdown/`
- GitHub fetch via `https://api.github.com/users/:username` (no auth, client-side, rate-limit aware)
- Markdown rendering with `react-markdown` + `remark-gfm`; code styling via existing tailwind tokens
- Framer Motion for all motion; Lucide for icons; Sonner for toasts (already available)
- Update `src/styles.css` to dark-by-default with neon gradient tokens

### Out of Scope (for this build)

- Real backend user counter, accounts, cloud-saved drafts, payments — structured for future wiring but not implemented
