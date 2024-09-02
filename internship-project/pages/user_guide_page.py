from pages.base_page import Base
from selenium.webdriver.common.by import By

class UserGuidePage(Base):
    USER_GUIDE_URL = "https://soft.reelly.io/user-guide"
    VIDEO_TITLE_LINKS = (By.XPATH, "//a[@class='ytp-title-link yt-uix-sessionlink']")



    def verify_user_guide_open(self):
        self.verify_partial_url('user-guide')

    def verify_video_title_links(self):
        video_links = self.find_elements(*self.VIDEO_TITLE_LINKS)
        for video in video_links:
            title = video.text
            assert title, f"Video with link '{video.get_attribute('href')}' has no title."



