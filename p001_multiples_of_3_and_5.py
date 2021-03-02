"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiples(m, max):
    """
    T(m, max) = {n | ∀i. (0 < i ≤ max//m) ∧ (n = i×m)}
    :param m:
    :param max:
    :return:
    """
    return {i * m for i in range(1, (max // m) + 1)}


def solve():
    my_max = 999
    mult_3 = multiples(3, my_max)
    mult_5 = multiples(5, my_max)
    return sum(mult_3 | mult_5)


print(solve())
