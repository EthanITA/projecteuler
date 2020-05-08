""" 
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def sum_of_digits(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

print(sum_of_digits(fact(100)))