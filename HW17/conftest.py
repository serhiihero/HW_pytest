import pytest
from HW17.page_objects.login_page import LoginPage
from HW17.utilities.config_reader import get_resource_url, get_browser_id, get_valid_user_data
from HW17.utilities.driver_factory import driver_factory


@pytest.fixture()
def open_required_browser():
    driver = driver_factory(get_browser_id())
    driver.maximize_window()
    driver.get(get_resource_url())
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(open_required_browser):
    return LoginPage(open_required_browser)


@pytest.fixture()
def open_content_page(open_login_page):
    return open_login_page.enter_username_to_input(get_valid_user_data()[0]).enter_password_to_input(
        get_valid_user_data()[1]).click_login_button()


@pytest.fixture()
def open_actions_menu(open_content_page):
    return open_content_page.click_hamburger_button()


@pytest.fixture()
def open_shopping_bag(open_content_page):
    return open_content_page.click_shopping_bag()


@pytest.fixture()
def open_product_item_page(open_content_page):
    return open_content_page.click_product_item()


@pytest.fixture()
def open_checkout_page(open_shopping_bag):
    return open_shopping_bag.click_checkout_button()
