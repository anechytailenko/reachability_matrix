from Visualization import *
from Graph import *
from GraphGenerator import *
from WarshallAlgorithm import *

graph = GraphGenerator.generate(20, 10)

reachability_matrix = WarshallAlgorithm.get_reachability_matrix(graph)

Visualization.visualize_matrix(reachability_matrix, labels=True)

Visualization.visualize_graph(graph)
