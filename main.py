from Visualization import *
from Graph import *

graph = Graph([
    [1, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1]
])

print(graph)

Visualization.visualize(graph)