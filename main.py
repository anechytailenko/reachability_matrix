from Visualization import *
from Graph import *
from GraphGenerator import *
from WarshallAlgorithm import *

graph = Graph([
    [0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0]
])

print(WarshallAlgorithm.get_reachability_matrix(graph))

Visualization.visualize(graph)