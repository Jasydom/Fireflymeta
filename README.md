# **Firefly Optimization Algorithm**

## **Description**
This project implements the Firefly Optimization Algorithm to minimize task execution time and cost in a distributed network. The algorithm uses Pareto optimization, crowd distance, and mutation strategies to refine solutions iteratively.

---

## **Files**
- **`Cost_Table.xlsx`**: Contains cost data for task execution on different nodes.
- **`Time_Table.xlsx`**: Contains execution time data for tasks on nodes.
- **`function_firefly.py`**: Core functions for the Firefly algorithm.
- **`main_firefly.py`**: Main script to execute the Firefly algorithm.
- **`ini.py`**: Initialization of tasks and nodes.
- **`population_initial.png`**: Visualization of the initial population.
- **`population_final.png`**: Visualization of the optimized population.

---

## **Steps**
1. **Initialize Fireflies**: Define initial task positions and parameters.
2. **Evaluate Solutions**: Calculate cost and execution time for each firefly.
3. **Optimize**: Use Pareto and mutation techniques to improve task allocations.
4. **Results**: Generate final visualizations and optimized metrics.

---

## **Results**
The algorithm minimizes total execution time and cost while balancing task allocation across nodes.
