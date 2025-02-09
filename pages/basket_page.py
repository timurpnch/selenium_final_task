from .base_page import Basepage
from .locators import BasketPageLocators


class BasketPage(Basepage):
    def no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_HEADER), \
            'The basket is not empty'

    def guest_can_see_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            'There is no empty basket text'
