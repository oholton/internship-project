from pages.base_page import Base
from selenium.webdriver.common.by import By

class ConnectCompanyPage(Base):
    def verify_connect_company_open(self):
        self.verify_partial_url('book-presentation')

