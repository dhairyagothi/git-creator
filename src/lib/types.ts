import type { SectionId, TemplateId } from "./templates";

export interface ProjectEntry {
  name: string;
  description: string;
  url: string;
}

export interface FormState {
  username: string;
  displayName: string;
  tagline: string;
  role: string;
  title: string;
  company: string;
  focus: string;
  bio: string;
  avatarUrl: string;
  location: string;
  city: string;
  country: string;
  currentlyLearning: string;
  currentlyWorkingOn: string;
  techStack: string[];
  tools: string[];
  projects: ProjectEntry[];
  achievements: string[];
  funFacts: string[];
  contributionGoals: string;
  email: string;
  university: string;
  major: string;
  academicYear: string;
  experienceYears: string;
  resumeUrl: string;
  scholarId: string;
  templateFields: Record<string, string>;
  socials: {
    twitter: string;
    linkedin: string;
    website: string;
    youtube: string;
    devto: string;
    instagram: string;
  };
  quote: string;
}

export interface AppState {
  template: TemplateId;
  sections: SectionId[];
  form: FormState;
  manualMarkdown: string | null; // null = derived from form
}

export const emptyForm: FormState = {
  username: "",
  displayName: "",
  tagline: "Building things on the internet",
  role: "",
  title: "",
  company: "",
  focus: "",
  bio: "",
  avatarUrl: "",
  location: "",
  city: "",
  country: "",
  currentlyLearning: "",
  currentlyWorkingOn: "",
  techStack: [],
  tools: [],
  projects: [],
  achievements: [],
  funFacts: [],
  contributionGoals: "",
  email: "",
  university: "",
  major: "",
  academicYear: "",
  experienceYears: "",
  resumeUrl: "",
  scholarId: "",
  templateFields: {},
  socials: {
    twitter: "",
    linkedin: "",
    website: "",
    youtube: "",
    devto: "",
    instagram: "",
  },
  quote: "",
};
