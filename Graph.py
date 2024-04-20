import copy

class Graph:
    def __init__(self, matrix: list[list[int]]):
        self.__matrix = matrix # adjacency matrix (матриця суміжності)
        self.__edges: list[tuple[int]] = []
        self.__calc_edges()
    
    def __calc_edges(self):
        for i in range(self.get_number()):
            for j in range(self.get_number()):
                if j > i and self.__matrix[i][j] == 1:
                    self.__edges.append((i, j))

    def get_n_of_edges(self):
        return len(self.__edges)

    def get_edges(self):
        return self.__edges

    def get_matrix(self):
        return copy.deepcopy(self.__matrix)
    
    def get_number(self):
        return len(self.__matrix)
    
    def __str__(self):
        result_string = ""
        for row in self.__matrix:
            result_string += ' '.join(map(str, row)) + '\n'
        return result_string.strip()