def largest_prime_factor(n):
        # Checking for factors of 2
        while n % 2 == 0:
              n //= 2
        # Now n is odd, check odd factors starting from 3
        factor = 3
        max_prime = 2  
        while factor * factor <= n:
              if n % factor == 0:
                 max_prime = factor
                 while n % factor == 0:
                       n //= factor
              factor += 2
        # If n is still greater than 1, it must be prime
        if n > 1:
           max_prime = n
        return max_prime

def solve() :
    
    n = 600851475143
    return(largest_prime_factor(n))
    
