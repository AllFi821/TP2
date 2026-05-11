from selenium.webdriver.common.by import By
from .base_page import BasePage

class InfiniteScrollPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://the-internet.herokuapp.com/infinite_scroll"
        self.BLOCKS = (By.CLASS_NAME, "jscroll-added")

    def load(self):
        self.driver.get(self.url)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_blocks_count(self):
        return len(self.driver.find_elements(*self.BLOCKS))