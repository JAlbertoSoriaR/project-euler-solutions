
def solve() :

    n = 100
    sum = n*(n+1)/2
    sum_of_squares = n*(n+1)*(2*n+1)/6
    r = sum**2 - sum_of_squares
    return(r)