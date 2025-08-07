# def test_example():
#     assert 1 * 1 == 12
import pytest
from playwright.sync_api import Page,Browser

def test_google_title(page:Page,browser:Browser):
        page.goto("https://www.google.com")
        title = page.title()
        print("Page title:", title)
        assert "Google"  
          