"""
created by Nagaj at 29/05/2021
"""
import phonenumbers

from core import BaseMixin
from errors import InvalidName, InvalidPhoneNumber
from group import Group


class UserProfile(BaseMixin):
    def __init__(self, name, phone, image=None, boi=""):
        super().__init__()
        self.name = name
        self.phone = phone
        self.image = image
        self.boi = boi
        self.groups = self.objs

    def is_exist(self, group):
        return group in self.groups

    def join_group(self, group: Group):
        if not self.is_exist(group):
            self.groups.append(group)
            group.members.append(self)
            print(f"User <{self.phone}> joined the group <{group.name}>")

    def leave_group(self, group):
        if self.is_exist(group):
            self.groups.remove(group)
            group.members.remove(self)
            print(f"User <{self.phone}> has left the group <{group.name}>")

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
