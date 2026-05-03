import { create } from "zustand";
import type { AppState } from "./types";
import { emptyForm } from "./types";
import { getTemplate, type SectionId, type TemplateId } from "./templates";

interface Store extends AppState {
  setTemplate: (id: TemplateId) => void;
  setSections: (s: SectionId[]) => void;
  toggleSection: (s: SectionId) => void;
  updateForm: (patch: Partial<AppState["form"]>) => void;
  updateSocial: (key: keyof AppState["form"]["socials"], value: string) => void;
  setManualMarkdown: (md: string | null) => void;
  reset: () => void;
  load: (s: Partial<AppState>) => void;
}

const initial: AppState = {
  template: "animated",
  sections: getTemplate("animated").defaultSections,
  form: emptyForm,
  manualMarkdown: null,
};

export const useAppStore = create<Store>((set) => ({
  ...initial,
  setTemplate: (id) =>
    set(() => ({
      template: id,
      sections: getTemplate(id).defaultSections,
      manualMarkdown: null,
    })),
  setSections: (sections) => set({ sections }),
  toggleSection: (s) =>
    set((state) => ({
      sections: state.sections.includes(s)
        ? state.sections.filter((x) => x !== s)
        : [...state.sections, s],
    })),
  updateForm: (patch) => set((state) => ({ form: { ...state.form, ...patch } })),
  updateSocial: (key, value) =>
    set((state) => ({ form: { ...state.form, socials: { ...state.form.socials, [key]: value } } })),
  setManualMarkdown: (md) => set({ manualMarkdown: md }),
  reset: () => set(initial),
  load: (s) => set((state) => ({ ...state, ...s })),
}));
