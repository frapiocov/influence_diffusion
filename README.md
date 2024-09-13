## 🌐 Cost Majority Cascade - Progetto Reti Sociali

Il problema preso in esame è la valutazione di un processo di Influence Diffusion su una rete sociale pesata. Una rete sociale è una struttura composta da individui/entità e le relative relazioni. Lo studio di una rete sociale permette di ottenere informazioni su dinamiche sociali, interazioni tra individui, diffusione di idee, di prodotti o di un’epidemia. Graficamente, le reti sociali, vengono rappresentate come grafi composti da nodi ed archi.

Scelto un grafo G=(V,E), un intero k come soglia, una funzione costi c: V->N, partito il processo di diffuzione vengono determinate le seguenti: 
- il seed set massimale S con costo c(S) <= k
- l’insieme dei nodi attivati Inf[S]
- i grafici mostranti i risultati ottenuti 
    - per ogni fissata funzione costi c: V->N
    - al variare del budget k del seed set S, i valori di |Inf[S]| per diversi algoritmi di selezione.

Vengono utilizzate tre funzioni costo:
- 1 - valore random scelto in un fissato range
- 2 - grado del nodo / 2
- 3 - valore di closeness centrality