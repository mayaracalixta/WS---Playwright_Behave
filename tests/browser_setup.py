from playwright.sync_api import sync_playwright

def start_browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    return playwright, browser, page

def stop_browser(playwright, browser):
    browser.close()
    playwright.stop()
