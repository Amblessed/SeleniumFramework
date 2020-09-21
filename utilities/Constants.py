import random
import string
from pathlib import Path


class Constants:
    MALE = "Male"
    FEMALE = "Female"
    EXPECTED_TITLE = "Dashboard / nopCommerce administration"
    REGISTERED = "Registered"
    ADMINISTRATORS = "Administrators"
    GUESTS = "Guests"
    VENDORS = "Vendors"
    PARENTDIRECTORY = Path(__file__).parent.parent

    VENDORS_ONE = "Vendor 1"
    VENDORS_TWO = "Vendor 2"

    @staticmethod
    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    @staticmethod
    def random_email_generator():
        first_part = Constants.get_random_string(4)
        second_part = Constants.get_random_string(6)
        email = first_part + "." + second_part + "@gmail.com"
        return email
