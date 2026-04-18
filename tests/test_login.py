from pages.login_page import LoginPage

def test_valid_login(page):
    # Create a LoginPage object and pass in the browser page
    login_page = LoginPage(page)

    # Open the login page URL
    login_page.load()

    # Perform login with valid credentials
    login_page.login("Admin", "admin123")

    # Get the dashboard heading text from the page object
    dashboard_text = login_page.get_dashboard_heading()

    # Check that login was successful
    assert dashboard_text == "Dashboard"


def test_invalid_login(page):
    # Create a LoginPage object and pass in the browser page
    login_page = LoginPage(page)

    # Open the login page URL
    login_page.load()

    # Perform login with invalid credentials
    login_page.login("WrongUser", "WrongPass")

    # Get the error message from the page object
    error_text = login_page.get_error_message()

    # Check that invalid login was rejected
    assert "Invalid credentials" in error_text
