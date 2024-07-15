from pages.base_page import Base
from selenium.webdriver.common.by import By

class SettingsPage(Base):
    EDIT_PROFILE_BUTTON = (By. CSS_SELECTOR, "[href='/profile-edit']")

    def click_edit_profile_button(self):
        self.click(*self.EDIT_PROFILE_BUTTON)
