from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def click_on_bucket(self):
        login_link = self.browser.find_element(*BasketPageLocators.BASKET_ICON)
        login_link.click()

    def should_be_empty_messaege(self):
        assert self.is_element_present(*BasketPageLocators.MESSEAGE_BASKET_EMPTY), "Basket with books"

    def should_be_without_books(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSEAGE_BASKET_WITHOUT_BOOKS), \
            "With Books"