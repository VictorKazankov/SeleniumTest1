from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def open_change_number_guests_panel(self):
        guests_number_toggle = self.get_element_present(*MainPageLocators.GUESTS_NUMBER_FIELD_TOGGLE)
        guests_number_toggle.click()

    def increase_number_children(self):
        plus_button = self.get_element_present(*MainPageLocators.PLUS_NUMBER_CHILDREN_BUTTON)
        plus_button.click()

    def is_displayed_age_child_input(self):
        #############??????#############
        age_child_input = Select(self.get_element_present(*MainPageLocators.AGE_CHILD_INPUT))

    def is_value_age_child_by_defult(self):
        age_child_input = Select(self.get_element_present(*MainPageLocators.AGE_CHILD_INPUT))
        assert age_child_input.first_selected_option.text

    def count_age_child_inputs(self, count_children):
        count_input = len(MainPageLocators.COUNT_AGE_CHILD_INPUT)
        assert count_input == count_children

    def open_bukovel_hotel_list(self):
        bukovel_small_postcard = self.get_element_present(*MainPageLocators.BUKOVEL_SMALL_POSTCARD)
        bukovel_small_postcard.click()
