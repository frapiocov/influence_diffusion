'''
Algoritmo Weighted Target Set Selection

Funzione costi
1. random
2. metà grafo
3. pagerank

'''
import snap
import math
import networkx as nx
import random
from collections import Counter


# crea il grafo dalla rete sociale
def create_graph(cost_func):
    # parametri: tipo di grafo da generare, file rete, colonna source vertex
    # colonna destination vertex, separatore
    net_graph = snap.LoadEdgeList(snap.TUNGraph, "data/musae_git_edges.csv", 0, 1, ",")
    # creazione grafo vuoto con networkx 
    nx_graph = nx.Graph()

    # print(net_graph.GetEdges())
    # print(net_graph.GetNodes())
    # riempimento grafo
    for edge in net_graph.Edges():
        nx_graph.add_edge(edge.GetSrcNId(), edge.GetDstNId())

    # assegnazione costi in base alla funzione scelta
    COSTS = {}

    if cost_func == 0: # random
        random.seed(14)
        COSTS = {node: random.randint(1, 10) for node in nx_graph.nodes()}
    elif cost_func == 1: # degree\2
        COSTS = {node: nx_graph.degree(node)/2 for node in nx_graph.nodes()}
    elif cost_func == 2: # pagerank 
        break

    # assegnazione soglie
    TRESHOLDS = {node: nx_graph.degree(node)/2 for node in nx_graph.nodes()}
    
    return nx_graph, COSTS, TRESHOLDS


def wtss(GRAPH, COSTS, TRESHOLDS, budget):
    # copia del grafo su cui effettuare il processo
    graph_copy = GRAPH;
    seed_set = set()
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
                seed_set.add(v)
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
        to_delete = max(selected_nodes, key=selected_nodes.get)
        graph_copy.remove_node(to_delete)
        
        if seed_set_cost >= budget:
            return seed_set

    return seed_set


# main function
def main():
    budget = 100
    print("Budget: " + str(budget))
    
    GRAPH, COSTS, TRESHOLDS = create_graph(0)
    SEED_SET = wtss(GRAPH, COSTS, TRESHOLDS, budget)
    
    print("seed set selezionato: ", SEED_SET)


if __name__=="__main__":
    main()
