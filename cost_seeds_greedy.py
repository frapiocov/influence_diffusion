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


# funzione obiettivo f1
def objective_function(graph, S, u):
    S_with_u = S | {u} # seed set con u
    total_with_u = 0
    total = 0
    # calcolo valore con u
    for v in graph.nodes():
        # applicazione minimo su intersezione tra N ed S e grado/2
        min_neighbors_in_S_with_u = min(len(set(graph.neighbors(v)) & S_with_u), math.ceil(graph.degree(v) / 2))
        total_with_u += min_neighbors_in_S_with_u
    # calcolo valore senza u
    for v in graph.nodes():
        min_neighbors_in_S = min(len(set(graph.neighbors(v)) & S), math.ceil(graph.degree(v) / 2))
        total += min_neighbors_in_S
    # differenza di incremento
    return total_with_u - total


# algoritmo cost seeds greedy
def cost_seeds_greedy(graph, costs, budget):
    graph_set = set(graph.nodes())
    Sp = set()
    Sd = set()
    discard = set()
    used_budget = 0
    while True:
        try:
            u = max(graph_set - Sd, key=lambda v:  objective_function(graph, Sd, v) / costs[v])
            if objective_function(graph, Sd, u) <= 0:
                break
            if sum(costs[v] for v in Sd) + costs[u] <= budget:
                Sp = Sd
                Sd = Sp.union({u})
                budget_used += costs[u]
                print("Budget usato:", budget_used)
                if budget_used == budget:
                    break
                # print(Sd)
            else:
                # nodi scartati dal seed set
                discard.add(u)
                graph_set = graph_set - discard
        except:
            break
    return Sd # seed set risultante


# main function
def main():
    budget = 100
    print("Budget: " + str(budget))
    
    GRAPH, COSTS = create_graph(0)
    SEED_SET = cost_seeds_greedy(GRAPH, COSTS, budget)
    
    print("seed set selezionato: ", SEED_SET)


if __name__=="__main__":
    main()
