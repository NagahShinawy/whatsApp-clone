"""
created by Nagaj at 29/05/2021
"""
import phonenumbers
from errors import InvalidName, InvalidPhoneNumber


class UserProfile:
    def __init__(self, name, phone, image=None, boi=""):
        self.name = name
        self.phone = phone
        self.image = image
        self.boi = boi
        self.groups = []

    def __str__(self):
        return f"{self.name.title()} {self.phone}"

    def __setattr__(self, attribute, value):
        if attribute == "name":
            self.__validate_name(value)
        if attribute == "phone":
            self.__validate_phone(value)

        super().__setattr__(attribute, value)

    @staticmethod
    def __validate_name(name):
        if len(name) not in range(3, 21):
            raise InvalidName(InvalidName.message)

    @staticmethod
    def __validate_phone(mobile_number):
        number = phonenumbers.parse(mobile_number)
        is_valid_mobile_number = phonenumbers.is_valid_number(number)
        if not is_valid_mobile_number:
            raise InvalidPhoneNumber(
                InvalidPhoneNumber.message.format(mobile_number=mobile_number)
            )
