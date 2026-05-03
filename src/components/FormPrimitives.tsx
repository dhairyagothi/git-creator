import type { ReactNode } from "react";

export function Field({
  label,
  hint,
  children,
}: {
  label: string;
  hint?: string;
  children: ReactNode;
}) {
  return (
    <label className="block">
      <div className="mb-1.5 flex items-center justify-between">
        <span className="text-xs font-medium text-foreground">{label}</span>
        {hint && <span className="text-[10px] text-muted-foreground">{hint}</span>}
      </div>
      {children}
    </label>
  );
}

export function Input(props: React.InputHTMLAttributes<HTMLInputElement>) {
  return (
    <input
      {...props}
      className={
        "w-full rounded-lg border border-border/60 bg-background/40 px-3 py-2 text-sm outline-none transition-colors placeholder:text-muted-foreground focus:border-[oklch(0.7_0.24_295)] focus:ring-1 focus:ring-[oklch(0.7_0.24_295/0.4)] " +
        (props.className ?? "")
      }
    />
  );
}

export function Textarea(props: React.TextareaHTMLAttributes<HTMLTextAreaElement>) {
  return (
    <textarea
      {...props}
      className={
        "w-full rounded-lg border border-border/60 bg-background/40 px-3 py-2 text-sm outline-none transition-colors placeholder:text-muted-foreground focus:border-[oklch(0.7_0.24_295)] focus:ring-1 focus:ring-[oklch(0.7_0.24_295/0.4)] resize-none " +
        (props.className ?? "")
      }
    />
  );
}
