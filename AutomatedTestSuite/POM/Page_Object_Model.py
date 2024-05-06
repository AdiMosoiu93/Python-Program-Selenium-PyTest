from selenium import webdriver
from selenium.webdriver.common.by import By


class TestingChallenge1:
    __test__ = False
    # Locators
    first_name = "//input[@id='firstname']"
    submit_button = "//input[@name='formSubmit']"
    checks_counter = "//span[@class='values-tested']"
    scenarios_list = "//ul[@class='values-description t10']/child::li"
    first_name_confirmation_message1 = "//h3[normalize-space()='Confirmation message']/following-sibling::p[2]"
    first_name_confirmation_message2 = "//h3[normalize-space()='Confirmation message']/following-sibling::p[4]"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Actions
    def enter_first_name(self, first_name):
        # Store the found element in a variable.
        enter_first_name = self.driver.find_element(By.XPATH, self.first_name)

        # Clear the input field.
        enter_first_name.clear()

        # Enter input.
        enter_first_name.send_keys(first_name)

    def press_submit_button(self):
        # Store the found element in a variable.
        press_submit_btn = self.driver.find_element(By.XPATH, self.submit_button)

        # Press the submit button.
        press_submit_btn.click()

    def get_checks_counter(self):
        # Store the found element in a variable.
        get_checks_counter = self.driver.find_element(By.XPATH, self.checks_counter)

        # Convert the checks_counter into an integer.
        get_checks_counter_text = get_checks_counter.text
        get_checks_counter_int = int(get_checks_counter_text)

        # Return
        return get_checks_counter_int

    def get_scenarios_list(self):
        # Store the found element in a variable.
        get_scenarios_list = self.driver.find_elements(By.XPATH, self.scenarios_list)

        # Extract text from scenario web elements.
        scenario_text = [scenario.text for scenario in get_scenarios_list]

        # Return
        return scenario_text

    def check_scenarios_are_displayed(self):
        # Find all scenario elements.
        scenario_elements = self.driver.find_elements(By.XPATH, self.scenarios_list)

        # Filter out elements that are displayed.
        displayed_elements = [element.text for element in scenario_elements if element.is_displayed()]

        # Return list of displayed elements
        return displayed_elements

    def get_first_name_confirmation_message1(self):
        # Store the found element in a variable.
        get_first_name_confirmation_message1 = self.driver.find_element(By.XPATH, self.first_name_confirmation_message1)

        # Return
        print(get_first_name_confirmation_message1.text)
        return get_first_name_confirmation_message1.text

    def get_first_name_confirmation_message2(self):
        # Store the found element in a variable.
        get_first_name_confirmation_message2 = self.driver.find_element(By.XPATH, self.first_name_confirmation_message2)

        # Return
        print(get_first_name_confirmation_message2.text)
        return get_first_name_confirmation_message2.text
