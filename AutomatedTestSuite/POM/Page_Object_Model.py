from selenium import webdriver
from selenium.webdriver.common.by import By


class TestingChallenge1:
    # Locators
    first_name = "//input[@id='firstname']"
    submit_button = "//input[@name='formSubmit']"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Actions
    def first_name_script_injection(self, first_name):
        # Store the found element in a variable.
        enter_first_name_script_injection = self.driver.find_element(By.XPATH, self.first_name)

        # Clear the input field.
        enter_first_name_script_injection.clear()

        # Enter input.
        enter_first_name_script_injection.send_keys(first_name)

    def press_submit_button(self):
        # Store the found element in a variable.
        press_submit_btn = self.driver.find_element(By.XPATH, self.submit_button)

        # Press the submit button.
        press_submit_btn.click()
