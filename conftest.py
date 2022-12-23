import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager as FirefoxService
from selenium_stealth import stealth
# import undetected_chromedriver as uc


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='firefox',
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
        # options.add_argument('--start-fullscreen')
        options.add_argument('--no-sandbox')
        options.add_argument('--single-process')
        options.add_argument('--disable-dev-shm-usage')
        # ======================================================
        # Ставит флаг WebDriver(New) -> missing (passed)
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                             "like Gecko) Chrome/108.0.0.0 Safari/537.36")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("disable-infobars")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_extension(r'D:\Alitools_auto_tests\Alitools.crx')
        # s = Service(ChromeService().install())
        webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True
        # Стратегия загрузки 'normal', 'eager', 'none'
        options.page_load_strategy = 'eager'
        browser = webdriver.Chrome(options=options)
        browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"""
        })
        browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                  const newProto = navigator.__proto__
                  delete newProto.webdriver
                  navigator.__proto__ = newProto
                  """
        })
        stealth(browser,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference('dom.webnotifications.enabled', False)
        options.set_preference('useAutomationExtension', False)
        options.set_preference("general.useragent.override",
                               "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0")
        # Запуск в фоне
        # options.headless = True
        ex = "alitools13897.xpi"
        ex_dir = "C:\\Users\\HP\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\4d9syyxl.default\\extensions\\"
        s = Service(FirefoxService().install())
        options.page_load_strategy = 'eager'
        browser = webdriver.Firefox(service=s, options=options)
        browser.install_addon(ex_dir + ex, temporary=True)
        browser.maximize_window()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.close()
    browser.quit()
