from playwright.sync_api import expect, sync_playwright


with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    for ch in 'user@example.com':
        page.keyboard.press(ch)

    page.keyboard.press('ControlOrMeta+A')

    page.wait_for_timeout(5000)