// src/llm.js
import OpenAI from "openai";
import dotenv from "dotenv";
dotenv.config();
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

export async function callLLC(prompt, systemRole = "You are a helpful SEO assistant.") {
  try {
    const resp = await openai.chat.completions.create({
      model: "gpt-4-turbo",
      messages: [{ role: "system", content: systemRole }, { role: "user", content: prompt }],
      temperature: 0.1,
    });
    return resp.choices[0].message.content.trim();
  } catch (err) {
    return "";
  }
}
