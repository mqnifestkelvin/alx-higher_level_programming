#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        print("{}".format(my_list))
    elif idx > len(my_list) - 1:
        print("{}".format())
    elif idx > 0 and idx <= len(my_list) -1:
        list_a = my_list
        list_b = my_list.copy()
        list_b[idx] = element
        print("{}".format(list_b))
new_in_list([1,2,3,4,5,6], 3, 50)
