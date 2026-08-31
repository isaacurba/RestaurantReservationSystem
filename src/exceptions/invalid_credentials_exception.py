class invalid_credentials_exception(Exception):

     def __init__(self, message: str):
         super().__init__(message)