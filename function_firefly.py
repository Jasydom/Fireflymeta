def Cost_function(Cost, matrix, num_nodes, num_task):

  somme = 0
  for i in range (0, num_task):
    for j in range (0, num_nodes):
      string_task = "Task_" + str(i+1)
      string_Node = "Node_" + str(j+1)
      ajout = Cost.loc[string_Node,string_task] * matrix[j][i]
      somme += ajout
  return somme

def Time_Execution_function(Time, matrix,  num_nodes, num_task):

  somme = 0
  for i in range (0, num_task):
    for j in range (0, num_nodes):
      string_task = "Task_" + str(i + 1)
      string_Node = "Node_" + str(j + 1)
      ajout = Time.loc[string_Node,string_task] * matrix[j][i]
      somme += ajout
  return somme

def crowd_distance(tableau_inner_join, firefly_cost, firefly_time):
  import numpy as np
  max = 0
  for id, valeur in tableau_inner_join.items():
    distance = np.sqrt((valeur[0] - firefly_cost) ** 2 + (valeur[1] - firefly_time) ** 2)
    if distance > max:
      max = distance
      time_best = valeur[1]
      cost_best = valeur[0]
      best = id

    
  return (best, cost_best, time_best)

def function_random(alpha, num_task, num_nodes):
    
  import numpy as np
  matrice = np.random.rand(num_nodes, num_task)

  # Soustraire 0.5 à chaque élément de la matrice
  matrice -= 0.5
  matrice *= alpha
  return matrice

def addition_binaire(luciole_origin, luciole_best, beta, mutation, num_nodes, num_iterations):
    import numpy as np
    # Calcul du résultat continu
    resultat_continu = luciole_origin + beta * (luciole_best - luciole_origin) + mutation
    
    # Trouver l'indice du maximum dans chaque colonne
    max_indices = np.argmax(resultat_continu, axis=0)
    
    # Créer une matrice vide avec les mêmes dimensions que resultat_continu
    resultat = np.zeros((num_nodes, num_iterations), dtype=int)
    
    # Mettre 1 à l'indice du maximum dans chaque colonne
    for col, row in enumerate(max_indices):
        resultat[row, col] = 1
    
    # Mettre les autres éléments à 0
    for col in range(resultat.shape[1]):
        for row in range(resultat.shape[0]):
            if row != max_indices[col]:
                resultat[row, col] = 0
    
    return resultat

def somme(resultat_time_execution, resultat_cost, Number_firefly):
    somme_time = 0
    somme_cost = 0
    for i in range (len(resultat_time_execution)):
        somme_time += resultat_time_execution[i]
    for i in range (len(resultat_cost)):
        somme_cost += resultat_cost[i]
    
    print("moyenne time:", somme_time/Number_firefly)
    print("moyenne cost:", somme_cost/Number_firefly)
    