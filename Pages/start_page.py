import logging
from time import sleep

from selenium.webdriver.common.by import By

from Pages.base import BasePage
from Pages.utils import wait_until_ok
from constants.start_page import StartPageConstants


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants

    def login(self, email_value, password_value):
        """Логиниться, используя предложенные емеил и пароль"""
        # открываем поле email и очищаем строку ввода
        self.fill_fields(locator=self.constants.SIGN_IN_EMAIL_XPATH, value=email_value)
        self.fill_fields(locator=self.constants.SIGN_IN_PASSWORD_XPATH, value=password_value)
        self.log.debug("Fields are filled with invalid values")

        # Нажимаем Sign In для входа
        sign_in_confirm = self.wait_until_find_element(value=self.constants.SIGN_IN_CONFIRM_BUTTON_XPATH)
        sign_in_confirm.click()
        self.log.debug("Clicked on Sign in")

    def verify_incorrect_login(self):
        """Проверка еррор-месседжа"""
        # проверка наличия ошибки посредством появления сообщения об ошибке
        error = self.wait_until_find_element(value=self.constants.SIGN_IN_ERROR)
        error.is_displayed()

    @wait_until_ok()
    def sign_out_button(self):
        # потвержжение успешного входа появлением кнопки Sign out
        sign_out_button = self.wait_until_find_element(value=self.constants.SIGN_OUT_BUTTON_XPATH)
        sign_out_button.is_enabled()
