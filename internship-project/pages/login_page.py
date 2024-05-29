from pages.base_page import Base
from selenium.webdriver.common.by import By
from time import sleep


class LoginPage(Base):
    EMAIL_FIELD = (By.CSS_SELECTOR, "#email-2")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#field")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[class*='login-button']")
    email = 'leoh215@gmail.com'
    password = 'bleach01'


    def open_login(self):
        self.driver.get('https://soft.reelly.io/sign-in')

    def login(self):
        self.input_text(self.email, *self.EMAIL_FIELD)
        self.input_text(self.password, *self.PASSWORD_FIELD)
        self.click(*self.LOGIN_BUTTON)




