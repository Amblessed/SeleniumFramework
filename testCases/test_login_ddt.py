import os
import time

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
from utilities.XMLReader import ReadXML
from utilities.Constants import Constants


class Test_OO2_DDT_Login:
    baseURL = ReadConfig.readApplicationURL()
    message_error = ReadConfig.readErrorMessage()
    # xml_path = Constants.PARENTDIRECTORY + "\\TestData\\TestData.xml"
    xml_path = os.path.join(Constants.PARENTDIRECTORY, "TestData", "TestData.xml")
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
            expected_title = Constants.EXPECTED_TITLE
            if actual_title == expected_title:
                print("******************** Valid Login test Passed ********************")
                self.logger.info("******************** Login test Passed ********************")
                self.lp.clickLogout()
                list_status.append("Pass")
            elif actual_title != expected_title:
                error_returned = self.lp.getErrorMessage()
                if self.message_error in error_returned:
                    list_status.append("Fail")
                    print("******************** Invalid Login test Passed ********************")
                    self.logger.info("******************** Invalid Login test Passed ********************")

            time.sleep(5)

        print(expected_output)
        print(list_status)
        print("********** End of Data Driven Test **********")
        self.driver.close()

        self.logger.info("********** End of Data Driven Test **********")
