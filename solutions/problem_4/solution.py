def solve() :
    
    def is_palindrome(n) :
        return str(n) == str(n)[::-1]

    largest_palindrome = 0

    for a in range(999, 99, -1) :
        for b in range(a, 99, -1) :  # Start b from a to avoid duplicate checks
            product = a * b
            if is_palindrome(product) :
                  if product > largest_palindrome :
                     largest_palindrome = product

    return(largest_palindrome)  


           



