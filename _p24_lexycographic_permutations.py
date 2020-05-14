""" A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9? """


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def perm(digits):
    array = []
    if len(digits) < 2:
        return
    elif len(digits) == 2:
        array.append(digits[0] + digits[1])
        array.append(digits[1] + digits[0])
        return array
    else:
        first_d = digits.pop(0)


def lex_perm(digits=[]):
    return sorted(perm(list(map(str, digits))))


def my_lex_perm(start_digit, index, other_digits=[]):
    perm_array = lex_perm(other_digits)
    return str(start_digit) + str(perm_array[index - 1])


def gen_digits(n, skip):
    digits = []
    for i in range(n):
        if i not in skip:
            digits.append(i)
    return digits


def solve():
    """ n: int
        i: int
        returns the i-th element of the n digits of lexicographic permutation """

    # some quick math to reduce the complexity of the algorithm
    # the purpose is to avoid the computation of all permutations under i-th lex perm
    # now I can compute i - fact(n)//n times instead of fact(n) times or i times

    # number of permutation for each digit
    n_permutations_digit = fact(n) // n
    # which digit to start from
    start_digit = i // n_permutations_digit
    # shifting my index
    shifted_i = i - start_digit*n_permutations_digit
    return my_lex_perm(start_digit=start_digit, index=shifted_i, other_digits=gen_digits(n, skip=[start_digit]))


if __name__ == "__main__":
    solve()
