class LoginError(Exception):
    def __init__(self, *args: object):
        super().__init__(args)
        self.message = args[0]
    pass

    def get_message(self):
        return self.message


class SignupError(Exception):
    def __init__(self, *args: object):
        super().__init__(args)
        self.message = args[0]
    pass

    def get_message(self):
        return self.message


class MovieError(Exception):
    def __init__(self, *args: object):
        super().__init__(args)
        self.message = args[0]
    pass

    def get_message(self):
        return self.message

