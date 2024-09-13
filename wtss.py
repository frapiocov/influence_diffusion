'''
Algoritmo Weighted Target Set Selection

'''
import snap
import math
import networkx as nx
import random
from collections import Counter

def wtss(GRAPH, COSTS, TRESHOLDS, budget):
    graph_copy = GRAPH.copy();
    seed_set = []
    used_budget = 0
    iter = 0

    while len(graph_copy.nodes()) > 0:
        
        if iter != 0:
            GRAPH = graph_copy.copy()
        
        for v in GRAPH.nodes():
            # primo caso
            if TRESHOLDS[v] == 0:
                to_delete = v
                # vicinato del nodo v
                neighbors = list(graph_copy.neighbors(v))
                # aggiornamento soglia vicini di v
                for u in neighbors:
                    TRESHOLDS[u] = max(0,(TRESHOLDS[u] - 1))
                # rimuoviamo v dal grafo
                graph_copy.remove_node(to_delete)
            # secondo caso
            elif graph_copy.degree(v) < TRESHOLDS[v]:
                # v viene aggiunto al seed set
                seed_set.append(v)
                # aggiornato il budget usato
                used_budget += COSTS[v]
                #print("budget " + str(used_budget))
                to_delete = v
                neighbors = list(graph_copy.neighbors(v))
                # aggiornamento soglie vicini di v
                for u in neighbors:
                    TRESHOLDS[u] = TRESHOLDS[u] - 1
                graph_copy.remove_node(to_delete)
            else: # terzo caso
                selected_nodes = Counter()
                # caratteristiche del nodo v in esame
                cost = COSTS[v]
                threshold = TRESHOLDS[v]
                degree = graph_copy.degree(v)
            
                if degree == 0: # evita la divisione per zero
                    degree = 1
                selected_nodes[v] = ((cost * threshold) / (degree * (degree + 1)))
                #scelta del nodo da rimuovere
                to_delete = max(selected_nodes, key=selected_nodes.get)
                graph_copy.remove_node(to_delete)
        
            if used_budget >= budget:
                return seed_set[:-1]
        
        # graph copy va aggiornato dopo la prima iterazione
        iter = 1    
    return seed_set