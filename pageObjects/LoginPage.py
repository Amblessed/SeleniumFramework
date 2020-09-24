
class LoginPage:
    WebElement_Username_id = "Email"
    WebElement_Password_id = "Password"
    WebElement_Password_xpath = "//div[@class='message-error validation-summary-errors']"
    WebElement_ButtonLogin_xpath = "//input[@type='submit']"
    WebElement_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.WebElement_Username_id).clear()
        self.driver.find_element_by_id(self.WebElement_Username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.WebElement_Password_id).clear()
        self.driver.find_element_by_id(self.WebElement_Password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.WebElement_ButtonLogin_xpath).click()

    def getErrorMessage(self):
        error_message = self.driver.find_element_by_xpath(self.WebElement_Password_xpath).text
        return error_message

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.WebElement_logout_linktext).click()
