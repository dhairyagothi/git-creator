import type { FormState } from "./types";
import type { SectionId } from "./templates";

type LinkType =
  | "typing"
  | "markdown"
  | "icons"
  | "api"
  | "external"
  | "repoCard"
  | "asset"
  | "generatedAsset";

export const SECTION_LINKS: Record<SectionId, { type: LinkType; url: string | null }> = {
  header: {
    type: "typing",
    url: "https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=600&size=24&duration=2500&pause=1000&color=58A6FF&center=true&vCenter=true&width=850&lines=Building+beautiful+and+performant+web+experiences;Exploring+AI+%2B+Web+integration;Open+to+collaboration+on+impactful+projects",
  },

  about: {
    type: "markdown",
    url: null,
  },

  skills: {
    type: "icons",
    url: "https://skillicons.dev/icons?i=js,ts,python,cpp,java,html,css,react,nextjs,nodejs,express,tailwind,mongodb,firebase,git,github,vscode,figma,postman",
  },

  techStack: {
    type: "icons",
    url: "https://skillicons.dev/icons?i=js,ts,python,cpp,java,html,css,react,nextjs,nodejs,express,tailwind,mongodb,firebase,git,github,vscode,figma,postman",
  },

  githubStats: {
    type: "api",
    url: "https://github-readmeapp.vercel.app/api?username={username}&show_icons=true&theme=transparent&hide_border=true&title_color=58A6FF&text_color=c9d1d9&icon_color=58A6FF&border_radius=15&include_all_commits=true&count_private=true",
  },

  streak: {
    type: "external",
    url: "https://streak-stats.demolab.com?user={username}&theme=tokyonight&hide_border=true&border_radius=15",
  },

  topLangs: {
    type: "api",
    url: "https://github-readmeapp.vercel.app/api/top-langs/?username={username}&layout=donut&theme=transparent&hide_border=true",
  },

  projects: {
    type: "repoCard",
    url: "https://github-readmeapp.vercel.app/api/pin/?username={username}&repo={repo}&theme=tokyonight&hide_border=true",
  },

  socials: {
    type: "markdown",
    url: null,
  },

  quote: {
    type: "external",
    url: "https://quotes-github-readme.vercel.app/api?type=horizontal&theme=tokyonight",
  },

  badges: {
    type: "external",
    url: "https://komarev.com/ghpvc/?username={username}&label=Profile%20views&color=0e75b6&style=for-the-badge",
  },

  trophies: {
    type: "external",
    url: "https://github-profile-trophy.vercel.app/?username={username}&theme=tokyonight&no-frame=true&no-bg=true&margin-w=10&row=1",
  },

  gifs: {
    type: "asset",
    url: null,
  },

  snake: {
    type: "generatedAsset",
    url: "https://raw.githubusercontent.com/{username}/{username}/output/github-contribution-grid-snake.svg",
  },

  pacman: {
    type: "generatedAsset",
    url: "https://raw.githubusercontent.com/{username}/{username}/output/pacman-contribution-graph.svg",
  },

  skyline: {
    type: "generatedAsset",
    url: "./profile-3d-contrib/profile-green-animate.svg",
  },

  grass: {
    type: "external",
    url: "https://typograssy.deno.dev/",
  },

  gameOfLife: {
    type: "generatedAsset",
    url: "https://raw.githubusercontent.com/{username}/{username}/output/game-of-life.svg",
  },

  pixelArt: {
    type: "generatedAsset",
    url: null,
  },

  typing: {
    type: "typing",
    url: "https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=600&size=24&duration=2500&pause=1000&color=58A6FF&center=true&vCenter=true&width=850&lines=Frontend+Developer;Open+Source+Enthusiast;Lifelong+Learner",
  },

  spotify: {
    type: "external",
    url: "https://spotify-github-profile.kittinanx.com/api/view?uid={spotifyUserId}&cover_image=true&theme=default&show_offline=true&background=transparent&interchange=false",
  },

  leetcode: {
    type: "external",
    url: "https://leetcard.jacoblin.cool/{leetcodeUsername}?theme=dark&font=JetBrains%20Mono&ext=contest",
  },

  activityGraph: {
    type: "external",
    url: "https://github-readme-activity-graph.vercel.app/graph?username={username}&custom_title={title}&bg_color=0d1117&color=58A6FF&line=7C3AED&point=FFFFFF&area=true&hide_border=true",
  },

  footer: {
    type: "markdown",
    url: null,
  },
};

function normalizeUsername(raw: string): string {
  return raw.trim().replace(/^@+/, "");
}

function enc(s: string): string {
  return encodeURIComponent(s);
}

export function fillSectionUrl(
  templateUrl: string,
  form: FormState,
  extras?: { repo?: string; title?: string; lines?: string },
): string {
  const username = normalizeUsername(form.username || "octocat");

  let url = templateUrl
    .replaceAll("{username}", enc(username))
    .replaceAll("{repo}", enc(extras?.repo ?? ""))
    .replaceAll("{spotifyUserId}", enc(form.socials.spotify || ""))
    .replaceAll("{leetcodeUsername}", enc(form.socials.leetcode || ""))
    .replaceAll("{title}", enc(extras?.title ?? ""));

  if (extras?.lines) {
    // If we have custom lines, replace the lines param in the URL if it exists
    if (url.includes("lines=")) {
      url = url.replace(/lines=[^&]*/, `lines=${enc(extras.lines)}`);
    } else {
      url += (url.includes("?") ? "&" : "?") + `lines=${enc(extras.lines)}`;
    }
  }

  return url;
}


export function getSectionUrl(
  id: SectionId,
  form: FormState,
  extras?: { repo?: string; title?: string },
): string | null {
  const templateUrl = SECTION_LINKS[id]?.url;
  if (!templateUrl) return null;
  return fillSectionUrl(templateUrl, form, extras);
}
