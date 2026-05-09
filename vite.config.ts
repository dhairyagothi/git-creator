// vite.config.ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import tsConfigPaths from "vite-tsconfig-paths";
import { tanstackStart } from "@tanstack/react-start/plugin/vite";

export default defineConfig({
  base: '/',
  server: {
    proxy: {
      '/api': 'http://localhost:3001',   
    },
  },
  plugins: [
    tanstackStart({
      server: {
        preset: 'node',
      },
    }),
    react(),
    tailwindcss(),
    tsConfigPaths(),
  ],
});