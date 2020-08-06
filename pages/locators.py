from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_USERNAME_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_USERNAME_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.XPATH, "//*[@id='register_form']/button")
    USED_IS_LOGINED = (By.XPATH, "//*[@id='top_page']/div[2]/div/ul/li[1]/a")
    URL = (By.LINK_TEXT, "http://selenium1py.pythonanywhere.com/uk/accounts/login/")

class ProductPageLocators():
    ADD_BUTTON = (By.XPATH,"//*[@id='add_to_basket_form']/button")
    MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ICON = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
    MESSEAGE_BASKET_EMPTY = (By.XPATH, "//*[@id='content_inner']/p")
    MESSEAGE_BASKET_WITHOUT_BOOKS = (By.XPATH, "//*[@id='basket_formset']/div/div")