'''
Algoritmo Cost Seed Greedy: ad ogni iterazione include nel seed set
il nodo con il miglior rapporto tra incremento di influenza e costo,
continua fino ad esaurimento budget.

Funzione costi
1. random
2. metà grafo
3. pagerank

'''
import snap
import math
import networkx as nx
import random

# crea il grafo della rete sociale
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
        COSTS = {node: Graph_nx.degree(node)/2 for node in Graph_nx.nodes()}
    elif cost_func == 2: # pagerank 
        "You're too young to party"

    return nx_graph, COSTS


# algoritmo cost seeds greedy
def cost_seeds_greedy(graph, costs, budget):
    graph_set = set(graph.nodes())
    Sp = set()
    Sd = set()
    print(sorted(setGrafo, key=lambda v: delta_v_fi(graph, Sd, v) / costs[v]))
    used_budget = 0
    while True:
        try:
            delta_value = delta_v_fi(graph, Sd, u)
            u = max(graph_set - Sd, key=lambda v: delta_value / costs[v])
            if delta_value <= 0:
                break
            if sum(costs[v] for v in Sd) + costs[u] <= budget:
                Sp = Sd
                Sd = Sp.union({u})
                budget_used += costs[u]
                print("Budget utilizzato:", budget_used)
                if budget_used == budget:
                    break
                print(Sd)
            else:
                # nodi scartati
                discard = set()
                discard.add(u)
                graph_set = graph_set - discard
        except:
            break
    return Sd # seed set iniziale risultante


# main function
def main():
    budget = 100
    GRAPH, COSTS = create_graph(0)
    SEED_SET = cost_seeds_greedy(GRAPH, COSTS, budget)
    print(SEED_SET)


if __name__=="__main__":
    main()
