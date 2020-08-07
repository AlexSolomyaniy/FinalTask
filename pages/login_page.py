from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def register_new_user(self,email,password):
        name = self.browser.find_element(*LoginPageLocators.REGISTRATION_USERNAME_FIELD)
        password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        confirm = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        password1.send_keys(password)
        confirm.send_keys(password)
        name.send_keys(email)
        button.click()

    def should_be_logined(self):
        assert self.is_element_present(*LoginPageLocators.USED_IS_LOGINED),"Not Logined"

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
