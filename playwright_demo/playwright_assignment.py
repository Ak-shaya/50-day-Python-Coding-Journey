from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)  # slow motion for visibility
        context = browser.new_context()
        page = context.new_page()

        # Step 1: Go to Bing
        page.goto("https://www.bing.com")

        # Step 2: Wait for Bing search bar
        page.wait_for_selector('xpath=//*[@id="sb_form_q"]', timeout=15000)

        # Step 3: Enter query
        page.fill('xpath=//*[@id="sb_form_q"]', 'latest trends in AI in photography and videography')

        # Step 4: Hit Enter to search
        page.keyboard.press("Enter")

        # Step 5: Wait for first result
        page.wait_for_selector('li.b_algo h2 a', timeout=15000)

        # Step 6: Click the first link
        first_result = page.locator('li.b_algo h2 a').first
        first_result.click()

        # Step 7: Wait for full page load
        page.wait_for_load_state("load")
        time.sleep(5)  # give it some breathing room

        # Step 8: Scrape metadata
        title = page.title()
        description = page.locator('meta[name="description"]').get_attribute("content")
        og_title = page.locator('meta[property="og:title"]').get_attribute("content")
        og_desc = page.locator('meta[property="og:description"]').get_attribute("content")

        # Step 9: Save to file
        with open("ai_photography_metadata.txt", "w", encoding="utf-8") as f:
            f.write(f"Title: {title}\n")
            f.write(f"Meta Description: {description}\n")
            f.write(f"OG Title: {og_title}\n")
            f.write(f"OG Description: {og_desc}\n")

        print("✅ Metadata saved to ai_photography_metadata.txt")

        input("🔍 Press Enter to close the browser...")
        browser.close()

run()
