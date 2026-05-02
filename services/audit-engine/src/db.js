// src/db.js
import Database from "better-sqlite3";
import path from "path";
import { fileURLToPath } from "url";
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const db = new Database(path.join(__dirname, "../audit.db"));

db.exec(`
  CREATE TABLE IF NOT EXISTS visits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    location TEXT NOT NULL,
    seo_score REAL DEFAULT 0,
    visited_at TEXT DEFAULT (datetime('now')),
    UNIQUE(url, location)
  )
`);

export function logVisit(url, location, data) {
  const stmt = db.prepare(`INSERT OR REPLACE INTO visits (url, location, seo_score) VALUES (?, ?, ?)`);
  stmt.run(url, location, data.seoScore ?? 0);
}
export default db;
