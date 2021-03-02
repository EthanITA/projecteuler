import random

from my_libs.my_funcs import mod_exp


def miller_rabin(n, k):
    """
    Test miller-rabin presa dal PDF
    :param n:
    :param k:
    :return:
    """
    Ln = {a for a in range(n) if
          mod_exp(a, n - 1, n) == 1 and (mod_exp(a, n, n) == 1 or not mod_exp(a, n * 2, n) == 1)}
    for _ in range(k):
        a = random.randrange(2, n - 2)
        if a not in Ln:
            return "probably composite"
    return "prime"


def miller_rabin_optimized(n, k):
    """
    Questa funzione non genera Ln in modo tale da migliorare l'efficienza
    :param n:
    :param k:
    :return:
    """
    for _ in range(k):
        a = random.randrange(2, n - 2)
        if not (mod_exp(a, n - 1, n) == 1 and (mod_exp(a, n, n) == 1 or not mod_exp(a, n * 2, n) == 1)):
            return None
    return True


if __name__ == '__main__':
    n, k, u, j = int(1.933491197 * 10 ** 15 + 1), 1, 3517, 39
    n, k, u, j = 10376708097, 10, 1237, 23
    n, k, u, j = 73, 10, 9, 3
    n, k, u, j = 7, 5, 3, 1
    n, k, u, j = 1969, 5, 123, 4
    n, k = 996224275833, 10
    print(miller_rabin_optimized(n, k))
