from .base_page import Basepage
from .locators import ProductPageLocators


class ProductPage(Basepage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button is not presented"

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def same_names_of_products(self):
        name_in_alert = self.browser.find_elements(*ProductPageLocators.ALERTS)[0].text
        main_name = self.browser.find_element(*ProductPageLocators.MAIN_NAME).text
        assert name_in_alert == main_name, \
            "The product name in the message must match the product that was actually added"

    def same_prices_of_products(self):
        price_in_alert = self.browser.find_elements(*ProductPageLocators.ALERTS)[2].text
        main_price = self.browser.find_element(*ProductPageLocators.MAIN_PRICE).text
        assert price_in_alert == main_price, \
            "The basket value must match the product price"

    def guest_cant_see_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESAGES), \
            "The success message should not be shown"

    def guest_cant_see_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESAGES), \
            "The success message should not be shown"
