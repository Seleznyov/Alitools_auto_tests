import pytest
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options


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
        options.add_argument("--start-maximized")
        # Ставит флаг WebDriver(New) -> missing (passed)
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_extension(r'D:\Alitools_auto_tests\Alitools.crx')
        browser = webdriver.Chrome(options=options)
        stealth(browser,
                languages=["en-US", "en", "ru-RU", "ru"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
    elif browser_name == "firefox":
        # options.set_preference("dom.webdriver.enabled", False)
        # options.set_preference('dom.webnotifications.enabled', False)
        # options.set_preference('useAutomationExtension', False)
        ex = "alitools13897.xpi"
        ex_dir = "C:\\Users\\HP\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\4d9syyxl.default\\extensions\\"
        browser = webdriver.Firefox()
        browser.install_addon(ex_dir + ex, temporary=True)
        browser.maximize_window()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()
