"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from my_libs.my_funcs import product


def solve():
    """
    fun-fact:, all numbers in nums are prime!
    :return:
    """
    nums = [i for i in range(2, 21)]
    for i in range(len(nums)):
        n = nums[i]
        nums = [n_j // n if n_j % n == 0 and j > i else n_j for j, n_j in enumerate(nums)]
    return product(nums)


if __name__ == '__main__':
    print(solve())
