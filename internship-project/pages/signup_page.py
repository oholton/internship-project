from pages.base_page import Base
from selenium.webdriver.common.by import By
from time import sleep

class RegistrationPage(Base):
    #locators
    FULL_NAME_TEXT_FIELD = (By.ID, "Full-Name")
    PHONE_NUMBER_TEXT_FIELD = (By.ID, "phone2")
    EMAIL_TEXT_FIELD = (By.ID, "Email-3")
    PASSWORD_TEXT_FIELD = (By.ID, "field")

    #text
    fullname = 'oscar holton'
    phone_num = '2151234567'
    email = 'leoh215@gmail.com'
    password = 'Abcd12345'

    def open_registration_page(self):
        self.driver.get('https://soft.reelly.io/sign-up')

    def enter_full_name(self):
        sleep(2)
        self.input_text(self.fullname, *self.FULL_NAME_TEXT_FIELD)
        self.verify_entered_text(self.fullname, *self.FULL_NAME_TEXT_FIELD)

    def enter_phone_number(self):
        self.input_text(self.phone_num, *self.PHONE_NUMBER_TEXT_FIELD)

    def enter_email(self):
        self.input_text(self.email, *self.EMAIL_TEXT_FIELD)

    def enter_password(self):
        self.input_text(self.password, *self.PASSWORD_TEXT_FIELD)


    def verify_full_name(self):
        self.verify_entered_text(self.fullname, *self.FULL_NAME_TEXT_FIELD)


    def verify_phone(self):
        self.verify_entered_text(self.phone_num, *self.PHONE_NUMBER_TEXT_FIELD )

    def verify_email(self):
        self.verify_entered_text(self.email, *self.EMAIL_TEXT_FIELD)

    def verify_password(self):
        self.verify_entered_text(self.password, *self.PASSWORD_TEXT_FIELD)


