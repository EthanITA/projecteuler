
#   1 Multiples of 3 and 5

""" 
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiples(m, max):

    # n*(n + 1)/2
    max = (max - 1) // m
    return m * (max * (max + 1) // 2)


if __name__ == "__main__":

    m_three = multiples(3, 10)
    m_five = multiples(5, 10)
    # remove duplicates
    mcd = multiples(5 * 3, 10)

    print(m_three + m_five - mcd)
