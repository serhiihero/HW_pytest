# Find web page.
# Write 30 XPATH locators for this page using XPath Axes and Wildcards. Some of them should have more than 3 steps.
# For 10 XPATH locators write 10 CSS locators which find the same element
import time
from selenium.webdriver import Chrome


def test_locators_finder():
    driver_chrome = Chrome('chromedriver.exe')
    driver_chrome.maximize_window()
    driver_chrome.get('https://www.w3schools.com/')
    time.sleep(500)

    # logo
    logo = "//div[@class='w3-bar w3-card-2 notranslate w3-white']/a[@title='Home']/i[@class='fa fa-logo']"
    # login button
    login_btn = "//div[@id='loginactioncontainer']/a[@title='Login to your account']"
    # learn how to button at the bottom of the page
    learn_how_to_btn = "//a[@href='/howto/default.asp' and " \
                       "@class='w3-button tut-button ws-black w3-padding-16 w3-mobile vl-howtobtn']"
    # small search button
    small_search_btn = "//a[@id='nav_search_btn']"
    # copyright button
    copyright_btn = "//footer/p/a[text()='Copyright 1999-2023']"
    # get started button at kickstart your career block
    get_started_btn = "//div[@id='getdiploma']/child::a"
    forum_btn = "//nav[@class='w3-right w3-hide-medium w3-hide-small w3-wide']/a[@title='Forum']"

    # //ancestors//
    # header
    header = "//i[@class='fa fa-logo']/ancestor::div[@class='w3-bar w3-card-2 notranslate w3-white']"
    # learn to code block
    first_block_on_start = "//input[@type='text']/ancestor::div[@class='ws-black w3-center']"
    # main block of three small button at the top right
    three_top_right_buttons_block = "//a[@id='nav_search_btn']" \
                                    "/ancestor::div[@class='w3-right ws-black ext_icon_container']"

    # //child//
    # tutorials arrow
    arrow_for_tutorials_drop_down_list = "//div[@class='w3-bar w3-card-2 notranslate w3-white']" \
                                         "/a[@id='navbtn_tutorials']//child::*[@class='fa fa-caret-down']"
    # footer button "Quizzes"
    first_btn_of_footer = "//footer/div[@class='w3-container w3-padding-32']/child::a[@title='Quizzes'][1]"

    second_btn_of_python_learn_block = "//a[@href='/python/python_reference.asp']" \
                                       "/parent::div[@class='w3-col l6 w3-center']"

    # //parent//
    # learn python block
    learn_python_block = "//a[@class='w3-button tut-button']/parent::div"
    # exercises and quizzes block
    block_of_exercises_quizzes = "//div[@class='w3-row-padding w3-content']" \
                                 "/parent::div[@class='w3-center w3-padding-64 ws-black']"
    # popular topics block
    block_of_popular_topics = "//div[@class='w3-col l6 s12 w3-center']/parent::div/parent::div"

    # //following//
    # upgrade button on the header
    upgrade_btn = "//a[@id='cert_navbtn']/following::*"
    # color picker block
    color_picker_block = "//div[@class='pro-caption ws-black']/following::div[@class='w3-center']"
    # dynamic spaces gif
    dynamic_spaces_gif = "//div[@class='ws-black w3-center']/following::img[@src='/spaces/dynamicspaces.gif']"
    # find active dot on iframe
    active_dot = "//div[@class='slideshow-container']/following::div/span[@class='dot active']"

    # //XPATH + CSS locators//
    root_webpage_xpath = "//html[@lang='en-US']"
    root_webpage_css = ":root[lang='en-US']"
    search_btn_xpath = "//button[@id='learntocode_searchbtn']"
    search_btn_css = "#learntocode_searchbtn"
    search_btn_xpath = "//a[@id='nav_search_btn']"
    search_btn_css = "[title='Search W3Schools']"
    learn_to_code_title_xpath = "//div[@class='w3-content learntocodecontent']/h1"
    learn_to_code_title_css = "[class='w3-content learntocodecontent'] > h1"
    gif_w3schools_spaces_xpath = "//img[@src='/spaces/dynamicspaces.gif']"
    gif_w3schools_spaces_css = "[src='/spaces/dynamicspaces.gif']"
    instagram_btn_xpath = "//a[@title='W3Schools on Instagram']"
    instagram_btn_css = "[title='W3Schools on Instagram']"
    second_small_dot_xpath = "//span[@class='dot']//following::span"
    second_small_dot_css = "[class='dot'] + span"
    send_feedback_btn_xpath = "//a[@title='Like W3Schools on Facebook']//following::i"
    send_feedback_btn_css = "[title='Like W3Schools on Facebook'] > i"
    try_frontend_btn_xpath = "//div[@class='w3-content w3-padding']/a[@href='/tryit/tryit.asp?filename=tryhtml_hello']"
    try_frontend_btn_css = "[class='w3-content w3-padding'] > a[href='/tryit/tryit.asp?filename=tryhtml_hello']"
    logo_link_btn_xpath = "//div[@class='w3-bar w3-card-2 notranslate w3-white']" \
                          "/a[@class='w3-bar-item w3-button w3-hover-none w3-left w3-padding-16']"
    logo_link_btn_css = "[class='w3-bar w3-card-2 notranslate w3-white']" \
                        " > a[class='w3-bar-item w3-button w3-hover-none w3-left w3-padding-16']"
