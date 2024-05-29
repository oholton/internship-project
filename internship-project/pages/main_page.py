from pages.base_page import Base
from selenium.webdriver.common.by import By
from time import sleep

class MainPage(Base):
    OFFLEFT = (By.XPATH, "//div[text()='Off-plan']")
    FILTER_ICON = (By.CSS_SELECTOR, "[class='filter-text']")
    TITLE = (By.XPATH, "//div[text()='Total projects']")
    FILTER_LAST_UNITS_BUTTON = (By.XPATH, "//div[@class='tag-text-proparties' and text()='Last units']")
    LAST_UNITS_TAG = (By.XPATH, "//div[@wized='projectStatus' and @class='_5-comission' and @w-el-text='Status' and text()='Last units']")


    def offleft(self):
        self.click(*self.OFFLEFT)

    def search_filters(self):
        self.click(*self.FILTER_ICON)

    def verify_offleft_page(self):
        self.verify_text("Total projects", *self.TITLE)

    def filter_by_last_unit(self):
        self.click(*self.FILTER_ICON)
        self.wait_to_click(*self.FILTER_LAST_UNITS_BUTTON)
        sleep(5)

    def verify_tag_last_units(self):
        lastunit_elements = self.find_elements(*self.LAST_UNITS_TAG)
        for text in lastunit_elements:
            self.verify_text("Last units", *self.LAST_UNITS_TAG)






