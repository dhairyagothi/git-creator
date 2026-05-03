import { createFileRoute } from "@tanstack/react-router";
import { Navbar } from "@/components/Navbar";
import { GeneratorWorkspace } from "@/components/GeneratorWorkspace";
import { z } from "zod";
import { useEffect } from "react";
import { useAppStore } from "@/lib/store";
import type { TemplateId } from "@/lib/templates";

const search = z.object({
  template: z.string().optional(),
});

export const Route = createFileRoute("/generator")({
  validateSearch: search,
  head: () => ({
    meta: [
      { title: "Generator — github-readme.app" },
      { name: "description", content: "Build your GitHub profile README with live preview and one-click export." },
    ],
  }),
  component: Generator,
});

function Generator() {
  const { template: searchTemplate } = Route.useSearch();
  const setTemplate = useAppStore((s) => s.setTemplate);

  useEffect(() => {
    if (searchTemplate) setTemplate(searchTemplate as TemplateId);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [searchTemplate]);

  return (
    <main className="min-h-screen">
      <Navbar />
      <GeneratorWorkspace />
    </main>
  );
}
