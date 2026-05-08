# Contributing to git-creator 🤝

Thanks for taking the time to contribute! This project thrives on community templates and features.

## 🎨 Adding New Templates

The easiest way to contribute is by adding a new README template. All templates are stored in the [`md-templates/`](./md-templates) directory.

### Template Guidelines
1. **File Naming**: Use the format `XX-template-name.md` (e.g., `32-modern-minimal.md`).
2. **Sectioning**: Use HTML comments to wrap dynamic sections. This allows our builder to inject user data:
   ```markdown
   <!-- SECTION:header -->
   Your header markdown here
   <!-- /SECTION:header -->

   <!-- SECTION:about -->
   Your about me markdown here
   <!-- /SECTION:about -->
   ```
3. **Available Sections**:
   - `header`, `typing`, `about`, `socials`, `techStack`, `githubStats`, `topLangs`, `streak`, `trophies`, `activityGraph`, `projects`, `footer`, `quote`, `badges`.
4. **Placeholders**: Use standard placeholders like `YOUR_NAME`, `YOUR_USERNAME`, `YOUR_TAGLINE` which will be automatically replaced by the generator.

## 🛠️ Development Setup

1. Fork the repository and clone your fork:
   ```bash
   git clone https://github.com/<your-username>/git-creator.git
   cd git-creator
   npm install
   npm run dev
   ```
2. Create a feature branch:
   ```bash
   git checkout -b feat/your-feature-name
   ```

## 📜 Commit Style
We use [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `refactor:` for code restructuring

## 🚀 Submitting Changes
1. Run `npm run build` to ensure there are no TypeScript or build errors.
2. Open a Pull Request with a clear description of your changes.
3. If you added a template, include a screenshot of the preview if possible.

## 💻 Code Style
- **TypeScript**: Use strict types; avoid `any`.
- **Styling**: We use Tailwind CSS v4. Stick to our established design tokens (gradients, glassmorphism).
- **Separation of Concerns**: Keep business logic in `src/lib/` and UI in `src/components/`.

---

By contributing, you agree that your changes will be licensed under the [MIT License](LICENSE).
