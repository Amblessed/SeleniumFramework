import pytest

from pageObjects.LoginPage import LoginPage
from utilities.Constants import Constants
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration


class Test_OO1_Login:
    baseURL = ReadConfig.readApplicationURL()
    username = ReadConfig.readUserEmail()
    password = ReadConfig.readPassword()

    logger = LogGeneration.loggen()

    def test_HomePageTitle(self, setup):
        self.logger.info("******************** Test_OO1_Login Started ********************")
        self.logger.info("******************** Verifying Home Page Title********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******************** Verifying Home Page Title test passed********************")
        else:
            self.driver.save_screenshot(Constants.PARENTDIRECTORY+"\\Screenshots\\" + "test_HomePageTitle.png")
            self.driver.close()
            self.logger.error("******************** Home Page Title test failed********************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("******************** Verifying Login Test ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("******************** Login test Passed********************")
        else:
            self.driver.save_screenshot(Constants.PARENTDIRECTORY+"\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("******************** Login test Failed********************")
            assert False

