// src/metadata.js
export async function extractMetaAndSchema(page) {
  try {
    const metaData = await page.evaluate(() => {
      const getMeta = (name) => document.querySelector(`meta[name="${name}"]`)?.content || document.querySelector(`meta[property="${name}"]`)?.content;
      return {
        title: document.title,
        description: getMeta("description") || getMeta("og:description"),
        canonical: document.querySelector('link[rel="canonical"]')?.href,
        h1: Array.from(document.querySelectorAll("h1")).map(h => h.innerText),
        headings: Array.from(document.querySelectorAll("h2, h3")).map(h => ({ level: h.tagName, text: h.innerText })),
        og: { title: getMeta("og:title"), description: getMeta("og:description"), image: getMeta("og:image") }
      };
    });
    return metaData;
  } catch (err) {
    return { title: "", description: "", h1: [], headings: [] };
  }
}
