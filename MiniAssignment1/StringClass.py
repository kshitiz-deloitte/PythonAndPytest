class StringClass:
    in_string = ""

    def __int__(self):
        self.in_string = input("Enter the String: ")

    def get_length(self):
        return len(self.in_string)

    def convert_to_list(self):
        return list(self.in_string)


stringClass = StringClass()
stringClass.get_length()
stringClass.convert_to_list()
