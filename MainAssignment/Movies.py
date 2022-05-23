from time import sleep

from Exceptions.UserDefinedException import FormulaError
from Utils.ExcelReaderAndWriter import ExcelHelper
from Utils.readCfg import get_from_config


class Movies:
    __SECTION = "movies"
    __COM_SECTION = "common_attribute"
    __EXL_SECTION = "excel_file"
    username = ""
    num_booked_tickets = 0

    def __init__(self, username):
        self.username = username
        self.movies_dict = {}
        self.movies_data = ExcelHelper(get_from_config(self.__EXL_SECTION, "movies_sheet"))
        self.movies_header = self.movies_data.get_headers_from_exl()
        flag = True
        while flag:
            print(f"******Welcome to BookMyShow {self.username}*******")
            count = 1
            movie_list = list(self.movies_data.get_data_from_exl())
            for movie in movie_list:
                print(f"{count}. {movie[0]}")
                count += 1
            print(f"{count}. Logout")
            ch = int(input(get_from_config(self.__COM_SECTION, "enter_option")))
            if ch == count:
                self.movies_data.close_app()
                break
            counter = 0
            movie_dict = dict(zip(self.movies_header, movie_list[ch - 1]))
            for key, value in movie_dict.items():
                counter += 1
                if counter > 7:
                    break
                print(key + ": " + str(value))
            print("1. Book Tickets\n2. Cancel Tickets\n3. Give User Rating")
            ch = int(input(get_from_config(self.__COM_SECTION, "enter_option")))
            if ch == 1:
                print("Timings:")
                movie_times = list(movie_dict["Timings"].split(" "))
                counter = 1
                for movie_time in movie_times:
                    print(str(counter) + ". " + movie_time)
                    counter += 1
                timing = int(input("Enter Timing:"))
                self.timing = movie_times[timing-1]
                print("Remaining Seats: " + str(int(movie_dict["Capacity"])))
                try:
                    num_of_seats = int(input("Enter Number of seats: "))
                    if num_of_seats > int(movie_dict["Capacity"]):
                        raise FormulaError("Not enough seats")
                    self.num_booked_tickets = num_of_seats
                    print("Thanks for booking.")
                except FormulaError as e:
                    print(e.message)
            elif ch == 2:
                try:
                    cancel_num = int(input("Number of seats you want to cancel: "))
                    if cancel_num > self.num_booked_tickets:
                        raise FormulaError("Not enough seats")
                    self.num_booked_tickets = self.num_booked_tickets - cancel_num
                except FormulaError as e:
                    print(e.message)

            elif ch == 3:
                self.user_rating = input("Provide Rating: ")
                print("User Rating: "+str(self.user_rating))
            else:
                print("Invalid Input")

#
# Movies("Test")
