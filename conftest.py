import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.edge.options import Options as Edge_Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or edge")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en, ... (etc.)")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    user_language = request.config.getoption('language')
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options_chrome = Chrome_Options()
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options_chrome, service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "edge":
        print("\nstart edge browser for test..")
        options_edge = Edge_Options()
        options_edge.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Edge(options=options_edge, service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise pytest.UsageError("--browser_name should be chrome or edge")

    yield browser
    print("\nquit browser..")
    browser.quit()
