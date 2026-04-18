import os
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only take screenshot after the actual test call fails
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("artifacts/screenshots", exist_ok=True)
            screenshot_path = f"artifacts/screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
