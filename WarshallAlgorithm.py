import copy
from Graph import *
from datetime import datetime
from Conversions import *

class WarshallAlgorithm:
    @staticmethod
    def get_reachability_matrix(graph: Graph) :
        matrix = copy.deepcopy(graph.get_matrix())
        n_of_vertices = graph.get_number()

        start_time = Conversions.convert_datetime_to_float(datetime.now().strftime("%M.%S.%f"))

        for k in range(0, n_of_vertices):
            for i in range(0, n_of_vertices):
                for j in range(0, n_of_vertices):
                    matrix[i][j] = int(bool(matrix[i][j]) or (bool(matrix[i][k]) and bool(matrix[k][j])))

        for i in range(0, n_of_vertices):
            matrix[i][i] = 1

        end_time = Conversions.convert_datetime_to_float(datetime.now().strftime("%M.%S.%f"))
        conduction_time = end_time - start_time
        
        return matrix, conduction_time
