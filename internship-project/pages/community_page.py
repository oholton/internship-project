from pages.base_page import Base
from selenium.webdriver.common.by import By

class CommunityPage(Base):
    COMMUNITY_PAGE_URL = "https://soft.reelly.io/community"
    CONTACT_SUPPORT_BUTTON = By.CSS_SELECTOR, "[id*='w-node-f7ead340-ee2a-2b84-cdd5-5a35322aacbf']"

    def verify_community_page(self):
        self.verify_url(self.COMMUNITY_PAGE_URL)

    def verify_contact_support_button_clickable(self):
        self.wait_for_clickability(*self.CONTACT_SUPPORT_BUTTON)




