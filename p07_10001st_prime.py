#   7 10001st prime

""" 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
from util import primality_test


def nth_prime_number(n):
    prime = 1
    while n > 0:
        prime += 1
        n -= primality_test(prime)
    return prime


if __name__ == "__main__":

    print(nth_prime_number(10001))
