from src.exceptions.app_exception import AppException


class InvalidCredentialException(AppException):

     def __init__(self, message: str):
         super().__init__(message)