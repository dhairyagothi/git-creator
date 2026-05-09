import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import tsConfigPaths from "vite-tsconfig-paths";
import { tanstackStart } from "@tanstack/react-start/plugin/vite";

export default defineConfig({
  base: '/',
  plugins: [
    tanstackStart({
      // Force Node.js preset, not Cloudflare
      server: {
        preset: 'node',
      },
    }),
    react(),
      tailwindcss(),
    tsConfigPaths(),
  ],
});