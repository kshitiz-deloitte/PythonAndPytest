from time import sleep

from Exceptions.UserDefinedException import FormulaError
from MainAssignment.Movies import Movies
from Utils.ExcelReaderAndWriter import ExcelHelper
from Utils.readCfg import get_from_config


class User:
    __SECTION = "user"
    __COM_SECTION = "common_attribute"
    __EXL_SECTION = "excel_file"

    def __init__(self):
        self.user_dict = {}
        self.user_data = ExcelHelper(get_from_config(self.__EXL_SECTION, "user_details_sheet"))
        self.user_header = self.user_data.get_headers_from_exl()
        flag = True
        while flag:
            print("******Welcome to BookMyShow*******")
            print(get_from_config(self.__SECTION, "user_login_options"))
            ch = int(input(get_from_config(self.__COM_SECTION, "enter_option")))
            if ch == 1:
                self.user_login()
            elif ch == 2:
                self.user_register()
            elif ch == 3:
                self.user_data.close_app()
                print("Logging out")
                sleep(3)
                flag = False
            else:
                print("invalid input")

    def user_login(self):
        print("******Welcome to BookMyShow*******")
        user_name_log = input("User: ")
        user_pwd_log = input("Password: ")

        try:
            if self.user_data.check_user_password(user_name_log, user_pwd_log):
                self.user_data.close_app()
                print("next")
                Movies(user_name_log)
            else:
                raise FormulaError("Login not successful")
        except FormulaError as e:
            print(e.message)

    def user_register(self):
        print("****Create new Account*****")
        for header in self.user_header:
            self.user_dict[header] = input(header + ": ")
        self.user_data.insert_data_into_excel(list(self.user_dict.values()))

# user = User()