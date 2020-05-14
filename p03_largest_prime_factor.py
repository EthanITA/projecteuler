#   3 Largest prime factor

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

import math
from util import primality_test_wikipedia


def get_largest_prime_factor(n):
    for i in range(round(math.sqrt(n)), 1, -1):
        if (n % i == 0) and primality_test_wikipedia(i):
            return i
    return n


if __name__ == "__main__":
    print(get_largest_prime_factor(600851475143))
