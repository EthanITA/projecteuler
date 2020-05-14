#   4 Largest palindrome product

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


from util import rev


def parlindromic(s):
    s = str(s)
    if (s == rev(s)):
        return True
    else:
        return False


def largest_n_digit_palindr(n=0):
    greatest_n = 10 ** n - 1
    a = []
    for i in range(greatest_n, greatest_n // 2, -1):
        for j in range(greatest_n, i - 1, -1):
            if parlindromic(str(i * j)):
                a.append(i * j)
    return max(a)


if __name__ == "__main__":
    print(largest_n_digit_palindr(3))
