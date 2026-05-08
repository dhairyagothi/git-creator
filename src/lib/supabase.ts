import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;

if (!supabaseUrl || !supabaseAnonKey) {
  console.warn('Supabase credentials missing in .env');
}

export const supabase = createClient(supabaseUrl || '', supabaseAnonKey || '');

/**
 * Tracks a README generation event in Supabase.
 */
export async function trackGeneration(data: {
  username?: string;
  template_id?: string;
  type: 'profile' | 'repo';
  action: 'copy' | 'download' | 'preview';
}) {
  try {
    const { error } = await supabase.from('generations').insert([
      {
        username: data.username || 'anonymous',
        template_id: data.template_id || 'custom',
        type: data.type,
        action: data.action,
        created_at: new Date().toISOString(),
      }
    ]);
    if (error) console.error('Supabase track error:', error);
  } catch (err) {
    console.error('Supabase tracking failed:', err);
  }
}
