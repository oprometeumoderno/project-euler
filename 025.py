def solution025():
    f_n_minus_2 = 1
    f_n_minus_1 = 1
    f_n = 2
    i = 4

    found = False
    while not found:
        f_n_minus_1 = f_n_minus_2
        f_n_minus_2 = f_n
        f_n = f_n_minus_1 + f_n_minus_2
        if len(str(f_n)) >= 1000:
            found = True
        else:
            i += 1
    return i
