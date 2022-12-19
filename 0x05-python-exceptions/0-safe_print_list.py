#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    hold = 0
    for i in range(x):
        try:
            list_0 = my_list[i]
            print("{}".format(list_0), end="")
            hold += 1
        except IndexError:
            break
    print("")
    return hold
