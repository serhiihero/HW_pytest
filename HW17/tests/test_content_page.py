from pytest import mark


@mark.smoke
@mark.regression
def test_actions_menu_opens_from_content_page(open_actions_menu):
    actions_menu = open_actions_menu
    assert actions_menu.check_presence_of_actions_menu(), \
        'Something went wrong. Actions menu not opened.'


@mark.smoke
@mark.regression
def test_user_logout_from_content_page(open_content_page):
    content_page = open_content_page
    logout_action = content_page.click_hamburger_button().click_logout_button()
    assert logout_action.check_presence_location_login_page(), \
        'Something went wrong. User is not logged out.'


@mark.smoke
@mark.regression
def test_shopping_bag_opens_from_content_page(open_shopping_bag):
    shopping_bag = open_shopping_bag
    assert shopping_bag.check_presence_location_shopping_bag_container(), \
        'Something went wrong. User not redirected to shopping bag.'


@mark.smoke
@mark.regression
def test_product_item_opens_from_content_page(open_product_item_page):
    product_item_page = open_product_item_page
    assert product_item_page.check_presence_location_product_container(), \
        'Something went wrong. Product item is not opened.'


@mark.smoke
@mark.regression
def test_product_item_adds_to_bag_from_content_page(open_content_page):
    content_page = open_content_page
    shopping_bag = content_page.click_add_to_bag_product_item().click_shopping_bag()
    assert shopping_bag.check_presence_product_in_bag(), \
        'Something went wrong. Product item not added to bag.'
