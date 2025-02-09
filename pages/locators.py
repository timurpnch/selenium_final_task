from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ALERTS = (By.CSS_SELECTOR, ".alertinner strong")
    MAIN_NAME = (By.CSS_SELECTOR, ".product_main h1")
    MAIN_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESAGES = (By.CSS_SELECTOR, ".alert-success")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
