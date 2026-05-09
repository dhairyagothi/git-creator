import { createFileRoute } from "@tanstack/react-router";
import { Navbar } from "@/components/Navbar";
import { GeneratorWorkspace } from "@/components/GeneratorWorkspace";
import { z } from "zod";
import type { TemplateId } from "@/lib/templates";

const search = z.object({
  template: z.string().optional(),
  username: z.string().optional(),
});

export const Route = createFileRoute("/generator")({
  validateSearch: search,
  head: () => ({
    meta: [
      { title: "Generator — github-readme.tech" },
      { name: "description", content: "Build your GitHub profile README with live preview, 100+ templates, and one-click export." },
      { property: "og:title", content: "GitHub README Generator — github-readme.tech" },
      { property: "og:url", content: "https://github-readme.tech/generator" },
    ],
  }),
  component: Generator,
});

function Generator() {
  const { template: searchTemplate, username } = Route.useSearch();

  return (
    <main className="min-h-screen">
      <Navbar />
      <GeneratorWorkspace
        searchTemplate={searchTemplate as TemplateId | undefined}
        searchUsername={username}
      />
    </main>
  );
}
