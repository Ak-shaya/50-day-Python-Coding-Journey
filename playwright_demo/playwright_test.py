from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        context = browser.new_context()
        page = context.new_page()

        # Step 1: Go to Bing
        page.goto("https://www.bing.com")

        # Step 2: Locate search bar using XPath and type query
        search_bar = page.locator('xpath=//*[@id="sb_form_q"]')
        search_bar.wait_for(timeout=10000)
        search_bar.fill("latest trends in AI in photography and videography")

        # Step 3: Press Enter
        page.keyboard.press("Enter")

        # Step 4: Wait for results to load
        page.wait_for_selector('//li[@class="b_algo"]//h2/a', timeout=30000)

        # Step 5: Click on first result
        first_result = page.locator('//li[@class="b_algo"]//h2/a').first
        first_result.click()

        # Step 6: Pause for observation
        input("✅ Press Enter to close the browser...")

        browser.close()

run()
