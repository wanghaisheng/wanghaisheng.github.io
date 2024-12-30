import requests
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, urlunparse

# Target sitemap file
TARGET_SITEMAP_FILE = "target_sitemap.xml"
SITEMAPS_INPUT_FILE = "sitemaps_input.txt"

def subdomain_to_subpath(url):
    """Convert subdomain URLs to subpath format."""
    parsed = urlparse(url)
    if parsed.hostname and '.' in parsed.hostname:
        subdomain = parsed.hostname.split('.')[0]
        if subdomain != 'www' and subdomain != 'example':  # Skip root domain and www
            path = f"/{subdomain}{parsed.path}"
            new_url = urlunparse(parsed._replace(netloc="example.com", path=path))
            return new_url
    return url

def fetch_and_transform_sitemaps(sitemap_urls):
    """Fetch and process sitemap URLs."""
    urls = []
    for sitemap_url in sitemap_urls:
        try:
            print(f"Fetching sitemap: {sitemap_url}")
            response = requests.get(sitemap_url)
            response.raise_for_status()
            xml_root = ET.fromstring(response.content)
            for url_elem in xml_root.findall(".//url/loc"):
                original_url = url_elem.text.strip()
                transformed_url = subdomain_to_subpath(original_url)
                urls.append(transformed_url)
        except Exception as e:
            print(f"Failed to process {sitemap_url}: {e}")
    return urls

def append_to_target_sitemap(new_urls, target_file):
    """Append new URLs to the target sitemap."""
    try:
        tree = ET.parse(target_file)
        root = tree.getroot()
    except FileNotFoundError:
        # Create a new sitemap if the target doesn't exist
        urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
        root = urlset
        tree = ET.ElementTree(root)

    # Avoid duplicate URLs
    existing_urls = {url_elem.text for url_elem in root.findall(".//url/loc")}
    for url in new_urls:
        if url not in existing_urls:
            url_elem = ET.SubElement(root, "url")
            loc_elem = ET.SubElement(url_elem, "loc")
            loc_elem.text = url

    # Save updated sitemap locally
    tree.write(target_file, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    print("Reading input sitemaps...")
    with open(SITEMAPS_INPUT_FILE, "r") as file:
        sitemap_urls = file.read().strip().split(',')

    print(f"Processing the following sitemaps: {sitemap_urls}")
    new_urls = fetch_and_transform_sitemaps(sitemap_urls)
    print(f"Fetched {len(new_urls)} new URLs.")
    append_to_target_sitemap(new_urls, TARGET_SITEMAP_FILE)
    print(f"Updated sitemap saved to {TARGET_SITEMAP_FILE}")
