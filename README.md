# Discrete math project. Reachability matrix

## Description
In this project we analyzed how Warshall algorithm and how it works with unoriented graphs with different density

## Class Graph
This class is essential for the whole project. Inside there is a adjacency matrix. Also it has methods to get the number of vertices and the list of edges

## Graph Generator
This class uses Erdős-Rényi model to generate graphs. Returns a graph object with given number of vertices and given density

## Visualization
This class is designed to visualize graphs and matrixes
- visualize_graph - is for graphs. It uses matplotlib and networkx for visualization
- visualize_matrix - basically prints a matrix in prettier way

## WarshallAlgorithm class
Implemented warshall algorithm
Input: Graph object
Output: Reachability matrix for given Graph

## table.txt
This is the file with the results of the experiments. It contains amount of vertices, density and for each pair average execution of algorithm in seconds

## graphs.ipynb
This is file with the graphs of densities. The amount of experiments, list of number of vertices and list of densities afe all there

## Conversion class
This class contains simple convertion methods