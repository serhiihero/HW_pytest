from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self._waiter = WebDriverWait(self.driver, 10, 1)

    def _wait_until_element_located(self, locator):
        return self._waiter.until(EC.presence_of_element_located(locator))

    def _wait_until_to_be_clickable(self, locator):
        return self._waiter.until(EC.element_to_be_clickable(locator))

    def _send_keys(self, locator, value, is_clear=True):
        element = self._wait_until_element_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def _click(self, locator):
        self._wait_until_to_be_clickable(locator).click()
