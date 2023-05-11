from HW17.utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CheckoutSummaryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __checkout_summary_container = (By.XPATH, '//div[@id="checkout_summary_container"]')
    __cancel_button = (By.XPATH, '//button[@id="cancel"]')
    __products_container = (By.XPATH, '(//div[@id="inventory_container"])[1]')

    def check_presence_location_checkout_summary_page(self):
        checkout_summary_page = self._waiter.until(EC.presence_of_element_located(self.__checkout_summary_container))
        return checkout_summary_page.is_displayed()

    def click_cancel_button(self):
        self._click(self.__cancel_button)
        return self

    def check_presence_location_content_page(self):
        products_container = self._waiter.until(EC.visibility_of_element_located(self.__products_container))
        return products_container.is_displayed()
