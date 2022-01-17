from time import sleep

from selenium.webdriver.common.by import By

from Pages.base import BasePage
from Pages.utils import wait_until_ok
from constants.add_to_cart import AddToCartConstants


class AddToCart(BasePage):
    """Позитивный тест на проверку добавления товара в корзину:
    - заходим на сайт
    - выбираем категорию товаров Woman
    - в категории выбираем товар
    - переходим на его страницу
    - меняем фильтры: цвет товара, колличество...
    - добавляем товар в корзину
    - проверяем корзину на наличие текущих товаров"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.constants = AddToCartConstants

    def woman_category(self):
        # открываем категорию женских товаров
        woman_category = self.wait_until_find_element(value=self.constants.WOMAN_CATEGORY_XPATH)
        woman_category.click()

    def woman_choice(self):
        # находим определенный товар (Faded Short Sleeve T-shirts)
        woman_tshirt = self.wait_until_find_element(value=self.constants.WOMAN_TSHIRT_TITLE_XPATH)
        woman_tshirt.click()

    def check_filters(self):
        # увеличиваем количество товаров до 2-х
        woman_tshirt_add_quanity = self.wait_until_find_element(value=self.constants.WOMAN_TSHIRT_ADD_QUANITY_XPATH)
        woman_tshirt_add_quanity.click()

        # выбираем другой цвет товара
        woman_tshirt_change_color = self.wait_until_find_element(value=self.constants.WOMAN_TSHIRT_CHANGE_COLOR_XPATH)
        woman_tshirt_change_color.click()

    def confirm_adding(self):
        add_items_in_cart = self.wait_until_find_element(value=self.constants.WOMAN_TSHIRT_ADD_TO_CARD_XPATH)
        add_items_in_cart.click()
        sleep(3)

        confirm_add = self.wait_until_find_element(value=self.constants.WOMAN_TSHIRT_CONFIRM_XPATH)
        confirm_add.click()
        # проверяем, что в корзине лежат выбранные товары

    def check_cart(self):
        woman_tshirt_check_cart = self.wait_until_find_element(value=self.constants.WOMAN_TSHIRT_CHECK_CART_XPATH)
        woman_tshirt_check_cart.is_displayed()

        # проверяем, что количество товаров действительно 2
        woman_tshirt_check_count = self.wait_until_find_element(value=self.constants.WOMAN_T_CART_CHECK_COUNT_ITMES_XPATH)
        woman_tshirt_check_count.is_selected()

