

import pytest
from selenium.webdriver.chrome import webdriver

from Pages.add_to_cart import AddToCart
from Pages.newsletter import Newsletter
from Pages.search import Search
from Pages.start_page import StartPage
from Pages.test_mailbox import MailBox
from constants.add_to_cart import AddToCartConstants
from constants.base import BaseConstants
from constants.newsletter import NewsletterConstants
from constants.search import SearchConstants


class TestStartPage:

    @pytest.fixture(scope="function")
    def driver(self):
        """Создает драйвер, возвращает и закрывает его после теста"""
        driver = webdriver.WebDriver(BaseConstants.DRIVER_PATH)
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def start_page(self, driver):
        """Возращает start page object"""
        driver.get(BaseConstants.URL)
        return StartPage(driver)

    @pytest.fixture(scope="function")
    def adding_to_cart(self, driver):
        driver.get(AddToCartConstants.URL)
        return AddToCart(driver)

    @pytest.fixture(scope="function")
    def searching(self, driver):
        driver.get(SearchConstants.URL)
        return Search(driver)

    @pytest.fixture(scope="function")
    def newsletters(self, driver):
        driver.get(NewsletterConstants.URL)
        return Newsletter(driver)


    def test_login(self, start_page):
        """Авторизация на сайте с валидными данными """
        start_page.login("macvejs@gmail.com", "TeslaJoule")
        start_page.sign_out_button()

    def test_invalid_login(self, start_page):
        """Авторизация на сайте с инвалидными данными"""
        # заполнение полей валидными данными
        start_page.login("desd", "cdcdfds")
        start_page.verify_incorrect_login()

    def test_adding_to_cart(self, adding_to_cart):
        """Добавление товара в корзину:
        - открыть магазин
        - выбрать товар
        - добавить в корзину
        - изменить цвет, количество
        - проверить товары в корзине"""
        adding_to_cart.woman_category()
        adding_to_cart.woman_choice()
        adding_to_cart.check_filters()
        adding_to_cart.confirm_adding()
        adding_to_cart.check_cart()

    def test_search(self, searching):
        """Проверка поля поиска
        - с инвалидными данными
        - с валидным значением"""

        searching.search_field_empty()
        searching.search_field_valid()

    def test_newsletter(self, newsletters):
        """Проверка поля новостей
        - с инвалидными данными
        - с валидным значением"""

        newsletters.invalid_email()
        newsletters.valid_email()










