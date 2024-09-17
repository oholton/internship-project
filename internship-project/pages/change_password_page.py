from pages.base_page import Base
from selenium.webdriver.common.by import By
from time import sleep

class ChangePasswordPage(Base):
    PASSWORD_PAGE_URL = "https://soft.reelly.io/set-new-password"
    NEW_PASSWORD_TEXT_FIELD = (By.ID, "Enter-new-password")
    REPEAT_PASSWORD_TEXT_FIELD = (By.ID, "Repeat-password")
    TEST_PASSWORD = "password1234"
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".submit-button-2.w-button")

    def verify_password_page(self):
        self.verify_url(self.PASSWORD_PAGE_URL)

    def input_new_password(self):
        self.input_text(self.TEST_PASSWORD, *self.NEW_PASSWORD_TEXT_FIELD)

    def repeat_new_password(self):
        self.input_text(self.TEST_PASSWORD, *self.REPEAT_PASSWORD_TEXT_FIELD)

    def verify_change_password_clickability(self):
        self.wait_for_clickability(*self.CHANGE_PASSWORD_BUTTON)

