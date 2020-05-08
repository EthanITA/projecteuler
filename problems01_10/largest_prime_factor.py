#   3 Largest prime factor

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

import math


# about 11s to detect all primes from 1-2 000 000
def primality_test(n):
    for i in range(2, round(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# about 4s to detect all primes from 1-2 000 000
def wikipedia_primality_test(n):
    if n <= 3:
        return n >= 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, round(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def get_largest_prime_factor(n):
    for i in range(round(math.sqrt(n)), 1, -1):
        if (n % i == 0) and wikipedia_primality_test(i):
            return i
    return n


print(get_largest_prime_factor(600851475143))
