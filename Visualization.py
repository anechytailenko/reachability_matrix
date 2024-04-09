import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from string import ascii_uppercase as letters
from Graph import *

class Visualization:
    # letters is easier to look at than numbers so table will look like - {0: 'A', 1: 'B', ..., 25: 'C'}
    table: dict[int, str] = {idx: letter for idx, letter in enumerate(letters)}
    @staticmethod
    def visualize_graph(graph: Graph) -> None:
        nx_graph = nx.Graph(np.array(graph.get_matrix()))
        labels = None
        if graph.get_number() <= 25:
            labels = {k: v for k, v in Visualization.table.items() if k < graph.get_number()}

        nx.draw(nx_graph, with_labels=True, labels=labels)

        plt.show()
    
    def visualize_matrix(matrix: list[list[int]], **optional) -> None:
        # printing without labels (A, B, C, etc) if we don't have enough letters or we don't want to
        if (len(matrix) > 26 or optional.get('labels') == False):
            for row in matrix:
                print(' '.join(map(str, row)))
            return 
        
        # printing with labels
        print(' ', end=' ')
        for el in letters[0:len(matrix)]:
            print(el, end=' ')
        print()
        for idx, row in enumerate(matrix):
            print(letters[idx] + ' ' + ' '.join(map(str, row)))  
            