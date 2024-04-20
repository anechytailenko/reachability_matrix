
from GraphGenerator import *
from WarshallAlgorithm import *
import numpy as np
from prettytable import PrettyTable

list_of_n_vertices = [30,55,105, 155, 195]
list_of_density= [10,20,30,40,50]
AMOUNT_OF_EXPERIMENT = 40
dict_n_verticle = {}
for n_vertices in list_of_n_vertices:
    dict_n_verticle[n_vertices] = []
    for density in list_of_density:
        n = 0
        list_conduction_time = []
        while n < AMOUNT_OF_EXPERIMENT:
            graph = GraphGenerator.generate(n_vertices, density)
            reachability_matrix, conduction_time = WarshallAlgorithm.get_reachability_matrix(graph)
            list_conduction_time.append(conduction_time)
            n += 1
        dict_n_verticle[n_vertices].append((density, np.mean(list_conduction_time)))

print(dict_n_verticle)


result_table = PrettyTable(['Amount of verticles', 'Density','Average execution of algorithm'])
for n_vertices in dict_n_verticle.keys():
    list_value_given_amount_of_vericle = dict_n_verticle[n_vertices]
    for value in list_value_given_amount_of_vericle:
        density,time = value
        result_table.add_row([n_vertices, density, time])


