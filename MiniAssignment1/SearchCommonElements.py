from MiniAssignment1.StringClass import StringClass


class SearchCommonElements(StringClass):
    __common = []

    def common_elements(self, input_string_1):
        input_string = self.get_str()
        list1 = self.convert_into_list_char(input_string)
        list2 = self.convert_into_list_char(input_string_1)
        elements = {}
        for i in list1:
            if i in elements.keys():
                elements[i] += 1
            else:
                elements[i] = 1
        for k in list2:
            if k in elements.keys():
                self.__common += [k]

    def print_common_elements(self):
        print("Common Elements: ", self.__common)
