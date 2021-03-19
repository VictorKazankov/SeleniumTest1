import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

from pages.main_page import MainPage
from pages.search_page import SearchPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--language", action="store", default="ru")

def get_language_local_chrome(request):
    local = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': local})
    return options


def get_language_local_firefox(request):
    local = request.config.getoption("--language")
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", local)
    return fp


def change_browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        br = webdriver.Chrome(ChromeDriverManager().install(), options=get_language_local_chrome(request))
    elif browser_name == "firefox":
        br = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                               firefox_profile=get_language_local_firefox(request))
    else:
        raise ValueError("Unrecognized browser {}".format(browser_name))
    return br


@pytest.fixture(scope="function")
def browser(request):
    browser = change_browser(request)
    yield browser
    browser.quit()


@pytest.fixture()
def main_page(browser):
    main_page_url = "https://www.booking.com/"
    main_page = MainPage(browser, main_page_url)
    main_page.open()
    return main_page


@pytest.fixture()
def search_page(browser, main_page):
    main_page.open_bukovel_hotel_list()
    search_page = SearchPage(browser, browser.current_url)
    return search_page
