from selenium.webdriver.common.by import By


class MainPageLocators:
    GUESTS_NUMBER_FIELD_TOGGLE = (By.ID, "xp__guests__toggle")
    PLUS_NUMBER_CHILDREN_BUTTON = (By.XPATH, "//button[@aria-describedby='group_children_desc']/span[text()='+']")
    AGE_CHILD_INPUT = (By.XPATH, "//select[@name='age']")
    COUNT_AGE_CHILD_INPUT = (By.XPATH, "count(//select[@name='age'])")
    BUKOVEL_SMALL_POSTCARD = (By.XPATH, "//div[@class='promotion-postcard__small'][last()]")


class SearchPageLocators:
    SEARCH_RESULT = (By.XPATH, "//h1[@class='sorth1']")
    BOOKING_CALENDAR = (By.XPATH, "//div[@class='bui-calendar']")
    PRICE_BOOKING = (By.XPATH, "//div[@class='prco-inline-block-maker-helper']")
    SHOW_PRICE_BUTTON = (By.XPATH, "//div[@class='sr-cta-button-row sr-cta-button-top-spacing']/*[1]")
    DATA_BOOKING = (By.XPATH, "//td[@class='bui-calendar__date']")
    DATA_BOOKING_FINISH = (By.XPATH, "//td[@class='bui-calendar__date'][2]")
    SEARCH_BUTTIN = (By.XPATH, "//button[@data-sb-id='main']")
    HOTEL_RESULT_ITEMS = (By.XPATH, "//div[@id='hotellist_inner']//"
                                    "div[@class='bui-price-display__value prco-inline-block-maker-helper ']")
