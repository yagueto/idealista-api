class APIException(Exception):
    def __init__(self, message: str, response: dict | None = None):
        super().__init__(message)
        self.response = response


class AuthenticationException(APIException):
    pass
