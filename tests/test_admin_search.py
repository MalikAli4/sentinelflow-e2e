from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_admin_search_username(page):
    login_page = LoginPage(page)
    admin_page = AdminPage(page)

    # Log in
    login_page.load()
    login_page.login("Admin", "admin123")

    # Open Admin page
    admin_page.open()

    # Search for Admin user
    admin_page.search_username("Admin")

    # Verify result
    assert admin_page.is_username_visible("Admin")
