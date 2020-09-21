import time

import pytest

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.Constants import Constants
from utilities.customLogger import LogGeneration
from utilities.readProperties import ReadConfig


class Test_003_AddCustomer:
    baseURL = ReadConfig.readApplicationURL()
    username = ReadConfig.readUserEmail()
    password = ReadConfig.readPassword()
    logger = LogGeneration.loggen()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("******************** Test_003_AddCustomer ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        time.sleep(5)
        print("********** Login Successful **********")

        self.addCustomer = AddCustomer(self.driver)
        self.addCustomer.clickCustomers()
        self.addCustomer.clickSubMenuCustomers()
        self.addCustomer.clickAddNewCustomer()
        time.sleep(5)

        self.logger.info("******************** Providing Customer Information ********************")
        print("********** Providing Customer Information **********")

        self.email = Constants.random_email_generator()
        self.addCustomer.inputEmail(self.email)
        self.addCustomer.inputPassword("test123")
        self.addCustomer.inputFirstName("Bright")
        self.addCustomer.inputLastName("Brightest")
        self.addCustomer.selectGender(Constants.MALE)
        self.addCustomer.inputDateOfBirth("7/05/1985")
        self.addCustomer.inputCompanyName("NTTData GmbH")
        self.addCustomer.inputCustomerRoles(Constants.GUESTS)
        self.addCustomer.selectManagerVendor(Constants.VENDORS_TWO)
        self.addCustomer.inputAdminContent("This is for testing purposes only")
        self.driver.save_screenshot(".\\Screenshots\\" + "first_run.png")
        self.addCustomer.clickSaveButton()

        self.msg = self.driver.find_element_by_tag_name("body").text

        # print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")
