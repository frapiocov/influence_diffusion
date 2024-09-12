'''
Algoritmo My Seeds: viene calcolata la betweenneess centrality per ogni nodo
nella rete, vengono selezionati i nodi con valore più alto finché il
budget lo permette

Funzione costi
1. random
2. metà grafo
3. pagerank

'''
import snap
import math
import networkx as nx
import random

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

    return nx_graph, COSTS


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

# main function
def main():
    budget = 100
    print("Budget: " + str(budget))
    
    GRAPH, COSTS = create_graph(0)
    SEED_SET = my_seeds(GRAPH, COSTS, budget)
    
    print("seed set selezionato: ", SEED_SET)


if __name__=="__main__":
    main()
