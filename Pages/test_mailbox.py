from Pages.base import BasePage
from constants.newsletter import NewsletterConstants


class MailBox(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = NewsletterConstants

    def sign_in(self):
        button_post = self.wait_until_find_element(value=self.constants.GOOGLE_POST_XPATH)
        button_post.click()




