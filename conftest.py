import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="edge",
                     help="Choose browser: chrome or edge")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "edge":
        print("\nstart edge browser for test..")
        browser = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        raise pytest.UsageError("--browser_name should be chrome or edge")
    yield browser
    print("\nquit browser..")
    browser.quit()
