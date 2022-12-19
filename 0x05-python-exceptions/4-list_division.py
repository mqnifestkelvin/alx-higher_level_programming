#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_0 = []
    for i in range(list_length):
        try:
            hold = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            hold = 0
        except TypeError:
            print("wrong type")
            hold = 0
        except IndexError:
            print("out of range")
            hold = 0
        finally:
            list_0.append(hold)
    return list_0
