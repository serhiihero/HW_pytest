from selenium.webdriver.common.by import By
from HW17.page_objects.content_page import ContentPage
from HW17.utilities.web_ui.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __email_input = (By.XPATH, '//input[@id="user-name"]')
    __password_input = (By.XPATH, '//input[@id="password"]')
    __login_button = (By.XPATH, '//input[@id="login-button"]')
    __error_state = (By.XPATH, "//div[@class='error-message-container error']")

    def enter_username_to_input(self, email: str):
        self._send_keys(locator=self.__email_input, value=email)
        return self

    def enter_password_to_input(self, password: str):
        self._send_keys(locator=self.__password_input, value=password)
        return self

    def click_login_button(self):
        self._click(self.__login_button)
        return ContentPage(self.driver)

    def check_presence_of_warning_empty_inputs(self):
        error_message = 'Epic sadface: Username is required'
        error_element = self._waiter.until(EC.visibility_of_element_located(self.__error_state))
        return error_element.text == error_message

    def check_presence_of_warning_empty_username(self):
        return self.check_presence_of_warning_empty_inputs()

    def check_presence_of_warning_empty_password(self):
        error_message = 'Epic sadface: Password is required'
        error_element = self._waiter.until(EC.visibility_of_element_located(self.__error_state))
        return error_element.text == error_message

    def check_presence_of_warning_wrong_creds(self):
        error_message = 'Epic sadface: Username and password do not match any user in this service'
        error_element = self._waiter.until(EC.visibility_of_element_located(self.__error_state))
        return error_element.text == error_message

    def check_presence_of_warning_blocked_user(self):
        error_message = 'Epic sadface: Sorry, this user has been locked out.'
        error_element = self._waiter.until(EC.visibility_of_element_located(self.__error_state))
        return error_element.text == error_message
