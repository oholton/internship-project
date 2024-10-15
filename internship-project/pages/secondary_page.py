from pages.base_page import Base
from selenium.webdriver.common.by import By

class SecondaryPage(Base):
    SECONDARY_PAGE_URL = "https://soft.reelly.io/secondary-listings"
    NEXT_PAGE = (By.CSS_SELECTOR, "[wized='nextPageMLS']") #$$("[wized='nextPageMLS']")
    BACK_PAGE = (By.CSS_SELECTOR, "[wized='previousPageMLS']")



    def verify_secondary_page(self):
        self.verify_url(self.SECONDARY_PAGE_URL)

    def click_pagination_button_forward(self):
        self.wait_to_click(*self.NEXT_PAGE)

    def click_pagination_button_backward(self):
        self.wait_to_click(*self.BACK_PAGE)




