import re
from playwright.sync_api import Page, expect
from pages.login_page_objects import LoginPage


def test_example(page: Page):

    loginPage = LoginPage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page.get_by_role("img", name="company-branding")).to_be_visible()

    loginPage.login("Admin", "admin123")
    expect(page.get_by_role("button", name="Upgrade")).to_be_visible()

    # Navigate to the Admin section
    page.get_by_role("link", name="Admin").click()
    expect(page.get_by_role("heading", name="System Users")).to_be_visible()
