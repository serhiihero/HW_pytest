from pytest import mark


@mark.regression
def test_product_item_opening_from_shopping_bag(open_content_page):
    content_page = open_content_page
    product_item = content_page.click_add_to_bag_product_item().click_shopping_bag().click_product_item()
    assert product_item.check_presence_location_product_container(), \
        'Something went wrong. Product item is not opened from the shopping bag.'


@mark.smoke
@mark.regression
def test_product_item_can_be_removed_from_shopping_bag(open_content_page):
    content_page = open_content_page
    shopping_bag = content_page.click_add_to_bag_product_item().click_shopping_bag().click_remove_product_item_from_shopping_bug()
    assert shopping_bag.check_bag_is_empty(), \
        'Something went wrong. Not able to verify items in bag.'


@mark.regression
def test_actions_menu_opens_from_shopping_bag(open_shopping_bag):
    shopping_bag = open_shopping_bag
    shopping_bag.click_hamburger_button()
    assert shopping_bag.check_presence_of_actions_menu(), \
        'Something went wrong. Actions menu not opened.'


@mark.regression
def test_continue_shopping_button_is_clickable(open_shopping_bag):
    shopping_bag = open_shopping_bag
    content_page = shopping_bag.click_continue_shopping_button()
    assert content_page.check_presence_location_content_page(), \
        'Something went wrong. Catalog of products not fetched.'


@mark.smoke
@mark.regression
def test_checkout_page_opens_from_shopping_bag(open_shopping_bag):
    shopping_bag = open_shopping_bag
    checkout_page = shopping_bag.click_checkout_button()
    assert checkout_page.check_presence_location_checkout_page(), \
        'Something went wrong. User not redirected to checkout page.'
