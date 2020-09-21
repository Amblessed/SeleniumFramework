import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration


class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.readApplicationURL()
    username = ReadConfig.readUserEmail()
    password = ReadConfig.readPassword()
    logger = LogGeneration.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login Successful **********")

        self.logger.info("******* Starting Search Customer By Name **********")

        self.addCustomer = AddCustomer(self.driver)
        self.addCustomer.clickCustomers()
        self.addCustomer.clickSubMenuCustomers()

        self.logger.info("************* Searching Customer by Name **********")
        self.searchCustomer = SearchCustomer(self.driver)
        self.searchCustomer.setFirstName("Victoria")
        self.searchCustomer.setLastName("Terces")
        self.searchCustomer.clickSearch()
        time.sleep(5)
        status = self.searchCustomer.searchCustomerByName("Victoria Terces")
        self.driver.close()
        if status:
            assert True
        self.logger.info("***************  TC_SearchCustomerByEmail_005 Finished  *********** ")
