from Pages.base import BasePage
from constants.newsletter import NewsletterConstants


class Newsletter(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = NewsletterConstants

    def invalid_email(self):
        """Логиниться, используя предложенный емеил"""
        # открываем поле email и очищаем строку ввода
        self.fill_fields(locator=self.constants.NEWSLETTER_INPUT_XPATH, value="fsdfsdffs")
        self.log.debug("Fields are filled with invalid values")
        button_ok = self.wait_until_find_element(value=self.constants.NEWSLETTER_BUTTON_OK_XPATH)
        button_ok.click()

    def valid_email(self):
        """Логиниться, используя предложенный инвалидный емеил"""
        self.fill_fields(locator=self.constants.NEWSLETTER_INPUT_XPATH, value="onesupon@gmail.com")
        button_ok = self.wait_until_find_element(value=self.constants.NEWSLETTER_BUTTON_OK_XPATH)
        button_ok.click()

