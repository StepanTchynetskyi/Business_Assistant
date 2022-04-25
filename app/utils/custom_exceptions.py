class UniqueFieldException(Exception):
    def __init__(self, message: str):
        self.message = message


class LoginException(Exception):
    def __init__(self):
        self.message = "Failed to Login"
