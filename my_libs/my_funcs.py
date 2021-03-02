from functools import reduce
from time import time
from typing import Generator, Iterable


def all_factors(n: int) -> int:
    factors = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors += 1
    return factors


def truncate(value, n_decimals: int) -> float:
    """
    truncate "value" up to length of "n_decimals"
    :param value:
    :param n_decimals:
    :return:
    """
    integer, decimal = str(float(value)).split(".")
    return float(".".join([integer, decimal[:n_decimals]]))


def timer(func):
    """
    time a function, use it as decorator
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        t = time()
        result = func(*args, **kwargs)
        print(f"time: {truncate((time() - t) * 1000, 5)}ms")
        return result

    return wrapper


def perfect_square(n) -> bool:
    return n ** (1 / 2) - n ** (1 / 2) % 1 == n ** (1 / 2)


def primality_test_wikipedia(n) -> bool:
    # about 4s to detect all primes from 1-2 000 000
    """
    n: integer
    returns: boolean

    The function check if n is a prime number

    55 --> False, 101 --> True
    """
    if n <= 3:
        return n >= 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def next_prime(n) -> int:
    """
    return the next prime after n, n+=2 because we can skip numbers multiples of 2
    :param n:
    :return:
    """
    # base case
    if n == 1:
        return 2
    elif n == 2:
        return 3

    if n % 2 == 0:
        n += 1
    else:
        n += 2
    while primality_test_wikipedia(n) is False:
        n += 2
    return n


def get_prime(n) -> int:
    if n < 1:
        return 1
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    prime = 5
    n -= 3
    while n > 0:
        prime = next_prime(prime)
        n -= 1
    return prime


def sum_squares(n: int, exp: int) -> int:
    return sum(i ** exp for i in range(1, n + 1))


def mod_exp(a, x, N):
    r = 1
    while x > 0:
        if x % 2 == 1:
            r = (r * a) % N
        x = x // 2
        a = a ** 2 % N
    return r


def square_sums(n: int, exp: int) -> int:
    return sum(i for i in range(1, n + 1)) ** exp


def product(nums: Iterable):
    """
    similar to sum(), but it computes product
    :param nums:
    :return:
    """
    return reduce(lambda x, y: x * y, nums)


def gen_triangle_numbers() -> Generator:
    sum_tn = 0
    i = 0
    while True:
        i += 1
        sum_tn += i
        yield sum_tn


def get_smallest_prime_factor(n) -> int:
    """
    given n, return a prime factor of n
    :param n:
    :return:
    """
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    prime = 5
    while n % prime != 0:
        prime = next_prime(prime)
    return prime


def is_palidrome(n) -> float:
    return str(n) == str(n)[::-1]
