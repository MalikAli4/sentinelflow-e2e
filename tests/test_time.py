from pages.login_page import LoginPage
from pages.time_page import TimePage

def test_navigate_to_time_page(page):
    login_page = LoginPage(page)
    time_page = TimePage(page)

    # Log in
    login_page.load()
    login_page.login("Admin", "admin123")

    # Open Time page
    time_page.open()

    # Confirm navigation to the Time module
    assert time_page.is_time_page_open()
