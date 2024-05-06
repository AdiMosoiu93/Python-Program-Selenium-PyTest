from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from AutomatedTestSuite.POM.Page_Object_Model import TestingChallenge1
from selenium.webdriver.common.by import By
import pytest
from assertpy import assert_that


class TestScriptInjection:
    @pytest.fixture()
    def setup(self):
        # 1) Open Web Browser(Chrome/firefox/IE). Chrome was used for this test case.
        print("Open Chrome web browser")
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options, service=ChromeService(ChromeDriverManager().install()))

        # Set implicit wait
        self.driver.implicitly_wait(15)

        # 2) Open URL http://testingchallenges.thetestingmap.org/index.php
        print("Open URL http://testingchallenges.thetestingmap.org/index.php")
        self.driver.get('http://testingchallenges.thetestingmap.org/index.php')
        self.driver.maximize_window()

        yield
        # 3) Close the browser.
        print(" Close browser")
        self.driver.close()

    def test_script_injection(self, setup):
        self.script_injection = TestingChallenge1(self.driver)
        # Precondition: the check counter is 0.
        expected_value = 0
        actual_value = self.script_injection.get_checks_counter()

        assert actual_value == expected_value, "Precondition: checks_counter is not 0"

        # 1) Input script injection in First Name input field.
        self.script_injection.enter_first_name("<h1>TRG Group</h1>")

        # 2) Press on the "Submit" button.
        self.script_injection.press_submit_button()

        # Assert that the checks counter is at least 4.
        expected_value = 4
        actual_value = self.script_injection.get_checks_counter()

        print(type(self.script_injection.get_checks_counter()))
        print(type(expected_value))

        assert actual_value >= expected_value, "checks_counter is not at least expected_value"

        # Assert that all expected values are present in the actual list.
        expected_value = [
            "Other chars then alphabetic",
            "Space in the middle",
            "You used html tags",
            "Average value"
        ]
        actual_value = self.script_injection.get_scenarios_list()

        assert all(item in actual_value for item in expected_value), "Not all expected values are present in the actual value list"

        # Get the actual list of displayed elements on the page.
        displayed_elements = self.script_injection.check_scenarios_are_displayed()

        # Assert that all expected elements are displayed on the page.
        for item in actual_value:
            assert item in displayed_elements, f"Element '{item}' is not displayed on the page"

        # Assert that first name is included in confirmation message.
        expected_value = "<h1>TRG Group</h1>"
        actual_value = self.script_injection.get_first_name_confirmation_message1()

        assert expected_value in actual_value, "First name is not included in confirmation message"

        # Assert that username includes first name in confirmation message.
        expected_value = "<h1>TRG Group</h1>"
        actual_value = self.script_injection.get_first_name_confirmation_message2()

        assert expected_value in actual_value, "First name is not included in username"

