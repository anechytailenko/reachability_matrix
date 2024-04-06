class Graph:
    def __init__(self, matrix: list[list[int]]):
        self.__matrix = matrix # adjacency matrix (матриця суміжності)
    
    def get_matrix(self):
        return self.__matrix
    
    def get_number(self):
        return len(self.__matrix)
    