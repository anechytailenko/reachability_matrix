import copy
from Graph import *

class WarshallAlgorithm:
    @staticmethod
    def get_reachability_matrix(graph: Graph) -> list[list[int]]:
        matrix = copy.deepcopy(graph.get_matrix())
        n_of_vertices = graph.get_number()
        for k in range(0, n_of_vertices):
            for i in range(0, n_of_vertices):
                for j in range(0, n_of_vertices):
                    matrix[i][j] = int(bool(matrix[i][j]) or (bool(matrix[i][k]) and bool(matrix[k][j])))
        
        for i in range(0, n_of_vertices):
            matrix[i][i] = 1
        
        return matrix
