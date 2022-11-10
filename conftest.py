import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="language: en or ru")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_extension(r'D:\Alitools_auto_tests\Alitools.crx')
        # Ставит флаг WebDriver(New) -> missing (passed)
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_argument("--start-maximized")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()