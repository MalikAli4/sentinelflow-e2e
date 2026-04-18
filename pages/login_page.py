class LoginPage:
    def __init__(self, page):
        self.page = page

    def load(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/")

    def login(self, username, password):
        self.page.fill('input[name="username"]', username)
        self.page.fill('input[name="password"]', password)
        self.page.click('button[type="submit"]')

    def get_dashboard_heading(self):
        return self.page.locator("h6").text_content()

    def get_error_message(self):
        return self.page.locator(".oxd-alert-content-text").text_content()
