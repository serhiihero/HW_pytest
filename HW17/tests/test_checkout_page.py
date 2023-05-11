from pytest import mark


@mark.regression
def test_user_can_not_proceed_with_empty_inputs(open_checkout_page):
    checkout_page = open_checkout_page
    checkout_page.click_continue_button()
    assert checkout_page.check_presence_error_state(), \
        'Something went wrong. Error state not returned.'


@mark.regression
def test_user_can_open_shopping_bag_from_checkout_page(open_checkout_page):
    checkout_page = open_checkout_page
    click_back_button = checkout_page.click_back_button()
    assert click_back_button.check_presence_location_shopping_bag_container(), \
        'Something went wrong. User not redirected to shopping bag.'


@mark.smoke
@mark.regression
def test_user_can_proceed_success_with_data_for_purchase(open_checkout_page):
    checkout_page = open_checkout_page
    user_data = checkout_page.enter_user_data_to_inputs()
    checkout_summary_page = user_data.click_continue_button()
    assert checkout_summary_page.check_presence_location_checkout_summary_page(), \
        'Something went wrong. User not redirected to checkout summary page.'


@mark.regression
def test_user_can_return_to_shopping_bag_from_checkout_page(open_checkout_page):
    checkout_page = open_checkout_page
    shopping_bag = checkout_page.click_back_button()
    assert shopping_bag.check_presence_location_shopping_bag_container(), \
        'Something went wrong. User not redirected to shopping bag.'


@mark.regression
def test_user_can_open_actions_menu_from_checkout_page(open_checkout_page):
    checkout_page = open_checkout_page
    checkout_page.click_hamburger_button()
    assert checkout_page.check_presence_of_actions_menu(), \
        'Something went wrong. Actions menu not opened.'
