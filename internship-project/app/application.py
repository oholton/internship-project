from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.signup_page import RegistrationPage
from pages.connect_company import ConnectCompanyPage
from pages.settings_page import SettingsPage
from pages.profile_page import ProfilePage
from pages.add_a_project_page import AddProjectPage
from pages.community_page import CommunityPage
from pages.contact_us_page import ContactUsPage

class Application:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.signup_page = RegistrationPage(driver)
        self.connect_company = ConnectCompanyPage(driver)
        self.settings_page = SettingsPage(driver)
        self.profile_page = ProfilePage(driver)
        self.add_a_project_page = AddProjectPage(driver)
        self.community_page = CommunityPage(driver)
        self.contact_us_page = ContactUsPage(driver)




