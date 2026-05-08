import { Outlet, Link, createRootRoute, HeadContent, Scripts } from "@tanstack/react-router";
import { Toaster } from "@/components/ui/sonner";
import { BackgroundFX } from "@/components/BackgroundFX";

import appCss from "../styles.css?url";
import favicon from "../../assets/favicon.png?url";

import FuzzyText from "@/components/FuzzyText";

function NotFoundComponent() {
  return (
    <div className="flex min-h-screen items-center justify-center px-4">
      <div className="max-w-md text-center">
        <div className="flex justify-center text-7xl font-bold text-gradient">
          <FuzzyText 
            baseIntensity={0.2}
            hoverIntensity={0.5}
            enableHover
            color="currentColor"
          >
            404
          </FuzzyText>
        </div>
        <h2 className="mt-4 text-xl font-semibold">Page not found</h2>
        <p className="mt-2 text-sm text-muted-foreground">
          The page you're looking for doesn't exist or has been moved.
        </p>
        <div className="mt-6">
          <Link
            to="/"
            className="inline-flex items-center justify-center rounded-md bg-gradient-neon px-4 py-2 text-sm font-medium text-background transition-transform hover:scale-[1.03]"
          >
            Go home
          </Link>
        </div>
      </div>
    </div>
  );
}

export const Route = createRootRoute({
  head: () => ({
    meta: [
      { charSet: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { title: "github-readme.tech — Build a stunning GitHub profile README" },
      {
        name: "description",
        content: "Generate, preview, edit, and export a beautiful GitHub profile README in minutes. Premium templates, GitHub auto-fill, and live markdown preview.",
      },
      { property: "og:title", content: "github-readme.tech — Best GitHub Profile README Generator" },
      { property: "og:description", content: "Create a stunning GitHub profile README in seconds for FREE. 100+ premium templates, auto-fill stats, and live editor." },
      { property: "og:type", content: "website" },
      { property: "og:url", content: "https://github-readme.tech" },
      { property: "og:image", content: "https://github-readme.tech/og-image.png" },
      { name: "twitter:card", content: "summary_large_image" },
      { name: "twitter:title", content: "github-readme.tech — Best GitHub Profile README Generator" },
      { name: "twitter:description", content: "Create a stunning GitHub profile README in seconds for FREE. 100+ premium templates." },
      { name: "keywords", content: "github readme generator, github profile readme, free readme builder, stunning github profile, best readme templates" },
    ],
    links: [
      { rel: "stylesheet", href: appCss },
      { rel: "icon", type: "image/png", href: favicon },
    ],
  }),
  shellComponent: RootShell,
  component: RootComponent,
  notFoundComponent: NotFoundComponent,
});

function RootShell({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className="dark">
      <head>
        <HeadContent />
      </head>
      <body>
        {children}
        <Scripts />
      </body>
    </html>
  );
}

function RootComponent() {
  return (
    <>
      <BackgroundFX />
      <Outlet />
      <Toaster theme="dark" position="bottom-right" />
    </>
  );
}
