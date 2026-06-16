import { BRICKS, CATEGORIES, type BrickSpec } from "../blocks/catalog";

// 🧱 The palette of bricks you can snap onto the canvas, grouped by stage.
export default function BlockPalette({
  onAdd,
}: {
  onAdd: (brick: BrickSpec) => void;
}) {
  return (
    <aside className="palette">
      <h2>🧱 Bricks</h2>
      <p className="hint">Click a brick to snap it onto the canvas.</p>

      {CATEGORIES.map((cat) => (
        <div key={cat.id} className="palette-group">
          <h3 style={{ color: cat.color }}>{cat.label}</h3>
          {BRICKS.filter((b) => b.category === cat.id).map((brick) => (
            <button
              key={brick.type}
              className="brick-chip"
              style={{ borderColor: cat.color }}
              title={brick.description}
              onClick={() => onAdd(brick)}
            >
              {brick.emoji} {brick.name}
            </button>
          ))}
        </div>
      ))}
    </aside>
  );
}
