class AdminPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        # Click Admin menu to navigate to Admin page
        self.page.click("text=Admin")

    def search_username(self, username):
        # Fill username input field
        self.page.locator('input[class*="oxd-input"]').nth(1).fill(username)

        # Click Search button
        self.page.click("text=Search")

    def is_username_visible(self, username):
        return self.page.locator(f"text={username}").first.is_visible()
