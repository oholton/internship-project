from pages.base_page import Base
from selenium.webdriver.common.by import By

class ContactUsPage(Base):
    CONTACT_US_URL = "https://soft.reelly.io/contact-us"
    SOCIAL_MEDIA_ICONS = (By.CSS_SELECTOR, "[class='social-button']")
    CONNECT_THE_COMPANY_BTN = (By.XPATH, "//div[text()='Connect the company']")

    def verify_contact_us_page(self):
        self.verify_partial_url('contact-us')

    def verify_social_media_icons(self, min_count=4):
        elements = self.find_elements(*self.SOCIAL_MEDIA_ICONS)
        assert len(elements) >= min_count, f"Expected at least {min_count} but only returned {len(elements)}"
        return elements

    def verify_connect_the_company_btn(self):
        self.wait_for_clickability(*self.CONNECT_THE_COMPANY_BTN)

