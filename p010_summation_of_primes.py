"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from my_libs.my_funcs import next_prime


def solve():
    prime_prod = 0
    prime = 2
    while prime < 2000000:
        prime_prod += prime
        prime = next_prime(prime)
    return prime_prod


if __name__ == '__main__':
    print(solve())
