from pages.base_page import Base
from selenium.webdriver.common.by import By
from time import sleep
class AddProjectPage(Base):
    ADD_PROJECT_PAGE_URL = "https://soft.reelly.io/add-a-project"
    YOUR_NAME_TEXTFIELD = (By.CSS_SELECTOR, "[data-name='Your name']")
    YOUR_COMPANY_NAME_TEXTFIELD = (By.CSS_SELECTOR, "[data-name='Your company name']") #$$("[data-name='Your company name']")
    ROLE_TEXTFIELD = (By.CSS_SELECTOR, "[data-name='Role']")
    SEND_APP_BUTTON = (By.CSS_SELECTOR, "[type='submit']")


    def verify_add_project_page_open(self):
        self.verify_url(expected_url=self.ADD_PROJECT_PAGE_URL)

    def input_name(self):
        self.input_text("Oscar Holt", *self.YOUR_NAME_TEXTFIELD)

    def input_company(self):
        self.input_text("My company", *self.YOUR_COMPANY_NAME_TEXTFIELD)


    def input_role(self):
        self.input_text("Tester", *self.ROLE_TEXTFIELD)


    def verify_all_entries(self):
        self.verify_multiple_text_entries(
            ("Oscar Holt", self.YOUR_NAME_TEXTFIELD),
            ("My company", self.YOUR_COMPANY_NAME_TEXTFIELD),
            ("Tester", self.ROLE_TEXTFIELD)
        )

    def send_bttn_clickable(self):
        self.wait_for_clickability(*self.SEND_APP_BUTTON)




