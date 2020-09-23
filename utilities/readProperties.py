import configparser
import os

from utilities.Constants import Constants

config = configparser.RawConfigParser()
ini_file = os.path.join(Constants.PARENTDIRECTORY, "Configurations", "config.ini")
config.read(ini_file)


class ReadConfig:

    @staticmethod
    def readApplicationURL():
        applicationURL = config.get("common values", "baseURL")
        return applicationURL

    @staticmethod
    def readUserEmail():
        username = config.get("common values", "useremail")
        return username

    @staticmethod
    def readPassword():
        password = config.get("common values", "password")
        return password

    @staticmethod
    def readErrorMessage():
        error = config.get("common values", "error_message")
        return error

