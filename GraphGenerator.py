import random
from Graph import *

class GraphGenerator:
    @staticmethod
    def generate(n_of_vertices: int) -> Graph:
        # filling the matrix with 0 by default
        matrix: list[list[int]] = [[0 for j in range(n_of_vertices)] for i in range(n_of_vertices)]

        # setting the first half of the matrix to either 0 or 1
        for i in range(n_of_vertices):
            for j in range(n_of_vertices):
                if j > i:
                    break
                matrix[i][j] = random.randint(0, 1)
        
        # filling the main diagonal with 1
        for i in range(n_of_vertices):
            matrix[i][i] = 1

        # as adj. matrix of undirected graph is symmentrical, 
        # so here mirroring the first half
        for i in range(n_of_vertices):
            for j in range(n_of_vertices):
                if j <= i: 
                    matrix[j][i] = matrix[i][j]
        
        return Graph(matrix)