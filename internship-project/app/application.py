from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.signup_page import RegistrationPage
from pages.connect_company import ConnectCompanyPage

class Application:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.signup_page = RegistrationPage(driver)
        self.connect_company = ConnectCompanyPage(driver)



