from .base_page import BasePage
from .locators import ProfilePageLocators


class ProfilePage(BasePage):
    def click_edit_jmih(self):
        click_edit_jmih = self.browser.find_element(*ProfilePageLocators.EDIT_JMIH)
        click_edit_jmih.click()

    def add_pet(self):
        add_pet = self.browser.find_element(*ProfilePageLocators.ADD_PET)
        add_pet.click()

    def name_add_pet(self):
        name_add_pet = self.browser.find_element(*ProfilePageLocators.NAME_ADD_PET)
        name_add_pet.send_keys('KarP')

    def type_add_pet(self):
        type_add_pet = self.browser.find_element(*ProfilePageLocators.TYPE_ADD_PET)
        type_add_pet.click()

    def type_add_pet_1(self):
        type_add_pet_1 = self.browser.find_element(*ProfilePageLocators.TYPE_ADD_PET_1)
        type_add_pet_1.click()

    def age_add_pet(self):
        age_add_pet = self.browser.find_element(*ProfilePageLocators.ADD_PET_AGE)
        age_add_pet.send_keys('5')

    def gender_add_pet(self):
        gender_add_pet = self.browser.find_element(*ProfilePageLocators.GENDER_ADD_PET)
        gender_add_pet.click()

    def female_add_pet(self):
        female_add_pet = self.browser.find_element(*ProfilePageLocators.FEMALE_ADD_PET)
        female_add_pet.click()

    def submit_add_pet(self):
        submit_add_pet = self.browser.find_element(*ProfilePageLocators.SUBMIT_ADD_PET)
        submit_add_pet.click()

    def delete_pet(self):
        delete_pet = self.browser.find_element(*ProfilePageLocators.DELETE_PET)
        delete_pet.click()

    def delete_yes(self):
        delete_yes = self.browser.find_element(*ProfilePageLocators.DELETE_YES)
        delete_yes.click()

    def button_logo(self):
        button_logo = self.browser.find_element(*ProfilePageLocators.BUTTON_LOGO)
        button_logo.click()

    def button_quit(self):
        button_quit = self.browser.find_element(*ProfilePageLocators.BUTTON_QUIT)
        button_quit.click()


