import { ALL_SECTIONS, type SectionId } from "@/lib/templates";
import { GripVertical, Eye, EyeOff } from "lucide-react";
import { useState } from "react";

export function SectionToggles({
  sections,
  onChange,
  availableSections,
}: {
  sections: string[];
  onChange: (s: string[]) => void;
  availableSections?: { id: string; label: string }[];
}) {
  const [draggedId, setDraggedId] = useState<string | null>(null);

  const source = availableSections ?? ALL_SECTIONS;
  const enabled = new Set(sections);
  const ordered: string[] = [
    ...sections,
    ...source.filter((a) => !enabled.has(a.id)).map((a) => a.id),
  ];

  const toggle = (id: string) => {
    if (enabled.has(id)) onChange(sections.filter((s) => s !== id));
    else onChange([...sections, id]);
  };

  const onDrop = (target: string) => {
    if (!draggedId || draggedId === target || !enabled.has(draggedId) || !enabled.has(target)) {
      setDraggedId(null);
      return;
    }
    const next = [...sections];
    const from = next.indexOf(draggedId);
    const to = next.indexOf(target);
    next.splice(from, 1);
    next.splice(to, 0, draggedId);
    onChange(next);
    setDraggedId(null);
  };

  return (
    <ul className="space-y-1">
      {ordered.map((id) => {
        const section = source.find((s) => s.id === id);
        if (!section) return null;
        const on = enabled.has(id);
        return (
          <li
            key={id}
            draggable={on}
            onDragStart={() => on && setDraggedId(id)}
            onDragOver={(e) => e.preventDefault()}
            onDrop={() => onDrop(id)}
            className={`group flex items-center gap-2 rounded-lg border px-2 py-1.5 text-sm transition-colors ${
              on
                ? "border-border/60 bg-card/40"
                : "border-border/30 bg-transparent text-muted-foreground"
            }`}
          >
            <GripVertical className={`h-3.5 w-3.5 ${on ? "text-muted-foreground cursor-grab" : "opacity-30"}`} />
            <span className="flex-1 truncate">{section.label}</span>
            <button
              onClick={() => toggle(id)}
              className="inline-flex h-6 w-6 items-center justify-center rounded text-muted-foreground hover:text-foreground transition-colors"
              aria-label={on ? "Hide" : "Show"}
            >
              {on ? <Eye className="h-3.5 w-3.5" /> : <EyeOff className="h-3.5 w-3.5" />}
            </button>
          </li>
        );
      })}
    </ul>
  );
}
