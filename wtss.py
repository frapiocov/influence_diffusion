'''
Algoritmo Weighted Target Set Selection

'''
import snap
import math
import networkx as nx
import random
from collections import Counter

def wtss(GRAPH, COSTS, TRESHOLDS, budget):
    # copia del grafo su cui effettuare il processo
    graph_copy = GRAPH;
    seed_set = []
    seed_set_cost = 0

    while len(graph_copy.nodes()) > 0:

        first_case_flag = False
        second_case_flag = False

        # PRIMO CASO 
        for v in graph_copy.nodes():
            if TRESHOLDS[v] == 0:
                first_case_flag = True
                to_delete = v
                # vicinato del nodo v
                neighbors = list(graph_copy.neighbors(v))
                # aggiornamento soglia vicini di v
                for u in neighbors:
                    TRESHOLDS[u] = max(0,(TRESHOLDS[u] - 1))
                # rimuoviamo v dal grafo
                graph_copy.remove_node(to_delete)
                break

        if first_case_flag:
            continue

        # SECONDO CASO
        for v in G_copy.nodes():
            if graph_copy.degree(v) < TRESHOLDS[v]:
                second_case_flag = True
                # v viene aggiunto al seed set
                seed_set.append(v)
                # aggiornato il budget usato
                seed_set_cost += COSTS[v]
                
                to_delete = v
                neighbors = list(graph_copy.neighbors(v))
                # aggiornamento soglie vicini di v
                for u in neighbors:
                    TRESHOLDS[u] = TRESHOLDS[u] - 1

                graph_copy.remove_node(to_delete)
                break
        
        if second_case_flag: 
            continue

        selected_nodes = Counter()
        # TERZO CASO
        for v in graph_copy.nodes():
            # caratteristiche del nodo v in esame
            cost = COSTS[v]
            threshold = TRESHOLDS[v]
            degree = graph_copy.degree(v)

            selected_nodes[v] = ((cost * threshold) / (degree * (degree + 1)))
        #scelta del nodo da rimuovere
        to_delete = max(selected_nodes, key=selected_nodes.get)
        graph_copy.remove_node(to_delete)
        
        if seed_set_cost >= budget:
            return seed_set[:-1]

    return seed_set