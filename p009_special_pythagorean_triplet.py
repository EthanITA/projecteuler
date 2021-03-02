"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a² + b² = c²
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def solve():
    """
    System of equations:
        -----
        | a² + b² = c² => a² + b² = (1000 - (a + b))² => ... =>  a = (500000-1000*b)/(1000-b)
        | a + b + c = 1000 => c = 1000 - (a + b)
        -----
    That means "b" is free
    The problem is limited only with natural numbers, "a" can produce float numbers
    :return:
    """
    # "b" will never reach 1000 since "a" and "c" exist, the solution will be found in "1000-c-a" steps
    for b in range(1, 1000):
        a = (500000 - 1000 * b) // (1000 - b)
        c = 1000 - a - b
        if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
            return a * b * c


if __name__ == '__main__':
    print(solve())
