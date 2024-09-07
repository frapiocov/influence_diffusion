import snap
import copy
import math
import time
import random


# total cost of Seed set
def seed_set_cost(ss, cost):
    totalCost = 0
    for i in ss:
        totalCost += cost[i]

    return totalCost


# genera un costo casuale da 1 a 30
def rand_cost_func():
    p = random.randint(1, 30)
    return p


# costo  è la metà del grado del nodo
def half_deg_cost_func(deg):
    if deg != 0:
        return deg / 2
    else:
        return 1
