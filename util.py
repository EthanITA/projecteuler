
""" This is my personal util module """


def factorial(n):
    """ 
    n: integer
    returns: integer

    The function compute the factorial of n

    5 -> 5 * 4 * 3 * 2 * 1 = 120
    """
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    """ 
    n: integer
    returns: integer

    The function compute the fibonacci of index n
    fib(n) = fib(n-1) + fib(n-2)

    12 -> 55 + 89 = 144
    """
    f1 = 1
    f2 = 1
    if n < 3:
        return 1
    else:
        while (n > 2):
            f1, f2 = f2, f1 + f2
            n -= 1
            print(f1, f2)
        return f2


def rev(s=""):
    """ 
    s: string
    returns: string

    The function reverse s

    1234abc --> cba4321
    """
    t = ""
    for i in range(0, len(s)):
        t += s[len(s) - 1 - i]
    return t


def primality_test(n):
    # about 11s to detect all primes from 1-2 000 000
    """
    NOTE: use primality_test_wikipedia() instead, about 3 times faster

    n: integer
    returns: boolean

    The function check if n is a prime number

    55 --> False, 101 --> True

    """
    for i in range(2, round(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def primality_test_wikipedia(n):
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

    for i in range(5, round(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def count_matching(a, b):
    """ 
    a: generic
    b: a type you can use the keyword "in"
    returns: integer

    The function counts how many a is in b
    ("a", "ababababa") --> 5
    (1, [1, 5, 8, 1]) --> 2
    """
    count = 0
    for i in b:
        if a == i:
            count += 1
    return count


