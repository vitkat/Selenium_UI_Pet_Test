from selenium.webdriver import Keys
from .locators import MainPageLocators, LoginPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_filter_type(self):
        filter_by_type = self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE)
        filter_by_type.click()

    def go_to_filter_by_cat(self):
        filter_by_cat = self.browser.find_element(*MainPageLocators.FILTER_BY_CAT)
        filter_by_cat.click()

    def go_to_filter_by_name(self):
        filter_by_name = self.browser.find_element(*MainPageLocators.FILTER_BY_NAME)
        filter_by_name.send_keys('Thor')
        filter_by_name.send_keys(Keys.RETURN)

    def go_to_filter_name_thor(self):
        filter_name_thor = self.browser.find_element(*MainPageLocators.FILTER_BY_NAME)
        filter_name_thor.send_keys('Thor')
        filter_name_thor.send_keys(Keys.RETURN)
        filter_name_thor = self.browser.find_element(*MainPageLocators.FILTER_NAME_THOR)
        filter_name_thor.click()

    def go_to_like_thora(self):
        like_thora = self.browser.find_element(*MainPageLocators.FILTER_BY_NAME)
        like_thora.send_keys('Thora')
        like_thora.send_keys(Keys.RETURN)
        like_thora = self.browser.find_element(*MainPageLocators.LIKE_THORA).click()

    def go_paginator_page(self):
        go_paginator_page = self.browser.find_element(*MainPageLocators.PAGINATOR_PAGE_1)
        go_paginator_page.click()

    def go_paginator_page_1(self):
        go_paginator_page_1 = self.browser.find_element(*MainPageLocators.PAGINATOR_PAGE_2)
        go_paginator_page_1.click()

    def go_paginator_page_2(self):
        go_paginator_page_2 = self.browser.find_element(*MainPageLocators.PAGINATOR_PAGE_3)
        go_paginator_page_2.click()

    def comment_thor(self):
        comment_thor = self.browser.find_element(*MainPageLocators.FILTER_BY_NAME)
        comment_thor.send_keys('Thor')
        comment_thor.send_keys(Keys.RETURN)
        comment_thor = self.browser.find_element(*MainPageLocators.FILTER_NAME_THOR)
        comment_thor.click()
        comment_thor_2 = self.browser.find_element(*MainPageLocators.COMMENT_THOR)
        comment_thor_2.send_keys('CooL BRO!')
        comment_thor_3 = self.browser.find_element(*MainPageLocators.COMMENT_SAVE)
        comment_thor_3.click()

    def go_login_exit(self):
        go_login_exit = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        go_login_exit.click()
        go_login_exit = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        go_login_exit.send_keys('bubka@mail.ru')
        go_login_exit = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        go_login_exit.send_keys('5566220vint95')
        go_login_exit = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        go_login_exit.submit()
        go_login_exit = self.browser.find_element(*MainPageLocators.LOGIN_EXIT)
        go_login_exit.click()