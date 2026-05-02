// src/audit-playwright.js
import { chromium } from "playwright";
import { launch } from "chrome-launcher";
import lighthouse from "lighthouse";
import { extractMetaAndSchema } from "./metadata.js";
import { logVisit } from "./db.js";
import { CircuitBreaker, exponentialBackoff } from "./retry.js";

const lb = new CircuitBreaker();

export class PlaywrightAuditor {
  async runAudit(url, location = "au_sydney") {
    const chrome = await lb.execute(() => launch({ chromeFlags: ["--no-sandbox"] }));
    const browser = await chromium.connectOverCDP(`http://localhost:${chrome.port}`);
    const page = await browser.newPage();

    const results = await exponentialBackoff(async () => {
      await page.goto(url, { waitUntil: "networkidle" });
      const metadata = await extractMetaAndSchema(page);
      
      const lhRun = await lighthouse(url, { port: chrome.port, output: "json", onlyCategories: ["seo"] });
      const lhReport = JSON.parse(lhRun.report);
      
      return { ...metadata, seoScore: lhReport.categories.seo.score * 100 };
    });

    logVisit(url, location, results);
    await browser.close();
    await chrome.kill();
    return results;
  }
}
