def safe_print_list_integers(my_list=[], x=0):
    hold = 0
    for i in range(x):
        try:
            if my_list[i] <= 0 or my_list[i] >= 0:
                clean = my_list[i]
                hold += 1
                print("{:d}".format(clean), end="")
            except (ValueError, TypeError):
                continue
        print("")
        return hold
