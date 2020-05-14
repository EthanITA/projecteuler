#   6 Sum square difference

""" 
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_of_squares_of_firsts(n):
    result = 0
    for i in range(n, 0, -1):
        result += i ** 2
    return result


def square_of_sum_of_firsts(n):
    result = 0
    for i in range(n, 0, -1):
        result += i
    return result ** 2


if __name__ == "__main__":

    print(abs(sum_of_squares_of_firsts(100) - square_of_sum_of_firsts(100)))
