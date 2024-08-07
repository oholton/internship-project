from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from support.logger import logger

class Base:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url):
        logger.info(f"Opening {url}")
        self.driver.get(url)

    def find_element(self, *locator):
        self.driver.find_element(*locator)
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        self.driver.find_elements(*locator)
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        logger.info(f"Clicking {locator}")
        self.find_element(*locator).click()

    def store_current_window(self):
        current_window = self.driver.current_window_handle
        print(f'Current window: {current_window}')
        print('ALL windows:', self.driver.window_handles)
        return current_window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print('ALL windows:', self.driver.window_handles)
        print('Switching to... ', all_windows[1])
        self.driver.switch_to.window(all_windows[1])

    def switch_window_by_id(self, window_id):
        print('Switching to... ', window_id)
        self.driver.switch_to.window(window_id)

    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f"Expected {expected_text}, but got {actual_text}"

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f"Expected {expected_text} but got {actual_text}"

    def verify_partial_url(self, expected_partial_url):
        self.wait.until(EC.url_contains(expected_partial_url), message=f'Url does not contain {expected_partial_url}')
    def verify_url(self, expected_url):
        self.wait.until(EC.url_matches(expected_url))
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"Expected URL: {expected_url}, but got: {actual_url}"


    def wait_to_click(self, *locator):
        logger.info(f"Waiting for {locator} to appear")
        self.wait.until(EC.element_to_be_clickable((locator))).click()

    def wait_for_clickability(self, *locator):
        logger.info(f"Waiting for {locator} to appear")
        self.wait.until(EC.element_to_be_clickable((locator)))
        logger.info(f"Element {locator} is clickable")

    def close(self):
        self.driver.close()

    def verify_entered_text(self, expected_text, *locator):
        textfield = self.find_element(*locator)
        entered_text = textfield.get_attribute("value")
        assert expected_text in entered_text, f"Expected {expected_text} but got {entered_text}"

    def verify_multiple_text_entries(self, *expected_locator_pairs):
        for expected_text, locator in expected_locator_pairs:
            textfield = self.find_element(*locator)
            entered_text = textfield.get_attribute("value")
            assert entered_text == expected_text, f"Expected '{expected_text}' in {locator} but got '{entered_text}'"

    def replace_text(self, text, *locator):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)
