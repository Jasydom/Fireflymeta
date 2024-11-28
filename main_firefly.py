#################################################################################################################################
############################################---------Initialisation----------####################################################
#################################################################################################################################


import pandas as pd
import function_firefly
import matplotlib.pyplot as plt
import ini
import numpy as np
import math
import time

start = time.time()


n = 0

Time = pd.read_excel('Time_Table.xlsx')
Time = Time.iloc[1:]
Time.set_index(Time.columns[0], inplace=True)


Cost = pd.read_excel('Cost_Table.xlsx')
Cost = Cost.iloc[1:]
Cost.set_index(Cost.columns[0], inplace=True)

# Iniatilisation population
population = []

for _ in range(ini.Number_firefly):
  matrix = np.zeros((ini.num_nodes, ini.num_task), dtype=int)
  for i in range(ini.num_task):
    random_node = np.random.randint(ini.num_nodes)
    matrix[random_node, i] = 1

  population.append(matrix.copy())
  
  
#iniatilisation population future
population_future = population

resultat_cost = []
for i in range (ini.Number_firefly):
  resultat = function_firefly.Cost_function(Cost, population[i], ini.num_nodes, ini.num_task)
  resultat_cost.append(resultat)
  
resultat_time_execution = []
for i in range (ini.Number_firefly):
  resultat = function_firefly.Time_Execution_function(Time, population[i], ini.num_nodes, ini.num_task)
  resultat_time_execution.append(resultat) 
  
plt.figure(figsize=(10, 6))
plt.plot(resultat_time_execution, resultat_cost, marker='.', linestyle='')
plt.title('Temps d\'exécution vs Coût à l\'initialisation')
plt.xlabel('Temps d\'exécution')
plt.ylabel('Coût')
plt.grid(True)
plt.savefig('population initial.png')  # Sauvegarde le graphique en tant qu'image PNG
plt.show()

function_firefly.somme(resultat_time_execution, resultat_cost, ini.Number_firefly)


while n < ini.N:

  


  resultat_time_execution = []
  for i in range (ini.Number_firefly):
    resultat = function_firefly.Time_Execution_function(Time, population[i], ini.num_nodes, ini.num_task)
    resultat_time_execution.append(resultat)
  resultat_cost = []
  for i in range (ini.Number_firefly):
    resultat = function_firefly.Cost_function(Cost, population[i], ini.num_nodes, ini.num_task)
    resultat_cost.append(resultat)

  for firefly in range (ini.Number_firefly):
    ID_resultat_cost = {i: value for i, value in enumerate(resultat_cost)}
    sup_cost = {key: value for key, value in ID_resultat_cost.items() if value < resultat_cost[firefly]}

    ID_resultat_time_execution = {i: value for i, value in enumerate(resultat_time_execution)}
    sup_time = {key: value for key, value in ID_resultat_time_execution.items() if value < resultat_time_execution[firefly]}

    tableau_inner_join = {}

    for cle in sup_cost:
        if cle in sup_time:
            tableau_inner_join[cle] = (sup_cost[cle], sup_time[cle])
    if len(tableau_inner_join) == 0:
      cost_best = resultat_cost[firefly]
      time_best = resultat_time_execution[firefly]
      best = firefly
    else :
      best, cost_best, time_best = function_firefly.crowd_distance(tableau_inner_join, resultat_cost[firefly], resultat_time_execution[firefly])
  
    
    
    random = function_firefly.function_random(ini.alpha, ini.num_task, ini.num_nodes)
    
    population_future[firefly] = function_firefly.addition_binaire(population[firefly], population[best], ini.Beta[firefly], random, ini.num_nodes, ini.num_task)

  population = population_future

  n = n + 1
  
######################################################################################################################################
##################################################---------------Conclusion----------------###########################################
######################################################################################################################################  

resultat_cost = []
for i in range (ini.Number_firefly):
  resultat = function_firefly.Cost_function(Cost, population[i], ini.num_nodes, ini.num_task)
  resultat_cost.append(resultat)

resultat_time_execution = []
for i in range (ini.Number_firefly):
  resultat = function_firefly.Time_Execution_function(Time, population[i], ini.num_nodes, ini.num_task)
  resultat_time_execution.append(resultat)

plt.figure(figsize=(10, 6))
plt.plot(resultat_time_execution, resultat_cost, marker='.', linestyle='')
plt.title('Temps d\'exécution vs Coût')
plt.xlabel('Temps d\'exécution')
plt.ylabel('Coût')
plt.grid(True)
plt.savefig('population final.png')  # Sauvegarde le graphique en tant qu'image PNG
plt.show()

function_firefly.somme(resultat_time_execution, resultat_cost, ini.Number_firefly)

end = time.time()

# Calculer le temps écoulé
last = end - start 

print("Temps écoulé:", last, "secondes")

  
  