import numpy as np

def sieve_of_eratosthenes(n):
        # Initialize the list of boolean values
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  

        # Mark non-prime numbers
        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
               for multiple in range(p * p, n + 1, p):
                   is_prime[multiple] = False

        # Collect all prime numbers
        primes = [num for num, prime in enumerate(is_prime) if prime]
        return primes

def solve() :

    n = 20 
    primes = sieve_of_eratosthenes(n)
    factors = [0] * len(primes)
    for i, p in enumerate(primes) :
        f = p
        while f <= n  :
            factors[i] = f
            f *= p     
    
    return(np.prod(factors))

 