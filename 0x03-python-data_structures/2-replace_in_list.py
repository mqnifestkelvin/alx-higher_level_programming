#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    list = my_list
    list[idx] = element
    print("{}".format(list))

replace_in_list([1,2,3,4,5], 3, 30)
