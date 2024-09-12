'''
Algoritmo My Seeds: viene calcolata la betweenneess centrality per ogni nodo
nella rete, vengono selezionati i nodi con valore più alto finché il
budget lo permette

'''
import snap
import math
import networkx as nx
import random

# algoritmo my seeds
def my_seeds(graph, costs, budget):
    graph_set = set(graph.nodes())
    seed_set = set()
    used_budget = 0
    # calcolo valori betweenness
    betweenness = nx.betweenness_centrality(graph)
    # ordinamento dei nodi 
    ordered_nodes = sorted(betweenness, key=betweenness.get, reverse=True)
    # seleziono i nodi con valore più alto fino a esaurimento budget
    for v in ordered_nodes:
        # controllo budget
        if used_budget + costs[v] > budget:
            break
        # aggiunto al seed set
        seed_set.add(v)
        used_budget += costs[v]
        print("Budget utilizzato:", used_budget)
    # seed set risultante
    return seed_set