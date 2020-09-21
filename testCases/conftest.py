from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        p = ChromeDriverManager()  # pytest -v -s testCases/test_login.py --browser chrome
        driver = webdriver.Chrome(executable_path=p.install())
        # return driver
    elif browser == "firefox":
        p = GeckoDriverManager()
        driver = webdriver.Firefox(executable_path=p.install())
    else:
        p = ChromeDriverManager()
        driver = webdriver.Chrome(executable_path=p.install())
    return driver


def pytest_addoption(parser):  # This will get the value from CLI / hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


# ############## Pytest HTMl Report ######################


# It is hook to Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata["Project Name"] = "Nop Commerce"
    config._metadata["Module Name"] = "Customers"
    config._metadata["Tester"] = "Bright"


# It is hook to delete / Modify Environment info to HTML Report
def pytest_metadata(metadata):
    # metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
