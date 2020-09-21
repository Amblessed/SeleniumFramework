import time

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
from utilities.XMLReader import ReadXML


class Test_OO2_DDT_Login:
    baseURL = ReadConfig.readApplicationURL()
    message_error = ReadConfig.readErrorMessage()
    xml_path = "C:\\Users\\okeyb\\Documents\\Pycharm\\SeleniumFramework\\TestData\\TestData.xml"
    logger = LogGeneration.loggen()

    def test_login(self, setup):
        self.logger.info("******************** Test_OO2_DDT_Login ********************")
        self.logger.info("******************** Verifying Login DDT Test ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        list_status = []
        expected_output = []

        login_data_values = ReadXML.readXMLFile(self.xml_path)
        for credentials in login_data_values:
            self.username = credentials.get("username")
            self.password = credentials.get("password")
            self.output = credentials.get("output")
            expected_output.append(self.output)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"
            if actual_title == expected_title:
                self.logger.info("******************** Login test Passed ********************")
                self.lp.clickLogout()
                list_status.append("Pass")

            elif self.lp.getErrorMessage() == self.message_error:
                self.logger.info("******************** Invalid Login test Passed ********************")
                list_status.append("Fail")

        # if "Fail" not in list_status:
        #     self.logger.info("********** Data Driven Test Passed **********")
        #     self.driver.close()
        #     assert True
        # else:
        #     self.logger.info("********** Data Driven Test Failed **********")
        #     self.driver.close()
        #     assert False

        self.logger.info("********** End of Data Driven Test **********")
