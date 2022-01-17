class StartPageConstants:

    SIGN_IN_BUTTON_XPATH = ".//a[@href='http://automationpractice.com/index.php?controller=my-account'and @class='login']"
    SIGN_IN_EMAIL_XPATH = ".//input[@name='email' and @data-validate='isEmail']"
    SIGN_IN_PASSWORD_XPATH = ".//input[@id='passwd']"
    SIGN_IN_CONFIRM_BUTTON_XPATH = ".//button[@id='SubmitLogin']"
    SIGN_OUT_BUTTON_XPATH = ".//*[@title='Log me out']"

    SIGN_IN_ERROR = ".//div[@class='alert alert-danger' and p='There is 1 error']"
    SIGN_IN_ERROR_MESSAGE_TEXT = "There is 1 error"
