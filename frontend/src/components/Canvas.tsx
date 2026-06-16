import { CATEGORIES, type BrickSpec } from "../blocks/catalog";

// A brick that's been placed on the canvas.
export interface PlacedBrick extends BrickSpec {
  id: string;
}

function colorFor(category: string): string {
  return CATEGORIES.find((c) => c.id === category)?.color ?? "#888";
}

// 🧱 The build area. Bricks stack top-to-bottom; the ▼ between them is the
// "stud" connecting one brick to the next. Real drag-to-wire comes later.
export default function Canvas({
  bricks,
  onRemove,
}: {
  bricks: PlacedBrick[];
  onRemove: (id: string) => void;
}) {
  if (bricks.length === 0) {
    return (
      <main className="canvas empty">
        <div className="empty-state">
          <div className="big">🧱</div>
          <p>Your baseplate is empty.</p>
          <p className="hint">Snap a brick from the palette to start building.</p>
        </div>
      </main>
    );
  }

  return (
    <main className="canvas">
      {bricks.map((brick, i) => (
        <div key={brick.id}>
          <div className="placed-brick" style={{ borderLeftColor: colorFor(brick.category) }}>
            <span className="placed-brick-label">
              {brick.emoji} {brick.name}
            </span>
            <button className="remove" onClick={() => onRemove(brick.id)} title="Remove brick">
              ✕
            </button>
          </div>
          {i < bricks.length - 1 && <div className="stud">▼</div>}
        </div>
      ))}
    </main>
  );
}
