import random
from Graph import *

class GraphGenerator:
    @staticmethod
    def generate(n_of_vertices: int, density: int) -> Graph:
        # filling the matrix with 0 by default
        matrix: list[list[int]] = [[0 for j in range(n_of_vertices)] for i in range(n_of_vertices)]

        # setting the first half of the matrix to either 0 or 1
        for i in range(n_of_vertices):
            for j in range(n_of_vertices):
                if j > i:
                    matrix[i][j] = int(random.random() < (density / 100))
                elif j == i:
                    # filling the main diagonal with 0
                    matrix[i][i] = 0
                else:
                    # copying the symmetrcial value because it's an undirected graph
                    matrix[i][j] = matrix[j][i]
        
        return Graph(matrix)
    