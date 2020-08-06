import time

from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
import math
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_book_in_bucket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        login_link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_login_url(self):
        messeage = self.browser.find_element(*ProductPageLocators.MESSAGE)
        assert "has been added to your basket." in messeage.text , "'login' not in current url"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE), \
            "Success message is presented, but should not be"

    def should_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE), \
            "Success message is presented, and not dissapered"