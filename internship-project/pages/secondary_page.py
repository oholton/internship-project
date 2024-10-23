from pages.base_page import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SecondaryPage(Base):
    SECONDARY_PAGE_URL = "https://soft.reelly.io/secondary-listings"
    NEXT_PAGE = (By.CSS_SELECTOR, "[wized='nextPageMLS']") #$$("[wized='nextPageMLS']")
    BACK_PAGE = (By.CSS_SELECTOR, "[wized='previousPageMLS']")
    PAGE_NUMBER = (By.XPATH, "//div[@w-el-text='1']") #$x("//div[@w-el-text='1']")



    def verify_secondary_page(self):
        self.verify_url(self.SECONDARY_PAGE_URL)

    def click_pagination_button_forward(self):
       current_page = 1
       final_page = 99
       while current_page <= final_page:
           self.wait_to_click(*self.NEXT_PAGE)
           current_page += 1




    def click_pagination_button_backward(self):
        self.wait_to_click(*self.BACK_PAGE)
        current_page = 99
        final_page = 1
        while current_page > final_page:
            self.wait_to_click(*self.BACK_PAGE)
            current_page -= 1






