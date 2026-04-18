def login(page, username, password):
    page.goto("https://opensource-demo.orangehrmlive.com/")
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]', password)
    page.click('button[type="Submit"]')
