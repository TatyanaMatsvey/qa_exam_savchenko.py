import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.log = logging.getLogger(__name__)
        self.wait = WebDriverWait(driver, timeout=10)

    def fill_fields(self, locator, value, by=By.XPATH):
        """Заполняем поля используя предоставленные данные"""
        email = self.wait_until_find_element(by=by, value=locator)
        email.clear()
        email.send_keys(value)

    def wait_until_find_element(self, value, by=By.XPATH):
        """Ожидание, пока найдется элемент"""
        return self.wait.until(EC.presence_of_element_located(locator=(by, value)))

    def wait_until_element_enabled(self, value, by=By.XPATH):
        """Ожидание, пока жлемент не станет кликабелен"""
        element = self.wait_until_element_enabled(by=by, value=value)
        return self.wait.until(EC.element_to_be_clickable(element))
