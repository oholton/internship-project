from pages.base_page import Base
from selenium.webdriver.common.by import By

class ProfilePage(Base):
    COMPANY_NAME_TEXT = (By.XPATH, "//input[@name='Company-name']")
    SAVE_CHANGES = (By.XPATH, "//*[text()='Save changes']")
    CLOSE_BUTTON = (By.XPATH, "//*[text()='Close']")
    TEXT_TEST = 'automated testing'

    def company_text_change(self):
        self.replace_text(self.TEXT_TEST, *self.COMPANY_NAME_TEXT)

    def verify_company_text_change(self):
        self.verify_entered_text(self.TEXT_TEST, *self.COMPANY_NAME_TEXT)
    def verify_save_changes_clickable(self):
        self.wait_for_clickability(*self.SAVE_CHANGES)
    def verify_close_button_clickable(self):
        self.wait_for_clickability(*self.CLOSE_BUTTON)
