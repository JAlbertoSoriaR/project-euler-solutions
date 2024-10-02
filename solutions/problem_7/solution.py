def is_prime(n):
    if n == 1 :
       return False
    if n < 4 :
        return True
    if n % 2 == 0 or n % 3 == 0 :
        return False
    if n < 9 :
        return True 
    for i in range(5, int(n**0.5) + 1, 6) :
        if n % i == 0 or n % (i + 2) == 0 :
            return False
    return True     
    
def solve() :
    primes = [2]
    n = 3

    while len(primes) < 10001 :
        if is_prime(n) :
            primes.append(n)
        n += 2     
        
    return(primes[-1])
