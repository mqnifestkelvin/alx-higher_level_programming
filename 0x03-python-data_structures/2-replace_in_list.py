#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        print("{}".format(my_list))
    elif idx > len(my_list) - 1:
        print("{}".format(my_list))
    elif idx <= len(my_list) - 1 and idx > 0:
        list = my_list
        list[idx] = element
        print("{}".format(list))

replace_in_list([1,2,3,4,5], 3, 30)
