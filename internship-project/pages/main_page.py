from pages.base_page import Base
from selenium.webdriver.common.by import By
from time import sleep
from support.logger import logger


class MainPage(Base):
    OFFLEFT = (By.XPATH, "//div[text()='Off-plan']")
    FILTER_ICON = (By.CSS_SELECTOR, "[class='filter-text']")
    TITLE = (By.XPATH, "//div[text()='Total projects']")
    FILTER_LAST_UNITS_BUTTON = (By.XPATH, "//div[@class='tag-text-proparties' and text()='Last units']")
    LAST_UNITS_TAG = (By.XPATH, "//div[@wized='projectStatus' and @class='_5-comission' and @w-el-text='Status' and text()='Last units']")


    def offleft(self):
        self.wait_to_click(*self.OFFLEFT)

    def search_filters(self):
        self.click(*self.FILTER_ICON)

    def verify_offleft_page(self):
        self.verify_text("Total projects", *self.TITLE)

    def filter_by_last_unit(self):
        self.wait_to_click(*self.FILTER_ICON)
        self.wait_to_click(*self.FILTER_LAST_UNITS_BUTTON)
        sleep(5)

    def verify_tag_last_units(self):
        expected_text = "Last units"
        lastunit_elements = self.find_elements(*self.LAST_UNITS_TAG)
        for tag in lastunit_elements:
            print(f"Verifying element text: {tag.text}")
            assert expected_text == tag.text, f"Expected {expected_text} but got {tag.text}"









