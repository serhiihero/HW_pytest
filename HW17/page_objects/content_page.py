import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from HW17.page_objects.product_item_page import ProductItemPage
from HW17.page_objects.shopping_bag_page import ShoppingBagPage
from HW17.utilities.web_ui.base_page import BasePage


class ContentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __actions_menu_opened = (By.XPATH, '(//a[@tabindex="0"])[1]')
    __products_container = (By.XPATH, '(//div[@id="inventory_container"])[1]')
    __login_container = (By.XPATH, '//div[@class="login_container"]')
    __hamburger_button = (By.XPATH, '//button[@id="react-burger-menu-btn"]')
    __logout_button = (By.XPATH, '//a[@id="logout_sidebar_link"]')
    __shopping_bag_button = (By.XPATH, '//div[@id="shopping_cart_container"]')
    __product_item_button = (By.XPATH, f'//a[@id="item_{random.randint(0, 5)}_img_link"]/img')
    __add_product_to_bag_button = (
        By.XPATH, f'(//button[@class="btn btn_primary btn_small btn_inventory"])[{random.randint(1, 6)}]')

    def check_presence_of_actions_menu(self):
        actions_menu = self._waiter.until(EC.visibility_of_element_located(self.__actions_menu_opened))
        return actions_menu.is_displayed()

    def check_presence_location_content_page(self):
        products_container = self._waiter.until(EC.visibility_of_element_located(self.__products_container))
        return products_container.is_displayed()

    def check_presence_location_login_page(self):
        login_container = self._waiter.until(EC.presence_of_element_located(self.__login_container))
        return login_container.is_displayed()

    def click_hamburger_button(self):
        self._click(self.__hamburger_button)
        return self

    def click_logout_button(self):
        self._click(self.__logout_button)
        return self

    def click_shopping_bag(self):
        self._click(self.__shopping_bag_button)
        return ShoppingBagPage(self.driver)

    def click_product_item(self):
        self._waiter.until(EC.presence_of_element_located(self.__product_item_button))
        self._click(self.__product_item_button)
        return ProductItemPage(self.driver)

    def click_add_to_bag_product_item(self):
        self._click(self.__add_product_to_bag_button)
        return self
