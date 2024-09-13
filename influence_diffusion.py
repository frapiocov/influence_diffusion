'''
Simula la cascade sull'intera rete partendo dal seed set individuato

Funzione costi
1. random
2. metà grafo
3. pagerank

Budget
50, 100, 150, 200

'''
import snap
import math
import networkx as nx
import random

from my_seeds import my_seeds
from cost_seeds_greedy import cost_seeds_greedy
from wtss import wtss

# crea il grafo dalla rete sociale
def create_graph(cost_func, is_wtss):
    # parametri: tipo di grafo da generare, file rete, colonna source vertex
    # colonna destination vertex, separatore
    net_graph = snap.LoadEdgeList(snap.TUNGraph, "data/github_social_network.csv", 0, 1, ",")
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
        COSTS = {}

    TRESHOLDS = {}    
    if is_wtss:
        # assegnazione soglie
        TRESHOLDS = {node: nx_graph.degree(node)/2 for node in nx_graph.nodes()}
 
    return nx_graph, COSTS, TRESHOLDS


def influence_diffusion(GRAPH, SEED_SET):
    INFLUENCED = set(SEED_SET)
    prev_influenced = set(SEED_SET)
    # Numero totale di nodi influenzati
    total_influenced = len(SEED_SET)

    current_iteration = 0

    while True:
        current_influenced = set()
        # cicla sui nodi del grafo
        for v in GRAPH.nodes():
            # controlla se il nodo non è già stato influenzato
            if v not in prev_influenced:
                # vicini di v
                neighbors = set(GRAPH.neighbors(v))
                # vicini di v influenzati nel turno precedente
                count_influenced_neighbors = len(neighbors.intersection(prev_influenced))
                # se la soglia di influenza è superata avviene il contagio
                if count_influenced_neighbors >= len(neighbors) / 2:
                    current_influenced.add(v)

        # processo finito se non ci sono nuovi contagiati
        if not current_influenced:
            break

        # Aggiorna inf_s con l'insieme di nodi influenzati al passo corrente
        INFLUENCED = INFLUENCED.union(current_influenced)
        prev_influenced = prev_influenced.union(current_influenced)
        # Aggiorna il numero totale di nodi influenzati
        total_influenced += len(current_influenced)  
        current_iteration += 1  # Incrementa il contatore di iterazioni

    return INFLUENCED, total_influenced



# main function
def main():
    budget = 50
    print("Budget: " + str(budget))
    
    GRAPH, COSTS, TRESHOLDS = create_graph(0, TRUE)
    SEED_SET = wtss(GRAPH, COSTS,TRESHOLDS, budget)

    # print("Seed set: ")
    # print(SEED_SET)
    print("Dimensione seed set: " + str(len(SEED_SET)))

    # INFS nodi influenzati
    INFS, INFLUENCED = influence_diffusion(GRAPH, SEED_SET)
    print("Totale nodi influenzati: " + str(INFLUENCED))


if __name__=="__main__":
    main()