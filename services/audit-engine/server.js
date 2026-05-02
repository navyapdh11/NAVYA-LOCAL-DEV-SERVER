import express from "express";
import bodyParser from "body-parser";
import { PlaywrightAuditor } from "./src/audit-playwright.js";

const app = express();
const auditor = new PlaywrightAuditor();

app.use(bodyParser.json());

app.post("/trigger-audit", async (req, res) => {
  const { url, location } = req.body;
  try {
    const results = await auditor.runAudit(url, location);
    res.json({ status: "success", data: results });
  } catch (err) {
    res.status(500).json({ status: "error", message: err.message });
  }
});

app.listen(3001, () => console.log("Audit sidecar listening on port 3001"));
