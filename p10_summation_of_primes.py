#   10 Summation of primes


""" 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
from util import wikipedia_primality_test


def sum_primes_below(n):
    summation = 0
    for i in range(2, n):
        if wikipedia_primality_test(i):
            summation += i
    return summation


if __name__ == "__main__":

    print(sum_primes_below(2000000))
