#   9 Special Pythagorean triplet


""" 
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def pitagora_formula(a, b):
    return (a ** 2 + b ** 2)


def triplet_prod(a, b, c):
    return a * b * c


def find_triplet(d=1000):
    a = 0
    b = 0
    c = 0
    while c <= d:
        while b < c:
            a = d - c - b
            if pitagora_formula(a, b) == c ** 2:
                return [a, b, c, triplet_prod(a, b, c)]
            b += 1
        b = 0
        c += 1


print(find_triplet(1000))
