import { motion } from "framer-motion";
import type { PropsWithChildren } from "react";

export function GlassCard({
  children,
  className = "",
  hover = true,
}: PropsWithChildren<{ className?: string; hover?: boolean }>) {
  return (
    <motion.div
      whileHover={hover ? { y: -4 } : undefined}
      transition={{ type: "spring", stiffness: 300, damping: 20 }}
      className={`glass rounded-2xl ${className}`}
    >
      {children}
    </motion.div>
  );
}
