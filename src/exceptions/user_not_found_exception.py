from src.exceptions.app_exception import AppException


class UserNotFoundException(AppException):

    def __init__(self, message: str):
        super().__init__(message)

