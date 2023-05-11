from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

__CHROME = 1
__FIREFOX = 2


def driver_factory(driver_id: int):
    if int(driver_id) == __CHROME:
        return Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif int(driver_id) == __FIREFOX:
        return Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        return Chrome(service=ChromeService(ChromeDriverManager().install()))
