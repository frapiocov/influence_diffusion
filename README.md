## 🌐 Cost Majority Cascade - Progetto Reti Sociali

### Introduzione
Il problema preso in esame è la valutazione di un processo di Influence Diffusion su una rete sociale pesata. Una rete sociale è una struttura composta da individui/entità e le relative relazioni. Lo studio di una rete sociale permette di ottenere informazioni su dinamiche sociali, interazioni tra individui, diffusione di idee, di prodotti o di un’epidemia. Graficamente, le reti sociali, vengono rappresentate come grafi composti da nodi ed archi.

### Il problema
Scelto un grafo G=(V,E), un intero k come soglia, una funzione costi c: V->N, partito il processo di diffuzione vengono determinate le seguenti: 
- il seed set massimale S con costo c(S) <= k
- l’insieme dei nodi attivati Inf[S]
- i grafici mostranti i risultati ottenuti 
    - per ogni fissata funzione costi c: V->N
    - al variare del budget k del seed set S, i valori di |Inf[S]| per diversi algoritmi di selezione.

Vengono utilizzate tre funzioni costo:
- c(u) = valore random scelto in un fissato range
- c(u) = |d(u)/2|
- c(u) = ?

### Dataset utilizzato
La GitHub Social Network, scaricabile [qui](https://snap.stanford.edu/data/github-social.html), è una rete sociale i cui nodi sono gli sviluppatori presenti su GitHub, è stata creata con le API pubbliche nel giugno 2019. I nodi sono gli sviluppatori che hanno salvato (star) almeno 10 repository e gli edge rappresentano la relazione reciproca di following tra di loro.

Caratteristiche del grafo:
- Directed: No.
- Node features: Si.
- Edge features: No.
- Node labels: Si. Binary-labeled.
- Temporal: No.
- Nodes: 37,700
- Edges: 289,003
- Density: 0.001 
- Transitvity: 0.013