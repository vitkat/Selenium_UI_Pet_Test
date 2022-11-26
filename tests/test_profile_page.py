import time

import pytest

from pages.profile_page import ProfilePage
from tests.test_login_page import test_go_to_login


def test_click_edit_jmih(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.click_edit_jmih()
    time.sleep(2)
    # browser.save_screenshot('resultClickEditJmih.png')


@pytest.mark.smoke
def test_add_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.add_pet()
    time.sleep(1)
    page.name_add_pet()
    time.sleep(1)
    page.type_add_pet()
    time.sleep(1)
    page.type_add_pet_1()
    time.sleep(1)
    page.age_add_pet()
    time.sleep(1)
    page.gender_add_pet()
    time.sleep(1)
    page.female_add_pet()
    time.sleep(1)
    page.submit_add_pet()
    time.sleep(1)
    # browser.save_screenshot('resultAddPet.png')


@pytest.mark.skip
def test_delete_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.delete_pet()
    time.sleep(1)
    page.delete_yes()
    time.sleep(1)
    # browser.save_screenshot('resultDeletePet.png')


@pytest.mark.smoke
def test_button_logo(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.button_logo()
    time.sleep(3)
    # browser.save_screenshot('resultButtonLogo.png')


@pytest.mark.skip
def test_button_quit(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.button_quit()
    time.sleep(2)
