from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from AutomatedTestSuite.POM.Page_Object_Model import TestingChallenge1
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def setup():
    # 1) Open Web Browser(Chrome/firefox/IE). Chrome was used for this test case.
    print("Open Chrome web browser")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    # 2) Open URL http://testingchallenges.thetestingmap.org/index.php
    print("Open URL http://testingchallenges.thetestingmap.org/index.php")
    driver.get('http://testingchallenges.thetestingmap.org/index.php')
    driver.maximize_window()

    yield
    # 3) Close the browser.
    print(" Close browser")
    driver.close()
