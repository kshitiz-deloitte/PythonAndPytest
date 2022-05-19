flag = True


def duplicate_elements():
    array_list = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]
    for i in array_list:
        ele_count = {}
        for k in i:
            if k in ele_count.keys():
                ele_count[k] += 1
            else:
                ele_count[k] = 1
        for key, value in ele_count.items():
            if value > 1:
                print(key, "->", value, end=",")
        print()


def merge_lists():
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    fin_list = []
    for i in list1:
        for j in list2:
            fin_list.append(i+j)
    print(fin_list)


def iterate_nested_list(list1, sub_list):
    global flag
    for item in list1:
        if type(item) is list:
            iterate_nested_list(item, sub_list)
        if flag and type(item) is list:
            item += sub_list
            flag = False


def nested_list_prob(nested_list, sub_list):
    iterate_nested_list(nested_list, sub_list)
    print(nested_list)


def merge_list_to_dict(keys, value):
    res_dict = {}
    for i in range(len(keys)):
        res_dict[keys[i]] = value[i]
    print(res_dict)


duplicate_elements()
merge_lists()
nested_list_prob(["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"], ["h", "i", "j"])
merge_list_to_dict(["Ten", "Twenty", "Thirty"], [10, 20, 30])
