import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_orangehrm(page):

        # Navigate to the OrangeHRM login page
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.wait_for_timeout(3000)

        # Fill in the login form
        page.get_by_role("textbox", name="Username").fill("Admin")
        page.wait_for_timeout(1000)
        page.get_by_role("textbox", name="Password").click()
        page.get_by_role("textbox", name="Password").fill("admin123")
        page.get_by_role("button", name="Login").click()

        # Add any additional interactions or assertions here
    
    #page.get_by_role("link", name="Admin").click()
    # page.get_by_role("heading", name="System Users").click()
    # page.get_by_role("heading", name="/ User Management").click()
    # expect(page.locator("div").filter(has_text=re.compile(r"^AdminUser Management$"))).to_be_visible()
    # expect(page.locator("h5")).to_contain_text("System Users")

    # ---------------------