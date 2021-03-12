import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")


def change_browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        br = webdriver.Chrome()
    elif browser_name == "firefox":
        br = webdriver.Firefox()
    else:
        raise ValueError("Unrecognized browser {}".format(browser_name))
    return br


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    browser = change_browser(request)
    yield browser
    print("\nquit browser..")
    browser.quit()
