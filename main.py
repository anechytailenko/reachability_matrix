from Visualization import *
from Graph import *
from GraphGenerator import *
from WarshallAlgorithm import *

graph = GraphGenerator.generate(7, 30)

reachability_matrix = WarshallAlgorithm.get_reachability_matrix(graph)

Visualization.visualize_matrix(reachability_matrix)

Visualization.visualize_graph(graph)
