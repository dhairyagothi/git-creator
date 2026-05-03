export function BackgroundFX() {
  return (
    <div className="pointer-events-none fixed inset-0 -z-10 overflow-hidden">
      <div className="absolute inset-0 grid-bg opacity-40" />
      <div className="absolute -top-40 -left-40 h-[520px] w-[520px] rounded-full bg-[oklch(0.5_0.25_295)] opacity-30 blur-[120px] animate-blob" />
      <div className="absolute top-1/3 -right-40 h-[520px] w-[520px] rounded-full bg-[oklch(0.6_0.2_200)] opacity-25 blur-[120px] animate-blob [animation-delay:-6s]" />
      <div className="absolute bottom-0 left-1/3 h-[420px] w-[420px] rounded-full bg-[oklch(0.6_0.28_340)] opacity-20 blur-[120px] animate-blob [animation-delay:-12s]" />
      <div className="absolute inset-0 bg-gradient-to-b from-transparent via-background/40 to-background" />
    </div>
  );
}
