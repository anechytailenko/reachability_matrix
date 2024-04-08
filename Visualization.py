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
    
    def visualize_matrix(matrix: list[list[int]]) -> None:
        for row in matrix:
            print(row)
