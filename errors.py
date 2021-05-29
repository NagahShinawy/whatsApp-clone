"""
created by Nagaj at 29/05/2021
"""

from constants import (
    APP_ERROR,
    INVALID_NAME_CODE,
    INVALID_NAME_MSG,
    GENERAL_ERROR_MSG,
    INVALID_PHONE_CODE,
    INVALID_PHONE_MSG,
)


class BaseAPIError(Exception):

    code = APP_ERROR
    message = GENERAL_ERROR_MSG
    additional_info = None

    def to_json(self):
        return {
            "code": self.code,
            "message": self.message,
            "additional_info": self.additional_info,
        }


class InvalidName(BaseAPIError):
    code = INVALID_NAME_CODE
    message = INVALID_NAME_MSG


class InvalidPhoneNumber(BaseAPIError):
    code = INVALID_PHONE_CODE
    message = INVALID_PHONE_MSG
