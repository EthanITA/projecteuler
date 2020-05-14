

import time

start = time.time()
print(start)


class Tree:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def __init__(self):
        self.right = None
        self.left = None
        self.data = None


# Funzione che preso un array di dimensione crescente (di 1) e la classe albero biario, restituisce l'albero binario associato
""" 
[['75'],
['95', '64'],
['17', '47', '82']] 

        75
    95      64
17      47      82
i child di 64 sono 47 e 82
i child di 95 sono 17 e 47
"""


def array_to_tree(array, tree, index_i=0, index_j=0):
    try:
        tree.data = int(array[index_i][index_j])
        tree.left = array_to_tree(
            array, Tree(), index_i=index_i + 1, index_j=index_j)
        tree.right = array_to_tree(
            array, Tree(), index_i=index_i + 1, index_j=index_j + 1)
        return tree
    except:
        return None


def array_to_tree_optimized(array, tree, index_i=0, index_j=0):
    # array[i][j]: i array grande, j sotto array
    try:
        tree.data = int(array[index_i][index_j])
        try:
            array[index_i + 1]
            tree.left = array_to_tree(
                array, Tree(), index_i=index_i + 1, index_j=index_j)
            tree.right = array_to_tree(
                array, Tree(), index_i=index_i + 1, index_j=index_j + 1)
        except:
            tree.left = None
            tree.right = None
        return tree
    except:
        return None

# problema: visualizzare un albero


f = open("Problem_16.txt", "r")
root = Tree()
tree_array = []
for line in f.readlines():
    tree_array.append(line.split())

my_tree = array_to_tree_optimized(tree_array, root)

end = time.time()
print(end - start)
