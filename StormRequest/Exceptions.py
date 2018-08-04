class UnsupportedMethod(Exception):
    def __init__(self, message, errors):
        super().__init__(message)


class NoPayload(Exception):
    def __init__(self):
        super().__init__()