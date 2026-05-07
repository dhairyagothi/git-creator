import { useState, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { X, ChevronDown, Plus } from "lucide-react";

export function Label({ children, required }: { children: React.ReactNode; required?: boolean }) {
  return (
    <label className="mb-1.5 block text-xs font-medium text-foreground/80">
      {children}
      {required && <span className="ml-1 text-[oklch(0.7_0.24_295)]">*</span>}
    </label>
  );
}

export function Input({
  value, onChange, placeholder, type = "text", className = "",
}: {
  value: string; onChange: (v: string) => void; placeholder?: string;
  type?: string; className?: string;
}) {
  return (
    <input
      type={type}
      value={value}
      onChange={(e) => onChange(e.target.value)}
      placeholder={placeholder}
      className={`w-full rounded-lg border border-border/60 bg-background/50 px-3 py-2 text-sm text-foreground placeholder:text-muted-foreground/50 outline-none transition-colors focus:border-[oklch(0.7_0.24_295)] focus:bg-background/80 ${className}`}
    />
  );
}

export function TagInput({
  tags, onChange, placeholder,
}: {
  tags: string[]; onChange: (tags: string[]) => void; placeholder?: string;
}) {
  const [input, setInput] = useState("");
  const inputRef = useRef<HTMLInputElement>(null);

  const add = (raw: string) => {
    const items = raw.split(",").map((s) => s.trim()).filter(Boolean);
    const next = [...new Set([...tags, ...items])];
    onChange(next);
    setInput("");
  };

  const remove = (i: number) => onChange(tags.filter((_, idx) => idx !== i));

  return (
    <div
      className="min-h-[40px] w-full cursor-text rounded-lg border border-border/60 bg-background/50 px-2 py-1.5 transition-colors focus-within:border-[oklch(0.7_0.24_295)] focus-within:bg-background/80"
      onClick={() => inputRef.current?.focus()}
    >
      <div className="flex flex-wrap gap-1.5">
        {tags.map((t, i) => (
          <span
            key={i}
            className="inline-flex items-center gap-1 rounded-md bg-[oklch(0.7_0.24_295)]/15 px-2 py-0.5 text-xs text-[oklch(0.78_0.18_295)] border border-[oklch(0.7_0.24_295)]/30"
          >
            {t}
            <button
              onClick={(e) => { e.stopPropagation(); remove(i); }}
              className="opacity-60 hover:opacity-100 transition-opacity"
            >
              <X className="h-3 w-3" />
            </button>
          </span>
        ))}
        <input
          ref={inputRef}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => {
            if ((e.key === "Enter" || e.key === ",") && input.trim()) {
              e.preventDefault();
              add(input);
            } else if (e.key === "Backspace" && !input && tags.length) {
              remove(tags.length - 1);
            }
          }}
          onBlur={() => { if (input.trim()) add(input); }}
          placeholder={tags.length ? "" : placeholder}
          className="min-w-[120px] flex-1 bg-transparent text-sm text-foreground placeholder:text-muted-foreground/50 outline-none"
        />
      </div>
    </div>
  );
}

