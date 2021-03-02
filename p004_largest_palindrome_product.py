"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from my_libs.binarytree import BinaryTree
from my_libs.my_funcs import is_palidrome


def solve_tree_naive(product_tree=BinaryTree().insert_values(999, 999)):
    if is_palidrome(product_tree.value_product):
        return product_tree.value
    else:
        n1, n2 = product_tree.value
        product_tree.left = BinaryTree().insert_values(n1 - 1, n2)
        product_tree.right = BinaryTree().insert_values(n1, n2 - 1)
        return max(solve_tree_naive(product_tree.left), solve_tree_naive(product_tree.right))


def solve_tree(product_tree=BinaryTree().insert_values(999, 999), left=False):
    """
    This algorithm skips duplicates sub-trees
    :param product_tree:
    :param left:
    :return:
    """
    if is_palidrome(product_tree.value_product):
        return product_tree.value_product, product_tree.value
    else:
        n1, n2 = product_tree.value
        if n1 == n2:
            return solve_tree(BinaryTree().insert_values(n1 - 1, n2))
        else:
            product_tree.left = BinaryTree().insert_values(n1 - 1, n2)
            product_tree.right = BinaryTree().insert_values(n1, n2 - 1)
            if left:
                return solve_tree(product_tree.left, left)
            else:
                return max(solve_tree(product_tree.left, left=True), solve_tree(product_tree.right))


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1500)
    print(solve_tree())
