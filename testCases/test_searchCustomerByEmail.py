import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.readApplicationURL()
    username = ReadConfig.readUserEmail()
    password = ReadConfig.readPassword()
    logger = LogGeneration.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login Successful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addCustomer = AddCustomer(self.driver)
        self.addCustomer.clickCustomers()
        self.addCustomer.clickSubMenuCustomers()

        self.logger.info("************* searching customer by emailID **********")
        self.searchCustomer = SearchCustomer(self.driver)
        self.searchCustomer.setEmail("victoria_victoria@nopCommerce.com")
        self.searchCustomer.clickSearch()
        time.sleep(5)
        status = self.searchCustomer.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        if status:
            assert True
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")
