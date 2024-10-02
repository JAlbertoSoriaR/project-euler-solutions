def solve() :
    f_n = 1
    f_n_1 = 2
    f_n_2 = f_n + f_n_1
    s = 2

    while f_n_2 <= 4000000 :
        if f_n_2 % 2 == 0 :
           s += f_n_2
        f_n = f_n_1
        f_n_1 = f_n_2
        f_n_2 = f_n + f_n_1    

    return(s)