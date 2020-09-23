import time
from selenium.webdriver.support.ui import Select
from utilities.Constants import Constants


class AddCustomer:
    Customers_xpath: str = "//a[@href='#']//span[contains(text(), 'Customers')]"
    SubMenu_Customers_xpath: str = "//a[@href='/Admin/Customer/List']"
    Customers_AddNew_xpath: str = "//a[@href='/Admin/Customer/Create']"
    CustomerInfo_Email_xpath: str = "//input[@id='Email']"
    CustomerInfo_Password_xpath: str = "//input[@id='Password']"
    CustomerInfo_FirstName_xpath: str = "//input[@id='FirstName']"
    CustomerInfo_LastName_xpath: str = "//input[@id='LastName']"
    CustomerInfo_GenderMale_xpath: str = "//input[@id='Gender_Male']"
    CustomerInfo_GenderFemale_xpath: str = "//input[@id='Gender_Female']"
    CustomerInfo_DateOfBirth_xpath: str = "//input[@id='DateOfBirth']"
    CustomerInfo_CompanyName_xpath: str = "//input[@id='Company']"
    CustomerInfo_TaxExempt_xpath: str = "//input[@id='IsTaxExempt']"
    CustomerInfo_Newsletter_xpath: str = "//ul[@id='SelectedNewsletterSubscriptionStoreIds_taglist']"
    CustomerInfo_CustomerRoles_xpath: str = "//input[@aria-describedby='SelectedCustomerRoleIds_taglist']"
    CustomerInfo_CustomerRoles_Administrators_xpath: str = "//li[contains(text(), 'Administrators')]"
    CustomerInfo_CustomerRoles_ForumModerators_xpath: str = "//li[contains(text(), 'Forum Moderators')]"
    CustomerInfo_CustomerRoles_Guests_xpath: str = "//li[contains(text(), 'Guests')]"
    CustomerInfo_CustomerRoles_Registered_xpath: str = "//li[contains(text(), 'Registered')]"
    CustomerInfo_CustomerRoles_Vendors_xpath: str = "//select[@id='VendorId']"
    CustomerInfo_AdminComment_xpath: str = "//textarea[@id='AdminComment']"
    CustomerInfo_Save_xpath: str = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver
        self.listItem = None

    def clickCustomers(self):
        self.driver.find_element_by_xpath(self.Customers_xpath).click()

    def clickSubMenuCustomers(self):
        self.driver.find_element_by_xpath(self.SubMenu_Customers_xpath).click()

    def clickAddNewCustomer(self):
        self.driver.find_element_by_xpath(self.Customers_AddNew_xpath).click()

    def inputEmail(self, email):
        self.driver.find_element_by_xpath(self.CustomerInfo_Email_xpath).clear()
        self.driver.find_element_by_xpath(self.CustomerInfo_Email_xpath).send_keys(email)

    def inputPassword(self, password):
        self.driver.find_element_by_xpath(self.CustomerInfo_Password_xpath).clear()
        self.driver.find_element_by_xpath(self.CustomerInfo_Password_xpath).send_keys(password)

    def inputFirstName(self, firstName):
        self.driver.find_element_by_xpath(self.CustomerInfo_FirstName_xpath).clear()
        self.driver.find_element_by_xpath(self.CustomerInfo_FirstName_xpath).send_keys(firstName)

    def inputLastName(self, lastName):
        self.driver.find_element_by_xpath(self.CustomerInfo_LastName_xpath).clear()
        self.driver.find_element_by_xpath(self.CustomerInfo_LastName_xpath).send_keys(lastName)

    def selectGender(self, gender):
        if gender == Constants.MALE:
            self.driver.find_element_by_xpath(self.CustomerInfo_GenderMale_xpath).click()
        elif gender == Constants.FEMALE:
            self.driver.find_element_by_xpath(self.CustomerInfo_GenderFemale_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.CustomerInfo_GenderMale_xpath).click()

    def inputDateOfBirth(self, dob):
        # self.driver.find_element_by_id(self.CustomerInfo_FirstName_xpath).clear()
        self.driver.find_element_by_xpath(self.CustomerInfo_DateOfBirth_xpath).send_keys(dob)

    def inputCompanyName(self, companyName):
        self.driver.find_element_by_xpath(self.CustomerInfo_CompanyName_xpath).clear()
        self.driver.find_element_by_xpath(self.CustomerInfo_CompanyName_xpath).send_keys(companyName)

    def inputCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.CustomerInfo_CustomerRoles_xpath).click()
        time.sleep(5)
        if role == Constants.REGISTERED:
            self.listItem = self.driver.find_element_by_xpath(self.CustomerInfo_CustomerRoles_Registered_xpath)
        elif role == Constants.ADMINISTRATORS:
            self.listItem = self.driver.find_element_by_xpath(self.CustomerInfo_CustomerRoles_Administrators_xpath)
        elif role == Constants.VENDORS:
            self.listItem = self.driver.find_element_by_xpath(self.CustomerInfo_CustomerRoles_Vendors_xpath)
        elif role == Constants.GUESTS:
            try:
                registered = "//ul[@id='SelectedCustomerRoleIds_taglist']/li/span[contains(text(), 'Registered')]"
                self.driver.find_element_by_xpath(registered)
                self.driver.find_element_by_xpath(
                    "//ul[@id='SelectedCustomerRoleIds_taglist']/li/span[@title='delete']").click()
                self.listItem = self.driver.find_element_by_xpath(self.CustomerInfo_CustomerRoles_Guests_xpath)
            except Exception as io:
                self.listItem = self.driver.find_element_by_xpath(self.CustomerInfo_CustomerRoles_Guests_xpath)
        else:
            self.listItem = self.driver.find_element_by_xpath(self.CustomerInfo_CustomerRoles_Guests_xpath)

        time.sleep(4)
        self.driver.execute_script("arguments[0].click();", self.listItem)

    def selectManagerVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.CustomerInfo_CustomerRoles_Vendors_xpath))
        drp.select_by_visible_text(value)

    def inputAdminContent(self, adminContent):
        self.driver.find_element_by_xpath(self.CustomerInfo_AdminComment_xpath).clear()
        self.driver.find_element_by_xpath(self.CustomerInfo_AdminComment_xpath).send_keys(adminContent)

    def clickSaveButton(self):
        self.driver.find_element_by_xpath(self.CustomerInfo_Save_xpath).click()
        time.sleep(3)
