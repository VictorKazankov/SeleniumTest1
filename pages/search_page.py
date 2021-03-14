from pages.base_page import BasePage
from pages.locators import SearchPageLocators


class SearchPage(BasePage):
    def should_be_bukovel_result_page(self):
        search_result = self.get_element_present(*SearchPageLocators.SEARCH_RESULT)
        text_search_result = search_result.text
        assert 'Буковель' in text_search_result

    def should_be_visible_booking_calendar(self):
        assert self.get_element_present(*SearchPageLocators.BOOKING_CALENDAR)

    def should_not_be_booking_price_and_booking_status(self):
        assert self.element_not_present(*SearchPageLocators.PRICE_BOOKING)

    def click_price_button(self):
        price_button = self.get_element_present(*SearchPageLocators.SHOW_PRICE_BUTTON)
        # verify that booking calendar isn't visible
        if not self.get_element_present(*SearchPageLocators.BOOKING_CALENDAR):
            price_button.click()
        else:
            # if cooking calendar is visible to click search result
            search_result = self.get_element_present(*SearchPageLocators.SEARCH_RESULT)
            search_result.click()
            price_button.click()

    def choose_booking_data(self):
        data_start = self.get_element_present(*SearchPageLocators.DATA_BOOKING)
        data_start.click()

    def click_search_button(self):
        search_button = self.get_element_present(*SearchPageLocators.SEARCH_BUTTIN)
        search_button.click()

    def is_prices_for_every_result_items(self):
        hotel_list = self.get_elements_present(*SearchPageLocators.HOTEL_RESULT_ITEMS)
        for item in range(len(hotel_list)):
            assert 'UAH' in hotel_list[item].text