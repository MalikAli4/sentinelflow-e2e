from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_navigate_to_admin_page(page):
    login_page = LoginPage(page)
    admin_page = AdminPage(page)

    # Log in
    login_page.load()
    login_page.login("Admin", "admin123")

    # Open Admin page
    admin_page.open()

    # Check URL changed to admin module
    assert "admin" in page.url
