from playwright.sync_api import sync_playwright

class WikisourceScraper:
    def __init__(self):
        pass

    def scrape_and_screenshot(self, url, screenshot_path="screenshot.png"):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            # Wait for main content to load
            page.wait_for_selector(".mw-parser-output")
            # Extract chapter text
            content_elem = page.query_selector(".mw-parser-output")
            content = content_elem.inner_text() if content_elem else ""
            # Save screenshot
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"Screenshot saved as {screenshot_path}")
            browser.close()
            return content

if __name__ == "__main__":
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    scraper = WikisourceScraper()
    text = scraper.scrape_and_screenshot(url, "chapter1.png")
    with open("chapter1.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Scraped text saved as chapter1.txt")
