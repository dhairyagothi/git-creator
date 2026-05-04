# Contributing to git-creator

Thanks for taking the time to contribute! Here are a few guidelines to help things run smoothly.

## Getting Started

1. Fork the repository and clone your fork:

   ```bash
   git clone https://github.com/<your-username>/git-creator.git
   cd git-creator
   npm install
   npm run dev
   ```

2. Create a branch for your change:

   ```bash
   git checkout -b feat/your-feature-name
   ```

## Development Workflow

- `npm run dev` — start the development server
- `npm run lint` — run ESLint
- `npm run format` — run Prettier
- `npm run build` — production build (use this to check for TypeScript errors before opening a PR)

## Commit Style

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add dark/light mode toggle
fix: handle GitHub API rate-limit error gracefully
docs: update README setup instructions
refactor: extract section-order logic into hook
```

## Submitting a Pull Request

1. Make sure `npm run build` passes with no errors.
2. Keep PRs focused — one feature or fix per PR.
3. Fill in the PR template when you open a pull request.
4. Reference any related issues with `Closes #<issue-number>`.

## Reporting Bugs

Open a [bug report](https://github.com/dhairyagothi/git-creator/issues/new?template=bug_report.md) with:
- Steps to reproduce
- Expected vs actual behaviour
- Browser/OS version

## Suggesting Features

Open a [feature request](https://github.com/dhairyagothi/git-creator/issues/new?template=feature_request.md) with a clear description of the problem it solves.

## Code Style

- TypeScript strict mode — no `any` unless absolutely necessary
- Components go in `src/components/`, primitives under `src/components/ui/`
- Business logic belongs in `src/lib/`, not components
- Keep components small and focused; extract hooks when state logic grows

## License

By contributing, you agree that your changes will be licensed under the [MIT License](LICENSE).
