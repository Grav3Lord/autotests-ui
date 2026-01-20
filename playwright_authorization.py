from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.locator("input[id=':r0:']")
    email_input.fill("user.name@example.com")

    password_input = page.locator("input[id=':r1:']")
    password_input.fill("password")

    login_button = page.locator("button[id='login-page-login-button']")
    login_button.click()

    bad_creds_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(bad_creds_alert).to_be_visible()
    expect(bad_creds_alert).to_have_text("Wrong email or password")

    page.wait_for_timeout(2000)
