def test_booking_price_by_booking_date(search_page):
    search_page.should_be_bukovel_result_page()
    search_page.should_be_visible_booking_calendar()
    search_page.should_not_be_booking_price_and_booking_status()


def test_visibly_calendar_after_click_show_price_button(search_page):
    search_page.click_price_button()
    search_page.should_be_visible_booking_calendar()


def test_present_hotel_price_after_run_searching(search_page):
    search_page.click_price_button()
    search_page.choose_booking_data()
    search_page.click_search_button()
    search_page.is_prices_for_every_result_items()
