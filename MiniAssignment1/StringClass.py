class StringClass:
    __input_str = ""
    __char_list = []

    def __init__(self):
        self.__input_str = input("Enter the String:")

    def get_length(self):
        return len(self.__input_str)

    @staticmethod
    def convert_into_list_char(input_str):
        return list(input_str)

    def get_str(self):
        return self.__input_str
