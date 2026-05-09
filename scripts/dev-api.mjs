// scripts/dev-api.mjs
import dotenv from 'dotenv';
dotenv.config({ path: '.env.local' });      // ← loads .env.local explicitly

import express from 'express';
import cors from 'cors';

const { default: handler } = await import('../api/analyze-repo.js');

const app = express();
app.use(cors());
app.use(express.json());

app.post('/api/analyze-repo', handler);

const PORT = 3001;
app.listen(PORT, () => {
  console.log(`✅ AI API server running on http://localhost:${PORT}`);
  console.log('GROQ_API_KEY loaded:', !!process.env.GROQ_API_KEY); // quick check
});