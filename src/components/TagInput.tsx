import { useState, type KeyboardEvent } from "react";
import { X } from "lucide-react";

export function TagInput({
  value,
  onChange,
  placeholder = "Add and press Enter",
}: {
  value: string[];
  onChange: (v: string[]) => void;
  placeholder?: string;
}) {
  const [draft, setDraft] = useState("");

  const add = () => {
    const v = draft.trim();
    if (!v) return;
    if (value.includes(v)) return;
    onChange([...value, v]);
    setDraft("");
  };
  const onKey = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter" || e.key === ",") {
      e.preventDefault();
      add();
    } else if (e.key === "Backspace" && !draft && value.length) {
      onChange(value.slice(0, -1));
    }
  };

  return (
    <div className="flex flex-wrap items-center gap-1.5 rounded-lg border border-border/60 bg-background/40 p-2 focus-within:border-[oklch(0.7_0.24_295)] focus-within:ring-1 focus-within:ring-[oklch(0.7_0.24_295/0.4)]">
      {value.map((t) => (
        <span
          key={t}
          className="inline-flex items-center gap-1 rounded-md bg-gradient-neon px-2 py-0.5 text-xs font-medium text-background"
        >
          {t}
          <button
            type="button"
            onClick={() => onChange(value.filter((x) => x !== t))}
            className="hover:opacity-70"
            aria-label={`Remove ${t}`}
          >
            <X className="h-3 w-3" />
          </button>
        </span>
      ))}
      <input
        value={draft}
        onChange={(e) => setDraft(e.target.value)}
        onKeyDown={onKey}
        onBlur={add}
        placeholder={value.length ? "" : placeholder}
        className="flex-1 min-w-[100px] bg-transparent px-1 py-0.5 text-sm outline-none placeholder:text-muted-foreground"
      />
    </div>
  );
}
