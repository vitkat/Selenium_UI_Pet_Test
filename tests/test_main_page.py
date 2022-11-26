import time

import pytest

from pages.main_page import MainPage
from tests.test_login_page import test_go_to_login


@pytest.mark.skip
def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(2)
    # browser.save_screenshot('resultloginpage.png')


@pytest.mark.regression
def test_go_to_filter_type(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_type()
    page.go_to_filter_by_cat()
    time.sleep(2)
    # browser.save_screenshot('resultCatFilter.png')


@pytest.mark.smoke
def test_go_to_filter_by_name(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_name()
    time.sleep(2)
    # browser.save_screenshot('resultFilterName.png')


@pytest.mark.regression
@pytest.mark.smoke
def test_to_filter_name_thor(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_name()
    time.sleep(2)
    page.open()
    page.go_to_filter_name_thor()
    time.sleep(2)
    # browser.save_screenshot('resultFilterNameThor.png')


@pytest.mark.regression
def test_go_to_like_thora(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_name()
    time.sleep(2)
    page.open()
    page.go_to_like_thora()
    time.sleep(2)
    # browser.save_screenshot('resultFilterNameThor.png')


@pytest.mark.skip
def test_go_paginator_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_paginator_page()
    time.sleep(2)
    page.open()
    page.go_paginator_page_1()
    time.sleep(2)
    page.open()
    page.go_paginator_page_2()
    time.sleep(2)
    # browser.save_screenshot('resultPaginatorPage.png')


@pytest.mark.regression
def test_comment_thor(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.comment_thor()
    time.sleep(2)
    # browser.save_screenshot('resultCommentThor.png')


@pytest.mark.smoke
def test_go_login_exit(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_login_exit()
    time.sleep(1)
# browser.save_screenshot('resultCommentThor.png')


# pytest -v test_main_page.py -- команда для запуска теста с терминала
