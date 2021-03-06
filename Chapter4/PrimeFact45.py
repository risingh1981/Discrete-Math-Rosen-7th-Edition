import math
import time
# Chapter 4(Number Theory) Computer Projects #5
# Performance: Taking 0.246232 seconds to factor 123456786.
# Recreate program with Pollard’s Rho Algorithm for Prime Factorization.
# https://www.geeksforgeeks.org/pollards-rho-algorithm-prime-factorization/
# Other algorithms also available: https://en.wikipedia.org/wiki/Integer_factorization
# Learn about: Congruence of squares. Principle used in many factorization algorithms.

def main():
    n = 123456786
    #n = 147
    factorization =""
    pi = 1
    start = time.perf_counter_ns()
    while (n > 1):
        while not(prime(pi)):
            pi += 1
        count = 0
        print(f"Prime: {pi} , {pi}^2: {pi * pi} n: {n}")
        while(n%pi == 0):
            n=n/pi
            count += 1
        if (count != 0):
            factorization = factorization + str(pi) + "^" + str(count) + "  "
        pi += 1
        if (pi * pi >= n and n !=1):
            factorization = factorization + str(int(n)) + "^1"
            n = 1

    end = time.perf_counter_ns()
    print(factorization)
    print(f"Start time: {start} End time: {end}  Elapsed time: {end - start} nanoseconds or {(end - start)/(10**9)} Seconds.")



def prime(n):   
    if (n <= 3):
        return (n > 1)
    if (n % 2 == 0) or (n % 3 == 0):
        return False
    # This part uses fact that all numbers can be represented in form 6k + x, where k is an int => 0 
    # and x = {0,1,2,3,4,5}. Multiples of 6k + {0,2,3,4} already rules out above. Just have to check
    # multiples of 6k - 1 and 6k + 1 less than sqrt(n).
    i = 5 # Initial value is 6(1) - 1 = 5 and 6(1) + 1 = 7
    while (i ** 2 <= n):
        if (n % i == 0) or (n % (i+2)) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    main()



