from selenium.webdriver.common.by import By
from .base_page import BasePage

class DynamicControlsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://the-internet.herokuapp.com/dynamic_controls"
        self.CHECKBOX = (By.ID, "checkbox")
        self.REMOVE_ADD_BTN = (By.CSS_SELECTOR, "#checkbox-example button")
        self.MESSAGE = (By.ID, "message")
        self.INPUT_FIELD = (By.CSS_SELECTOR, "#input-example input")
        self.ENABLE_DISABLE_BTN = (By.CSS_SELECTOR, "#input-example button")

    def load(self):
        self.driver.get(self.url)

    def click_remove_add(self):
        self.driver.find_element(*self.REMOVE_ADD_BTN).click()

    def click_enable_disable(self):
        self.driver.find_element(*self.ENABLE_DISABLE_BTN).click()

    def is_input_enabled(self):
        return self.driver.find_element(*self.INPUT_FIELD).is_enabled()