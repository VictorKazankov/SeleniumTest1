from pages.main_page import MainPage
from pages.search_page import SearchPage

main_page_url = "https://www.booking.com/"


def test_user_able_specify_age_for_one_child(browser):
    main_page = MainPage(browser, main_page_url)
    main_page.open()
    main_page.open_change_number_guests_panel()
    main_page.increase_number_children()
    main_page.is_displayed_age_child_input()
    main_page.is_value_age_child_by_defult()


def test_user_able_specify_age_for_several_child(browser):
    # set up count child here
    count_children = 4
    main_page = MainPage(browser, main_page_url)
    main_page.open()
    main_page.open_change_number_guests_panel()
    for child in range(count_children):
        main_page.increase_number_children()
    main_page.count_age_child_inputs(count_children)


def test_booking_price_by_booking_date(browser):
    main_page = MainPage(browser, main_page_url)
    main_page.open()
    main_page.open_bukovel_hotel_list()
    search_page = SearchPage(browser, browser.current_url)
    search_page.should_be_bukovel_result_page()
    search_page.should_be_visible_booking_calendar()
    search_page.should_not_be_booking_price_and_booking_status()


def test_visibly_calendar_after_click_show_price_button(browser):
    main_page = MainPage(browser, main_page_url)
    main_page.open()
    main_page.open_bukovel_hotel_list()
    search_page = SearchPage(browser, browser.current_url)
    search_page.click_price_button()
    search_page.should_be_visible_booking_calendar()


def test_present_hotel_price_after_run_searching(browser):
    main_page = MainPage(browser, main_page_url)
    main_page.open()
    main_page.open_bukovel_hotel_list()
    search_page = SearchPage(browser, browser.current_url)
    search_page.click_price_button()
    search_page.choose_booking_data()
    search_page.click_search_button()
    search_page.is_prices_for_every_result_items()
