import { motion } from "framer-motion";
import type { PropsWithChildren, HTMLAttributes } from "react";

export function GlassCard({
  children,
  className = "",
  hover = true,
  ...rest
}: PropsWithChildren<{ className?: string; hover?: boolean } & HTMLAttributes<HTMLDivElement>>) {
  return (
    <motion.div
      whileHover={hover ? { y: -4 } : undefined}
      transition={{ type: "spring", stiffness: 300, damping: 20 }}
      className={`glass rounded-2xl ${className}`}
      {...(rest as never)}
    >
      {children}
    </motion.div>
  );
}
