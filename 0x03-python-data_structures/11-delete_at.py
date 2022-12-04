#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx > 0  and len(my_list) < idx:
        my_list.remove(my_list[idx])
        print("{}".format(my_list))
    else:
        print("{}".format(my_list))
delete_at([1,2,3,4,5], 3)
