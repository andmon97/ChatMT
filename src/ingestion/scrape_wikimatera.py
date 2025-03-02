import os
import sys
import psutil
import asyncio
import logging
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from crawl4ai import (
    AsyncWebCrawler,
    BrowserConfig,
    CrawlerRunConfig,
    CacheMode,
    CrawlResult
)
from dotenv import load_dotenv, find_dotenv

# Load environment variables if needed
load_dotenv(find_dotenv())

# Configure logging
logging.basicConfig(level=logging.INFO)

# Set starting URL (the proverbs page) and CSS selector for the main content.
BASE_URLS = [
    "https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/i-proverbi-materani/",
    "https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/soprannomi-piu-diffusi/",
    "https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/grammatica-di-base/",
    "https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/unita-di-misura/",
    "https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/numeri-u-nimmr/",
    "https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/la-famiglia-ed-nomi/"]  
CSS_SELECTOR = ".entry-content"  # Adjust if the main content container is different

def extract_internal_links(html_content: str, current_url: str) -> list:
    """
    Extracts and returns a list of internal links (full URLs) from the provided HTML content.
    Only links that start with the same base path as BASE_URL are returned.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        full_url = urljoin(current_url, href)
        # Only include URLs that are within the same section
        if full_url.startswith(BASE_URL):
            links.append(full_url)
    return links

async def crawl_page(url: str, crawler: AsyncWebCrawler, crawl_config: CrawlerRunConfig, visited: set) -> (str, list):
    """
    Crawls a single page and returns a tuple:
      (Markdown content, list of internal links extracted from the page)
    """
    if url in visited:
        return None, []
    visited.add(url)
    result = await crawler.arun(url=url, config=crawl_config, session_id="proverbs_crawl")
    if not result.success:
        logging.error(f"Failed to crawl {url}: status_code={result.status_code}")
        return None, []
    # Use the Markdown if available, else try to extract from the HTML.
    md_content = result.markdown or ""
    html_content = result.html_content if hasattr(result, "html_content") else ""
    # If Markdown is empty but HTML exists, extract links from the HTML
    links = extract_internal_links(html_content, url) if html_content else []
    return md_content, links

async def recursive_crawl(start_url: str, max_depth: int = 2) -> dict:
    """
    Recursively crawls pages starting from start_url, up to max_depth levels deep.
    Returns a dictionary mapping each visited URL to its extracted Markdown content.
    """
    visited = set()
    all_content = {}

    browser_config = BrowserConfig(
        headless=True,
        verbose=False,
        extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"]
    )

    # Use a crawl configuration with a Markdown generator that extracts the main content.
    # If you want to use a custom generator, pass it here instead of None.
    crawl_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        markdown_generator=None  # Using the default extractor; adjust if needed.
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        async def _crawl(url: str, depth: int):
            if depth > max_depth:
                return
            md, links = await crawl_page(url, crawler, crawl_config, visited)
            if md:
                all_content[url] = md
                logging.info(f"[OK] Crawled: {url}")
            else:
                logging.info(f"[WARN] No content extracted for: {url}")
            for link in links:
                await _crawl(link, depth + 1)

        await _crawl(start_url, 0)
    return all_content

async def main():
    # Starting URLs list (BASE_URLS) should be defined in your config
    all_md_total = {}
    for base_url in BASE_URLS:
        logging.info(f"Starting recursive crawl from: {base_url}")
        md_result = await recursive_crawl(base_url, max_depth=2)
        # Merge results: If the same URL appears in multiple crawls, the latter will overwrite the former.
        all_md_total.update(md_result)

    output_folder = "docs_markdown"
    os.makedirs(output_folder, exist_ok=True)
    for idx, (url, md_content) in enumerate(all_md_total.items()):
        filename = f"page_{idx}.md"
        filepath = os.path.join(output_folder, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)
        logging.info(f"Saved content from {url} to {filepath}")


if __name__ == "__main__":
    asyncio.run(main())
