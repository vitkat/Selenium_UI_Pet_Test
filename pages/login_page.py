
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('bubka@mail.ru')

    def go_to_pass(self):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys('5566220vint95')

    def go_to_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_button.submit()
