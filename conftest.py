from keywords.keywords import openBrowser, navigateTo, killBrowser
from utilities.data_reader import read_json, read_excel
from utilities.logger import logger
import pytest
import time

config = read_json("D:\Selenium Practices\Week 6\config\config.json")

browserType = config["browser"]["type"]
driverPath = config["driver_paths"]["chrome_driver"]
testURL = config["environment"]["base_url"]
waitTimw = config["browser"]["implicit_wait"]


reportDir = config["reporting"]["report_path"]

@pytest.fixture
def setup_browser():
    driver = openBrowser(browserType, driverPath)
    navigateTo(driver, testURL, waitTimw)
    yield driver
    time.sleep(5)
    killBrowser(driver)

@pytest.fixture(scope="function")
def log():
    return logger(reportDir)