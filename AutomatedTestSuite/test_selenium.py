from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from AutomatedTestSuite.POM.Page_Object_Model import TestingChallenge1


class TestScriptInjection:
    def test_script_injection(self):
        # 1) Open Web Browser(Chrome/firefox/IE). Chrome was used for this test case.
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options, service=ChromeService(ChromeDriverManager().install()))

        # 2) Open URL http://testingchallenges.thetestingmap.org/index.php
        self.driver.get('http://testingchallenges.thetestingmap.org/index.php')
        self.driver.maximize_window()

        self.script_injection = TestingChallenge1(self.driver)
        # 3) Input script injection in First Name input field.
        self.script_injection.first_name_script_injection("<h1>TRG Group</h1>")

        # 4) Press on the "Submit" button.
        self.script_injection.press_submit_button()
