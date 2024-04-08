class Graph:
    def __init__(self, matrix: list[list[int]]):
        self.__matrix = matrix # adjacency matrix (матриця суміжності)
    
    def get_matrix(self):
        return self.__matrix
    
    def get_number(self):
        return len(self.__matrix)
    
    def __str__(self):
        result_string = ""
        for row in self.__matrix:
            result_string += ' '.join(map(str, row)) + '\n'
        return result_string.strip()