export function Section({
  icon: Icon, title, badge, children, defaultOpen = false,
}: {
  icon: React.ElementType; title: string; badge?: string;
  children: React.ReactNode; defaultOpen?: boolean;
}) {
  const [open, setOpen] = useState(defaultOpen);
  return (
    <div className="rounded-xl border border-border/40 bg-card/20 overflow-hidden">
      <button
        onClick={() => setOpen((v) => !v)}
        className="flex w-full items-center gap-2.5 px-4 py-3 text-left hover:bg-card/30 transition-colors"
      >
        <div className="flex h-6 w-6 items-center justify-center rounded-md bg-gradient-to-br from-[oklch(0.7_0.24_295)]/20 to-[oklch(0.65_0.28_200)]/20">
          <Icon className="h-3.5 w-3.5 text-[oklch(0.78_0.18_295)]" />
        </div>
        <span className="flex-1 text-sm font-semibold">{title}</span>
        {badge && (
          <span className="rounded-full bg-[oklch(0.7_0.24_295)]/15 px-2 py-0.5 text-[10px] font-medium text-[oklch(0.78_0.18_295)]">
            {badge}
          </span>
        )}
        <ChevronDown
          className={`h-4 w-4 text-muted-foreground transition-transform duration-200 ${open ? "rotate-180" : ""}`}
        />
      </button>
      <AnimatePresence initial={false}>
        {open && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.2, ease: "easeInOut" }}
            className="overflow-hidden"
          >
            <div className="space-y-4 px-4 pb-4">{children}</div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

export function ListEditor({
  items, onChange, placeholder,
}: {
  items: string[]; onChange: (v: string[]) => void; placeholder?: string;
}) {
  const [input, setInput] = useState("");

  const add = () => {
    if (!input.trim()) return;
    onChange([...items, input.trim()]);
    setInput("");
  };

  return (
    <div className="space-y-2">
      {items.map((item, i) => (
        <div key={i} className="flex items-center gap-2">
          <span className="flex-1 rounded-lg border border-border/60 bg-background/50 px-3 py-1.5 text-sm text-foreground">
            {item}
          </span>
          <button
            onClick={() => onChange(items.filter((_, idx) => idx !== i))}
            className="flex h-7 w-7 items-center justify-center rounded-md text-muted-foreground hover:text-foreground hover:bg-card/60 transition-colors"
          >
            <X className="h-3.5 w-3.5" />
          </button>
        </div>
      ))}
      <div className="flex gap-2">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => { if (e.key === "Enter") { e.preventDefault(); add(); } }}
          placeholder={placeholder}
          className="flex-1 rounded-lg border border-border/60 bg-background/50 px-3 py-1.5 text-sm text-foreground placeholder:text-muted-foreground/50 outline-none focus:border-[oklch(0.7_0.24_295)]"
        />
        <button
          onClick={add}
          className="flex h-8 w-8 items-center justify-center rounded-lg border border-border/60 bg-card/40 text-muted-foreground hover:bg-card hover:text-foreground transition-colors"
        >
          <Plus className="h-3.5 w-3.5" />
        </button>
      </div>
    </div>
  );
}

export function ApiEndpointsEditor({
  endpoints, onChange,
}: {
  endpoints: { method: string; path: string; desc: string }[];
  onChange: (v: { method: string; path: string; desc: string }[]) => void;
}) {
  const add = () => onChange([...endpoints, { method: "GET", path: "/api/", desc: "" }]);
  const remove = (i: number) => onChange(endpoints.filter((_, idx) => idx !== i));
  const update = (i: number, patch: any) => {
    const next = [...endpoints];
    next[i] = { ...next[i], ...patch };
    onChange(next);
  };

  return (
    <div className="space-y-3">
      {endpoints.map((e, i) => (
        <motion.div
          key={i}
          initial={{ opacity: 0, y: -8 }}
          animate={{ opacity: 1, y: 0 }}
          className="relative rounded-lg border border-border/60 bg-card/30 p-3 space-y-2"
        >
          <button
            onClick={() => remove(i)}
            className="absolute right-2 top-2 flex h-6 w-6 items-center justify-center rounded-md text-muted-foreground hover:text-foreground hover:bg-card transition-colors"
          >
            <X className="h-3.5 w-3.5" />
          </button>
          <div className="flex gap-2 pr-7">
            <select
              value={e.method}
              onChange={(opt) => update(i, { method: opt.target.value })}
              className="h-9 rounded-lg border border-border/60 bg-background/50 px-2 py-1 text-[10px] font-bold outline-none"
            >
              <option>GET</option>
              <option>POST</option>
              <option>PUT</option>
              <option>DELETE</option>
              <option>PATCH</option>
            </select>
            <Input
              value={e.path}
              onChange={(v) => update(i, { path: v })}
              placeholder="/api/v1/users"
            />
          </div>
          <Input
            value={e.desc}
            onChange={(v) => update(i, { desc: v })}
            placeholder="Description..."
          />
        </motion.div>
      ))}
      <button
        onClick={add}
        className="flex w-full items-center justify-center gap-2 rounded-lg border border-dashed border-border/60 py-2 text-xs text-muted-foreground hover:border-[oklch(0.7_0.24_295)]/50 hover:text-foreground transition-colors"
      >
        <Plus className="h-3.5 w-3.5" /> Add Endpoint
      </button>
    </div>
  );
}
