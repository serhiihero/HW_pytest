from pytest import mark


@mark.smoke
@mark.regression
def test_add_to_bag_product_item(open_product_item_page):
    product_item = open_product_item_page
    product_item.click_add_to_bag_button()
    assert product_item.check_presence_product_in_bag(), \
        'Something went wrong. Not able to verify items in bag.'


@mark.smoke
@mark.regression
def test_remove_from_bag_product_item(open_product_item_page):
    product_item = open_product_item_page
    product_item.click_add_to_bag_button().click_remove_product_item_from_product_item_page()
    assert product_item.check_bag_is_empty(), \
        'Something went wrong. Not able to verify items in bag.'


@mark.regression
def test_back_button_from_product_item(open_product_item_page):
    product_item = open_product_item_page
    product_item.click_back_to_main_content_page_button()
    assert product_item.check_presence_location_content_container(), \
        'Something went wrong. User not redirected to content page.'


@mark.regression
def test_check_price_not_empty_for_product_item(open_product_item_page):
    product_item = open_product_item_page
    price_value = product_item.check_presence_price_set()
    assert len(str(price_value)) > 0 and price_value != 0.0, \
        'Something went wrong. Not able to verify price for product.'


@mark.regression
def test_open_shopping_bag_page_from_product_item(open_product_item_page):
    product_item = open_product_item_page
    product_item.click_shopping_bag()
    assert product_item.check_presence_location_shopping_container(), \
        'Something went wrong. User not redirected to shopping bag.'
