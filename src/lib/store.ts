import { create } from "zustand";
import type { AppState } from "./types";
import { emptyForm } from "./types";
import { getTemplate, TEMPLATES, type SectionId, type TemplateId } from "./templates";

interface Store extends AppState {
  setTemplate: (id: TemplateId) => void;
  setSections: (s: SectionId[]) => void;
  toggleSection: (s: SectionId) => void;
  updateForm: (patch: Partial<AppState["form"]>) => void;
  updateSocial: (key: keyof AppState["form"]["socials"], value: string) => void;
  updateTemplateField: (key: string, value: string) => void;
  setManualMarkdown: (md: string | null) => void;
  reset: () => void;
  load: (s: Partial<AppState>) => void;
}

const initial: AppState = {
  template: TEMPLATES[0]?.id ?? "",
  sections: TEMPLATES[0]?.defaultSections ?? [],
  form: emptyForm,
  manualMarkdown: null,
};

export const useAppStore = create<Store>((set) => ({
  ...initial,
  setTemplate: (id) =>
    set(() => {
      const next = getTemplate(id);
      return {
        template: next.id,
        sections: next.defaultSections,
        manualMarkdown: null,
      };
    }),
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
  updateTemplateField: (key, value) =>
    set((state) => ({
      form: {
        ...state.form,
        templateFields: { ...state.form.templateFields, [key]: value },
      },
    })),
  setManualMarkdown: (md) => set({ manualMarkdown: md }),
  reset: () => set(initial),
  load: (s) =>
    set((state) => {
      const nextTemplate = s.template ? getTemplate(s.template) : getTemplate(state.template);
      const nextForm = s.form ? { ...emptyForm, ...s.form, templateFields: s.form.templateFields ?? {} } : state.form;
      return {
        ...state,
        ...s,
        template: nextTemplate.id,
        sections: s.sections ?? nextTemplate.defaultSections,
        form: nextForm,
      };
    }),
}));
