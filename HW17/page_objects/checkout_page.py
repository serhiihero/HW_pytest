from HW17.page_objects.checkout_summary_page import CheckoutSummaryPage
from HW17.utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __checkout_page = (By.XPATH, '//div[@id="checkout_info_container"]')
    __continue_button = (By.XPATH, '//input[@id="continue"]')
    __error_state = (By.XPATH, '//div[@class="error-message-container error"]')
    __shopping_container = (By.XPATH, '//div[@id="cart_contents_container"]')
    __products_container = (By.XPATH, '(//div[@id="inventory_container"])[1]')
    # here should be back button, but they have only cancel, which is wrong
    __back_button = (By.XPATH, '//button[@id="cancel"]')
    __first_name_input = (By.XPATH, '//input[@id="first-name"]')
    __last_name_input = (By.XPATH, '//input[@id="last-name"]')
    __postal_code_input = (By.XPATH, '//input[@id="postal-code"]')
    __hamburger_button = (By.XPATH, '//button[@id="react-burger-menu-btn"]')
    __actions_menu_opened = (By.XPATH, '(//a[@tabindex="0"])[1]')

    def check_presence_location_shopping_bag_container(self):
        shopping_bag_container = self._waiter.until(EC.visibility_of_element_located(self.__shopping_container))
        return shopping_bag_container.is_displayed()

    def check_presence_location_checkout_page(self):
        checkout_page = self._waiter.until(EC.presence_of_element_located(self.__checkout_page))
        return checkout_page.is_displayed()

    def check_presence_location_content_page(self):
        products_container = self._waiter.until(EC.visibility_of_element_located(self.__products_container))
        return products_container.is_displayed()

    def check_presence_error_state(self):
        warning = self._waiter.until(EC.presence_of_element_located(self.__error_state))
        return warning.is_displayed()

    def check_presence_of_actions_menu(self):
        actions_menu = self._waiter.until(EC.visibility_of_element_located(self.__actions_menu_opened))
        return actions_menu.is_displayed()

    def click_continue_button(self):
        self._click(self.__continue_button)
        return CheckoutSummaryPage(self.driver)

    def click_back_button(self):
        self._click(self.__back_button)
        return self

    def click_hamburger_button(self):
        self._click(self.__hamburger_button)
        return self

    def enter_user_data_to_inputs(self):
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        postal_code = fake.postalcode()
        self._send_keys(self.__first_name_input, first_name)
        self._send_keys(self.__last_name_input, last_name)
        self._send_keys(self.__postal_code_input, postal_code)

        user_data = {
            'first_name': first_name,
            'last_name': last_name,
            'postal_code': postal_code,
        }
        return CheckoutPage(self.driver)
