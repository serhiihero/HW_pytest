from HW17.page_objects.checkout_page import CheckoutPage
from HW17.page_objects.product_item_page import ProductItemPage
from HW17.utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ShoppingBagPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __shopping_container = (By.XPATH, '//div[@id="cart_contents_container"]')
    __products_container = (By.XPATH, '(//div[@id="inventory_container"])[1]')
    __continue_shopping_button = (By.XPATH, '//button[@id="continue-shopping"]')
    __product_item_button = (By.XPATH, '//div[@class="cart_item_label"]/a[1]')
    __badge_for_shopping_bag = (By.XPATH, '//span[@class="shopping_cart_badge"]')
    __remove_product_item_button = (By.XPATH, '(//button[@class="btn btn_secondary btn_small cart_button"])[1]')
    __catalog_of_products = (By.XPATH, '(//div[@id="inventory_container"])[1]')
    __checkout_button = (By.XPATH, '//button[@id="checkout"]')
    __hamburger_button = (By.XPATH, '//button[@id="react-burger-menu-btn"]')
    __actions_menu_opened = (By.XPATH, '(//a[@tabindex="0"])[1]')

    def check_presence_location_shopping_bag_container(self):
        shopping_bag_container = self._waiter.until(EC.visibility_of_element_located(self.__shopping_container))
        return shopping_bag_container.is_displayed()

    def check_presence_location_content_page(self):
        products_container = self._waiter.until(EC.visibility_of_element_located(self.__products_container))
        return products_container.is_displayed()

    def check_presence_product_in_bag(self):
        badge_for_shopping_bag = self._waiter.until(EC.visibility_of_element_located(self.__badge_for_shopping_bag))
        return badge_for_shopping_bag.is_displayed()

    def click_product_item(self):
        self._click(self.__product_item_button)
        return ProductItemPage(self.driver)

    def click_remove_product_item_from_shopping_bug(self):
        self._click(self.__remove_product_item_button)
        return self

    def check_bag_is_empty(self):
        self._waiter.until(EC.invisibility_of_element(self.__badge_for_shopping_bag))
        return self

    def click_continue_shopping_button(self):
        self._click(self.__continue_shopping_button)
        return self

    def check_presence_of_products(self):
        catalog_of_products = self._waiter.until(EC.visibility_of_element_located(self.__catalog_of_products))
        return catalog_of_products.is_displayed()

    def click_checkout_button(self):
        self._click(self.__checkout_button)
        return CheckoutPage(self.driver)

    def click_hamburger_button(self):
        self._click(self.__hamburger_button)
        return self

    def check_presence_of_actions_menu(self):
        actions_menu = self._waiter.until(EC.visibility_of_element_located(self.__actions_menu_opened))
        return actions_menu.is_displayed()
