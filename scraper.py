from playwright.sync_api import sync_playwright
import time

class Scraper:
    def __init__(self):
        pass

    def scrape_and_screenshot(self, url, screenshot_path="screenshot.png"):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            page.wait_for_selector(".mw-parser-output")
            content_elem = page.query_selector(".mw-parser-output")
            content = content_elem.inner_text() if content_elem else ""
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"Screenshot saved as {screenshot_path}")
            browser.close()
            return content



if __name__ == "__main__":
    page_no = 1
    while (page_no <= 3):
        url = f"https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_{page_no}"
        scraper = Scraper()
        text = scraper.scrape_and_screenshot(url, f"screenshots/chapter{page_no}.png")
        with open(f"text/chapter{page_no}.txt", "w") as f:
            f.write(text)
        print(f"Scraped text saved as chapter{page_no}.txt")
        print(f"Chapter no {page_no} done")
        time.sleep(5)
        page_no += 1
