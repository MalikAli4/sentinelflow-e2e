from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_admin_search_invalid_username(page):
    login_page = LoginPage(page)
    admin_page = AdminPage(page)

    # Log in
    login_page.load()
    login_page.login("Admin", "admin123")

    # Open Admin page
    admin_page.open()

    # Search for a username that should not exist
    fake_username = "NotARealUser123"
    admin_page.search_username(fake_username)

    # Confirm the fake username does not appear in results
    assert not admin_page.is_username_visible(fake_username)
