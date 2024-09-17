from pages.base_page import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


class SettingsPage(Base):
    EDIT_PROFILE_BUTTON = (By. CSS_SELECTOR, "[href='/profile-edit']")
    ADD_PROJECT_BUTTON = (By. CSS_SELECTOR, "[href='/add-a-project']")
    COMMUNITY_BUTTON = (By. XPATH, "//div[@class='setting-text' and text()='Community']")
    CONTACT_US_BUTTON = (By. XPATH, "//div[@class='setting-text' and text()='Contact us']")
    USER_GUIDE_BTN = (By.XPATH, "//div[@class='setting-text' and text()='User guide']")
    CHANGE_PASSWORD_OPTION = (By. CSS_SELECTOR, '[href="/set-new-password"]')



    def click_edit_profile_button(self):
        self.click(*self.EDIT_PROFILE_BUTTON)

    def click_add_project_button(self):
        self.click(*self.ADD_PROJECT_BUTTON)

    def click_community_button(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        self.wait_to_click(*self.COMMUNITY_BUTTON)

    def click_contact_us_button(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        sleep(2)
        self.wait_to_click(*self.CONTACT_US_BUTTON)

    def click_user_guide(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        sleep(2)
        self.wait_to_click(*self.USER_GUIDE_BTN)

    def click_change_password_option(self):
        self.wait_to_click(*self.CHANGE_PASSWORD_OPTION)

