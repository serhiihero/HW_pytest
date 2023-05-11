import re
from HW17.utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProductItemPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    __product_container = (By.XPATH, '//div[@id="inventory_item_container"]')
    __back_to_main_content_page_button = (By.XPATH, '//button[@id="back-to-products"]')
    __remove_product_item_button = (By.XPATH, '//button[contains(@class, "btn_inventory")]')
    __add_product_to_bag_button = (By.XPATH, '//button[contains(@class,"btn_inventory")]')
    __badge_for_shopping_bag = (By.XPATH, '//span[@class="shopping_cart_badge"]')
    __content_container = (By.XPATH, '(//div[contains(@id,"inventory_container")])[1]')
    __shopping_bag_button = (By.XPATH, '//div[@id="shopping_cart_container"]')
    __shopping_container = (By.XPATH, '//div[@id="cart_contents_container"]')
    __price_location = (By.XPATH, '//div[@class="inventory_details_price"]')

    def check_presence_location_product_container(self):
        product_container = self._waiter.until(EC.visibility_of_element_located(self.__product_container))
        return product_container.is_displayed()

    def check_presence_product_in_bag(self):
        badge_for_shopping_bag = self._waiter.until(EC.visibility_of_element_located(self.__badge_for_shopping_bag))
        return badge_for_shopping_bag.is_displayed()

    def check_presence_location_content_container(self):
        content_container = self._waiter.until(EC.visibility_of_element_located(self.__content_container))
        return content_container.is_displayed()

    def check_presence_location_shopping_container(self):
        shopping_container = self._waiter.until(EC.visibility_of_element_located(self.__shopping_container))
        return shopping_container.is_displayed()

    def check_bag_is_empty(self):
        self._waiter.until(EC.invisibility_of_element(self.__badge_for_shopping_bag))
        return self

    def check_presence_price_set(self):
        price_element = self._waiter.until(EC.visibility_of_element_located(self.__price_location))
        price_text = price_element.text.strip()
        if not price_text:
            raise ValueError('Price value not found')
        price_text = price_text.replace('$', '')
        try:
            price_value = float(price_text)
            if price_value == int(price_value):
                price_value = int(price_value)
        except ValueError:
            raise ValueError('Price value is not a valid number')
        if price_value == 0:
            raise ValueError('Price value cannot be zero')
        return price_value

    def click_add_to_bag_button(self):
        self._click(self.__add_product_to_bag_button)
        return self

    def click_remove_product_item_from_product_item_page(self):
        self._click(self.__remove_product_item_button)
        return self

    def click_back_to_main_content_page_button(self):
        self._click(self.__back_to_main_content_page_button)
        return self

    def click_shopping_bag(self):
        self._click(self.__shopping_bag_button)
        return self
