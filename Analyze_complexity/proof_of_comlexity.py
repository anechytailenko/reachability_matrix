# we know that theoreticall time complexity is equal to O(n^3), it means that if there amount of verticies incresed by some number, then time complexity is incresed by this number^3
import numpy as np
import pandas as pd
with open('../table.csv', 'r') as file:
    file.readline()
    data = file.readlines()
    list_of_pairs = []
    list_of_density = []
    for item in data:
        list_by_pair = (item.removesuffix('\n')).split(',')
        list_of_pair = [float(item) for item in list_by_pair]
        list_of_pairs.append(list_of_pair)
        list_of_density.append(int(list_of_pair[1]))
    dict_by_density = {}
    list_of_density = sorted(list(set(list_of_density)))
    for density in list_of_density:
        dict_by_density[density] = []
        for item in list_of_pairs:
            if item[1] == density:
                dict_by_density[density].append([item[0],item[2]])
    dict_by_density = dict(sorted(dict_by_density.items()))
    print(dict_by_density)



def in_how_many_times_changes_time_by_density(list_by_density, in_difference):
    list_of_ratio =[]
    for item in list_by_density:
        amount_of_vertices = item[0]
        time_execution = item[1]
        for vertex in list_by_density:
            if vertex[0] == amount_of_vertices * in_difference:
                list_of_ratio.append((vertex[1]/time_execution))
    average_ratio = np.mean(list_of_ratio)
    return average_ratio

list_for_table = []
for density in list_of_density:
    for in_difference in range(2,11):
        list_by_density = dict_by_density[density]
        average_ratio = in_how_many_times_changes_time_by_density(list_by_density,in_difference)
        list_for_table.append([density, average_ratio,in_difference])


df = pd.DataFrame(data=list_for_table, columns= ['Density', 'Average_ratio_of_changes_in_time_execution','Ratio betweeen amounts_of_vertices'])
df.to_csv('complexity.csv', index=False)

