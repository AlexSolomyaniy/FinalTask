from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/" in self.browser.current_url, "'login' not in current url"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME_FIELD), "Login field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELD), "Password field is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_USERNAME_FIELD), "Registration login field is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD_FIELD), "Registration password field is not presented"
        assert self.is_element_present(
            *LoginPageLocators.CONFIRM_PASSWORD_FIELD), "Confirm password field is not presented"
