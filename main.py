from Visualization import *
from Graph import *
from GraphGenerator import *
from WarshallAlgorithm import *

graph = GraphGenerator.generate(15, 60)

print(graph.get_n_of_edges())

reachability_matrix, conduction_time = WarshallAlgorithm.get_reachability_matrix(graph)

# Visualization.visualize_matrix(reachability_matrix, labels=True)

print(graph.get_edges())

Visualization.visualize_graph(graph, labels=False)
