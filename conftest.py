import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager as ChromeService
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager as FirefoxService
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import os
from .settings import TOKEN
os.environ['GH_TOKEN'] = TOKEN


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
        # options.add_argument('--start-fullscreen')
        # ======================================================
        # Ставит флаг WebDriver(New) -> missing (passed)
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                             "like Gecko) Chrome/108.0.0.0 Safari/537.36")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_extension(r'D:\Alitools_auto_tests\Alitools.crx')
        # s = Service(ChromeService().install())
        # webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = False
        # webdriver.DesiredCapabilities.CHROME['acceptInsecureCerts'] = False
        # Стратегия загрузки 'normal', 'eager', 'none'
        options.page_load_strategy = 'eager'
        browser = webdriver.Chrome(options=options)
        browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"""
        })
        # browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        #     "source": """
        #           const newProto = navigator.__proto__
        #           delete newProto.webdriver
        #           navigator.__proto__ = newProto
        #           """
        # })
        stealth(browser,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        # browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference('dom.webnotifications.enabled', False)
        options.set_preference('useAutomationExtension', False)
        # options.set_preference("network.proxy.socks_remote_dns", False)
        # webdriver.DesiredCapabilities.FIREFOX['acceptSslCerts'] = False
        # webdriver.DesiredCapabilities.FIREFOX['acceptInsecureCerts'] = False
        options.set_preference("general.useragent.override",
                               "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0")
        # Запуск в фоне
        # options.headless = True
        ex = "alitools13939.xpi"
        ex_dir = "C:\\Users\\HP\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\2gsnd2e6.default\\extensions\\"
        # s = Service(FirefoxService().install())
        options.page_load_strategy = 'normal'
        # browser = webdriver.Firefox(service=s, options=options)
        browser = webdriver.Firefox(executable_path="Tools", options=options)
        browser.install_addon(ex_dir + ex, temporary=True)
        browser.maximize_window()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.close()
    browser.quit()
