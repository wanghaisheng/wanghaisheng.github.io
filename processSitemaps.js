const fs = require("fs");
const axios = require("axios");
const { parseStringPromise, Builder } = require("xml2js");
const path = require("path");

// Target sitemap file
const TARGET_SITEMAP_FILE = "target_sitemap.xml";

// Convert subdomain to subpath
function subdomainToSubpath(url) {
  try {
    const urlObj = new URL(url);
    const hostnameParts = urlObj.hostname.split(".");
    if (hostnameParts.length > 2) {
      const subdomain = hostnameParts[0];
      if (subdomain !== "www") {
        urlObj.hostname = "example.com";
        urlObj.pathname = `/${subdomain}${urlObj.pathname}`;
      }
    }
    return urlObj.toString();
  } catch (error) {
    console.error(`Invalid URL: ${url}`);
    return null;
  }
}

// Fetch and process sitemap URLs
async function fetchAndTransformSitemaps(sitemapUrls) {
  const urls = new Set();
  for (const sitemapUrl of sitemapUrls) {
    try {
      console.log(`Fetching sitemap: ${sitemapUrl}`);
      const response = await axios.get(sitemapUrl);
      const result = await parseStringPromise(response.data);

      if (result.urlset && result.urlset.url) {
        for (const entry of result.urlset.url) {
          const loc = entry.loc[0];
          const transformedUrl = subdomainToSubpath(loc);
          if (transformedUrl) {
            urls.add(transformedUrl);
          }
        }
      }
    } catch (error) {
      console.error(`Failed to process ${sitemapUrl}:`, error.message);
    }
  }
  return Array.from(urls);
}

// Append new URLs to the target sitemap
async function appendToTargetSitemap(newUrls, targetFile) {
  let existingUrls = new Set();
  let urlset = { urlset: { url: [] } };

  if (fs.existsSync(targetFile)) {
    const content = fs.readFileSync(targetFile, "utf-8");
    const parsed = await parseStringPromise(content);
    if (parsed.urlset && parsed.urlset.url) {
      existingUrls = new Set(parsed.urlset.url.map((entry) => entry.loc[0]));
      urlset = parsed;
    }
  }

  for (const url of newUrls) {
    if (!existingUrls.has(url)) {
      urlset.urlset.url.push({ loc: [url] });
    }
  }

  const builder = new Builder();
  const xml = builder.buildObject(urlset);
  fs.writeFileSync(targetFile, xml, "utf-8");
  console.log(`Updated sitemap saved to ${targetFile}`);
}

// Main function
async function main() {
  const sitemapUrlsInput = process.env.SITEMAP_URLS || "";
  const sitemapUrls = sitemapUrlsInput.split(",").map((url) => url.trim()).filter(Boolean);

  if (sitemapUrls.length === 0) {
    console.error("No sitemap URLs provided. Please set SITEMAP_URLS.");
    process.exit(1);
  }

  console.log("Processing sitemaps...");
  const newUrls = await fetchAndTransformSitemaps(sitemapUrls);
  console.log(`Fetched ${newUrls.length} new URLs.`);
  await appendToTargetSitemap(newUrls, TARGET_SITEMAP_FILE);
}

main().catch((error) => {
  console.error("An error occurred:", error);
  process.exit(1);
});
