import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// 🧱 LEGO RAG canvas dev server.
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    // Proxy API calls to the brain (backend) so we avoid CORS in dev.
    proxy: {
      "/api": "http://localhost:8000",
    },
  },
});
