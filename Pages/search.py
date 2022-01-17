
from Pages.base import BasePage
from constants.add_to_cart import AddToCartConstants
from constants.search import SearchConstants


class Search(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.constants = SearchConstants

        # открываем категорию женских товаров

    """Проверка работоспособности поиска
    - находим поле поиска
    - заполняем поле поиска
    - нажимаем кнопку-лупу Поиск
    - подверждаем, что поиск рабочий"""

    def search_field_empty(self):
        # находим поле для ввода, оставляем пустым и нажимаем кнопку Поиск
        search_button = self.wait_until_find_element(value=self.constants.SEARCH_CONFIRM_LUPA_XPATH)
        search_button.click()

        # проверяем, что на странице результата поиска появилась ошибка о незаполненном поле поиска
        confirm_search = self.wait_until_find_element(value=self.constants.SEARCH_ERROR_MESSAGE_EMPTY_XPATH)
        assert confirm_search.text == self.constants.SEARCH_EMPTY_TEXT

    def search_field_valid(self):
        # находим поле для ввода в поиск и вводим значение "дресс"
        self.fill_fields(locator=self.constants.SEARCH_FIELD_XPATH, value="dress")
        # подтверждаем введенный поиск, нажав на кнопку Поиск
        search_button = self.wait_until_find_element(value=self.constants.SEARCH_CONFIRM_LUPA_XPATH)
        search_button.click()
        # подтверждаем, что найден минимум 1 элемент, со словом Dress
        dress_result = self.wait_until_find_element(value=self.constants.SEARCH_DRESS_RESULT_XPATH)
        dress_result.is_displayed()

