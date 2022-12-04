#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if "c" != i and "C" != i:
            print("{}".format(i), end="")
    print()

no_c("Come on lads come with me lets go where no men dare can cum")
