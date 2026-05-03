import { motion, useInView, useMotionValue, useSpring, useTransform } from "framer-motion";
import { useEffect, useRef } from "react";
import { Users } from "lucide-react";

const BASE = 12480;

function getCount() {
  if (typeof window === "undefined") return BASE;
  try {
    const stored = localStorage.getItem("gra_user_count");
    if (stored) return parseInt(stored, 10);
    const seed = BASE + Math.floor(Math.random() * 40);
    localStorage.setItem("gra_user_count", String(seed));
    return seed;
  } catch {
    return BASE;
  }
}

export function UserCounter({ compact = false, big = false }: { compact?: boolean; big?: boolean }) {
  const ref = useRef<HTMLDivElement>(null);
  const inView = useInView(ref, { once: true, margin: "-50px" });
  const mv = useMotionValue(0);
  const spring = useSpring(mv, { duration: 1500, bounce: 0 });
  const display = useTransform(spring, (v) => Math.floor(v).toLocaleString());

  useEffect(() => {
    if (inView) mv.set(getCount());
  }, [inView, mv]);

  if (compact) {
    return (
      <div ref={ref} className="hidden lg:flex items-center gap-2 rounded-full border border-border/60 bg-card/40 px-3 py-1.5 text-xs">
        <span className="relative flex h-2 w-2">
          <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-emerald-400 opacity-75" />
          <span className="relative inline-flex h-2 w-2 rounded-full bg-emerald-400" />
        </span>
        <motion.span className="font-mono text-foreground">{display as unknown as string}</motion.span>
        <span className="text-muted-foreground">developers</span>
      </div>
    );
  }

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
      className={`glass rounded-2xl p-6 ${big ? "text-center" : ""}`}
    >
      <div className="flex items-center gap-3">
        <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-neon">
          <Users className="h-5 w-5 text-background" />
        </div>
        <div>
          <motion.div className="text-2xl font-bold tracking-tight font-display">
            {display as unknown as string}
            <span className="text-gradient">+</span>
          </motion.div>
          <div className="text-xs text-muted-foreground">developers built their README here</div>
        </div>
      </div>
    </motion.div>
  );
}
