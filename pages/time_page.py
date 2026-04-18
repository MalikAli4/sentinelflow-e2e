class TimePage:
    def __init__(self, page):
        self.page = page

    def open(self):
        # Click Time menu to navigate to Time page
        self.page.click("text=Time")

    def is_time_page_open(self):
        return "time" in self.page.url
