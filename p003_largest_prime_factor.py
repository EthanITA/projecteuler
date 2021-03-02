"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from my_libs.my_funcs import get_smallest_prime_factor


def solve():
    n = 600851475143
    last_factor = 1
    while n != 1:
        prime_factor = get_smallest_prime_factor(n)
        n //= prime_factor
        last_factor = prime_factor
    return last_factor


if __name__ == '__main__':
    print(solve())
