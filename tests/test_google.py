import re
from playwright.sync_api import expect 

def test_google_search(page):
    page.goto("https://www.google.com/ncr")
    page.wait_for_timeout(3000)
    try:
        page.get_by_role("button",name="Accept all").click()
        print("pop-up accepted")
    except:
        print("No pop-up to accept")
    page.get_by_role("combobox").fill("learn Playwright")
    page.keyboard.press("Enter")
    expect(page).to_have_title(re.compile("Playwright",re.IGNORECASE))


    