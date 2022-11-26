from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    FILTER_BY_TYPE = (By.CSS_SELECTOR, '#typesSelector')
    FILTER_BY_CAT = (By.CSS_SELECTOR, '#pv_id_2_1')
    FILTER_BY_NAME = (By.CSS_SELECTOR, '#petName')
    FILTER_NAME_THOR = (By.CSS_SELECTOR, '#app > main > div > div.p-dataview.p-component.p-dataview-grid.ml-3.mr-3 > div.p-dataview-content > div > div:nth-child(1) > div > div.product-grid-item-bottom.grid.flex-row.mt-3 > div:nth-child(1) > button > span')
    LIKE_THORA = (By.CSS_SELECTOR, '#app > main > div > div.p-dataview.p-component.p-dataview-grid.ml-3.mr-3 > div.p-dataview-content > div > div > div > div.product-grid-item-bottom.grid.flex-row.mt-3 > div.col.flex.align-content-end.justify-content-end > span.product-price')
    PAGINATOR_PAGE_1 = (By.CSS_SELECTOR, '#app > main > div > div.p-dataview.p-component.p-dataview-grid.ml-3.mr-3 > div.p-paginator.p-component.p-paginator-bottom > span > button:nth-child(3)')
    PAGINATOR_PAGE_2 = (By.CSS_SELECTOR, '#app > main > div > div.p-dataview.p-component.p-dataview-grid.ml-3.mr-3 > div.p-paginator.p-component.p-paginator-bottom > span > button:nth-child(5)')

    PAGINATOR_PAGE_3 = (By.CSS_SELECTOR, '#app > main > div > div.p-dataview.p-component.p-dataview-grid.ml-3.mr-3 > div.p-paginator.p-component.p-paginator-bottom > button.p-paginator-last.p-paginator-element.p-link')
    COMMENT_THOR = (By.CSS_SELECTOR, '#app > main > div.flex.xl\\:w-8.w-full.m-auto.mt-5.flex-wrap > div > div > div.p-card-content > form > div > div > div.p-editor-content.ql-container.ql-snow > div.ql-editor.ql-blank')
    COMMENT_SAVE = (By.CSS_SELECTOR, '#app > main > div.flex.xl\\:w-8.w-full.m-auto.mt-5.flex-wrap > div > div > div.p-card-content > form > div > button')
    LOGIN_EXIT = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(2) > a > span.p-menuitem-text')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'login')
    LOGIN_PASS = (By.CSS_SELECTOR, '#password > input')
    LOGIN_BTN = (By.XPATH, '/html/body/div[1]/main/fieldset/div/div/form/div[3]/button')


class ProfilePageLocators:
    EDIT_JMIH = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-content > div > div:nth-child(3) > div > div.product-list-action > button:nth-child(1)')
    ADD_PET = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-header > div > div:nth-child(1) > button')
    NAME_ADD_PET = (By.ID, 'name')
    TYPE_ADD_PET = (By.CSS_SELECTOR, '#typeSelector')
    TYPE_ADD_PET_1 = (By.XPATH, '/html/body/div[3]/div/ul/li[3]')
    ADD_PET_AGE = (By.CSS_SELECTOR, '#age > input')
    GENDER_ADD_PET = (By.CSS_SELECTOR, '#genderSelector')
    FEMALE_ADD_PET = (By.XPATH, '/html/body/div[3]/div/ul/li[2]')
    SUBMIT_ADD_PET = (By.CSS_SELECTOR, '#app > main > div > div > form > div > div.p-card-body > div.p-card-footer > button.p-button.p-component.p-button-success')
    DELETE_PET = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-content > div > div:nth-child(4) > div > div.product-list-action > button.p-button.p-component.p-button-danger')
    DELETE_YES = (By.CSS_SELECTOR, 'body > div.p-confirm-popup.p-component.p-ripple-disabled.p-confirm-popup-flipped > div.p-confirm-popup-footer > button.p-button.p-component.p-confirm-popup-accept.p-button-sm')
    BUTTON_LOGO =(By.XPATH, '/html/body/div[1]/header/div/div')
    BUTTON_QUIT = (By.XPATH, '/html/body/div[1]/header/div/ul/li[2]/a')