const GENERATE_COUNT_KEY = "gra_generate_count_v1";

export function incrementGenerateCount(): number {
  if (typeof window === "undefined") return 0;
  try {
    const current = Number(localStorage.getItem(GENERATE_COUNT_KEY) || "0");
    const next = Number.isFinite(current) ? current + 1 : 1;
    localStorage.setItem(GENERATE_COUNT_KEY, String(next));
    return next;
  } catch {
    return 0;
  }
}

export function getGenerateCount(): number {
  if (typeof window === "undefined") return 0;
  try {
    const current = Number(localStorage.getItem(GENERATE_COUNT_KEY) || "0");
    return Number.isFinite(current) ? current : 0;
  } catch {
    return 0;
  }
}
