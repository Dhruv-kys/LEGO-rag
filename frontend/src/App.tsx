import { useState } from "react";
import BlockPalette from "./components/BlockPalette";
import Canvas, { type PlacedBrick } from "./components/Canvas";
import type { BrickSpec } from "./blocks/catalog";

// 🧱 LEGO RAG — the canvas app.
// Boilerplate: add/remove bricks, connect a repo, and (stub) ship to the brain.
export default function App() {
  const [bricks, setBricks] = useState<PlacedBrick[]>([]);
  const [repoUrl, setRepoUrl] = useState("");

  const addBrick = (brick: BrickSpec) =>
    setBricks((prev) => [...prev, { ...brick, id: crypto.randomUUID() }]);

  const removeBrick = (id: string) =>
    setBricks((prev) => prev.filter((b) => b.id !== id));

  // TODO: POST the pipeline to the brain at /api/analyze and /api/generate.
  const build = () => {
    const pipeline = {
      repo_url: repoUrl || null,
      bricks: bricks.map((b) => ({
        id: b.id,
        category: b.category,
        type: b.type,
        config: {},
      })),
      connections: bricks.slice(1).map((b, i) => ({
        source: bricks[i].id,
        target: b.id,
      })),
      constraints: { optimize_for: ["production"] },
    };
    // eslint-disable-next-line no-console
    console.log("🚀 Shipping this build to the brain:", pipeline);
    alert("🧱 Build captured! Check the console — wiring this to /api is next.");
  };

  return (
    <div className="app">
      <header className="topbar">
        <h1>🧱 LEGO RAG</h1>
        <span className="tagline">build your RAG, brick by brick</span>
      </header>

      <div className="layout">
        <BlockPalette onAdd={addBrick} />

        <section className="workspace">
          <div className="repo-row">
            <label>🔌 Connect your repo:</label>
            <input
              type="text"
              placeholder="https://github.com/you/your-repo"
              value={repoUrl}
              onChange={(e) => setRepoUrl(e.target.value)}
            />
            <button className="build-btn" onClick={build} disabled={bricks.length === 0}>
              🚀 Build
            </button>
          </div>

          <Canvas bricks={bricks} onRemove={removeBrick} />
        </section>
      </div>
    </div>
  );
}
