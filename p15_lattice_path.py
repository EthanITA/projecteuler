import numpy as np


class LatticePath():
    """ 
        The lattice paths I considered can go only up and left, it's complementar to down and right one,
        but it was easier implement using a growing index

        associated matrix           
        lattice path:    

            0   1   1   1              
            0   1   2   3                
            0   1   3   6                
            0   1   4   10               

        lattice path dim 3:

            1   2   3   4   x
        1   .   .   .   . 
        2   .   .   .   .
        3   .   .   .   .
        4   .   .   .   .
        y

        (y,x)
        (1,1) has 0 paths on its left
        (1,2) has 1 path on its left
        ....
        (3,3) has 3 possible routes, on its left, going up and left
        ....
        (4,4) has 10 possible paths on its left 
    """

    def __init__(self, dimension):
        self.__dim = dimension + 1
        self.__matrix = self.__create_lattice_path_as_matrix()

    def __create_lattice_path_as_matrix(self):

        matrix = np.empty((self.__dim, self.__dim), dtype=np.int64)

        # matrix is transposed because __create_lattice_row() create a column of the final matrix
        for i in range(self.__dim):
            matrix[i] = self.__create_lattice_row(matrix, i)
        return matrix.T

    def __create_lattice_row(self, matrix, row):

        result = []
        for col in range(self.__dim):
            if row == 0:
                result.append(0)
            elif row == 1:
                result.append(1)
            else:
                if col == 0:
                    result.append(1)
                else:
                    result.append(matrix[row-1][col] + result[-1])
        return result

    def get_number_of_routes(self):
        if self.__dim == 0:
            return 1
        else:
            return self.__solve_lattice_path_matrix()

    def __solve_lattice_path_matrix(self):
        total_paths = 0
        for i in range(self.__dim):
            total_paths += self.__matrix[i][-1]
        return total_paths

    def __str__(self):
        return str(self.__matrix)

if __name__ == "__main__":
    
    lattice = LatticePath(20)

    print(lattice)
    print(lattice.get_number_of_routes())
