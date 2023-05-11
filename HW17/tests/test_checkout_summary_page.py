from pytest import mark


@mark.smoke
@mark.regression
def test_user_can_cancel_checkout(open_checkout_page):
    checkout_page = open_checkout_page
    user_data = checkout_page.enter_user_data_to_inputs()
    checkout_summary_page = user_data.click_continue_button()
    click_cancel_button = checkout_summary_page.click_cancel_button()
    assert click_cancel_button.check_presence_location_content_page(), 'Something went wrong. Not able to cancel order.'
