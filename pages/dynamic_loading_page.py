from selenium.webdriver.common.by import By
from .base_page import BasePage

class DynamicLoadingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://the-internet.herokuapp.com/dynamic_loading/2"
        self.START_BUTTON = (By.CSS_SELECTOR, "#start button")
        self.FINISH_TEXT = (By.ID, "finish")

    def load(self):
        self.driver.get(self.url)

    def click_start(self):
        self.driver.find_element(*self.START_BUTTON).click()