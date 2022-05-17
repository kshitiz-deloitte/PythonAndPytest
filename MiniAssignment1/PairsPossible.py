from MiniAssignment1.StringClass import StringClass


class PairsPossible(StringClass):
    __pair_list = []

    def all_possible_pairs(self):
        input_string = self.get_str()
        self.__pair_list = [[a, b] for idx, a in enumerate(self.convert_into_list_char(input_string))
                            for b in self.convert_into_list_char(input_string)[idx + 1:]]

    def get_all_possible_pairs(self):
        return self.__pair_list

    def print_pairs(self):
        print("All Possible Pairs of the Given List:", end=" ")
        for i in self.__pair_list:
            print(i, end=" ")
        print()
