from HW17.utilities.config_reader import get_valid_user_data, get_invalid_user_data, get_blocked_user_data
from pytest import mark


@mark.regression
def test_warning_on_login_with_empty_inputs(open_login_page):
    login_page = open_login_page
    login_page.click_login_button()
    assert login_page.check_presence_of_warning_empty_inputs(), \
        '"Username is required" warning is not displayed.'


@mark.regression
def test_warning_on_login_with_empty_password(open_login_page):
    login_page = open_login_page
    login_page.enter_username_to_input(get_valid_user_data()[0]).click_login_button()
    assert login_page.check_presence_of_warning_empty_password(), \
        '"Password is required" warning is not displayed.'


@mark.regression
def test_warning_on_login_with_empty_username(open_login_page):
    login_page = open_login_page
    login_page.enter_password_to_input(get_valid_user_data()[1]).click_login_button()
    assert login_page.check_presence_of_warning_empty_username(), \
        '"Username is required" warning is not displayed.'


@mark.smoke
@mark.regression
def test_warning_on_login_with_invalid_username(open_login_page):
    login_page = open_login_page
    login_page.enter_username_to_input(get_invalid_user_data()[0]).enter_password_to_input(
        get_valid_user_data()[1]).click_login_button()
    assert login_page.check_presence_of_warning_wrong_creds(), \
        '"Username and password do not match any user in this service" warning is not displayed.'


@mark.smoke
@mark.regression
def test_warning_on_login_with_invalid_password(open_login_page):
    login_page = open_login_page
    login_page.enter_username_to_input(get_valid_user_data()[0]).enter_password_to_input(
        get_invalid_user_data()[1]).click_login_button()
    assert login_page.check_presence_of_warning_wrong_creds(), \
        '"Username and password do not match any user in this service" warning is not displayed.'


@mark.regression
def test_warning_on_login_with_blocked_user(open_login_page):
    login_page = open_login_page
    login_page.enter_username_to_input(get_blocked_user_data()).enter_password_to_input(
        get_valid_user_data()[1]).click_login_button()
    assert login_page.check_presence_of_warning_blocked_user(), \
        '"Sorry, this user has been locked out." warning is not displayed.'


@mark.smoke
@mark.regression
def test_success_login(open_login_page):
    login_page = open_login_page
    main_page = login_page.enter_username_to_input(get_valid_user_data()[0]).enter_password_to_input(
        get_valid_user_data()[1]).click_login_button()
    assert main_page.check_presence_location_content_page(), \
        'Something went wrong. User not logged in.'
