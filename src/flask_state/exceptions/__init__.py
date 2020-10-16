from abc import abstractmethod, ABC
from enum import unique, Enum


class FlaskStateResponse(ABC):
    @abstractmethod
    def get_code(self):
        pass

    @abstractmethod
    def get_msg(self):
        pass

    @abstractmethod
    def get_data(self):
        pass


# Success response
class SuccessResponse(FlaskStateResponse):
    def __init__(self, msg=None, data=None):
        if msg is None:
            msg = 'SUCCESS'
        self.code = 200
        self.msg = msg
        self.data = data

    def get_code(self):
        return self.code

    def get_msg(self):
        return self.msg

    def get_data(self):
        return self.data


# Error response
class ErrorResponse(FlaskStateResponse):
    def __init__(self, error_code):
        self.error_code = error_code
        self.data = []

    def get_code(self):
        return self.error_code.get_code()

    def get_msg(self):
        return self.error_code.get_msg()

    def get_data(self):
        return self.data


# Enumeration function
@unique
class ErrorCode(Enum):
    def get_code(self):
        return self.value.get('code')

    def get_msg(self):
        return self.value.get('msg')


# Custom exception
class CustomError(Exception):
    def __init__(self, error_info):
        super().__init__(self)
        self.error_info = error_info

    def __str__(self):
        return self.error_info
