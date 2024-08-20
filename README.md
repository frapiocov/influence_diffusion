## 🌐 Cost Majority Cascade - Progetto Reti Sociali

### Introduzione
Il progetto tratta un processo di diffusione in una rete pesata combinando tre algoritmi di spreading, molteplici funzioni di costo e threshold differenti.

**Il problema**

Scelto un grafo G=(V,E), un intero k come soglia, una funzione costi c: V->N, partito il processo di diffuzione vengono determinate le seguenti: 
- il seed set massimale S con costo c(S) <= k
- l’insieme dei nodi attivati Inf[S]
- i grafici mostranti i risultati ottenuti 
    - per ogni fissata funzione costi c: V->N
    - al variare del budget k del seed set S, i valori di |Inf[S]| per diversi algoritmi di selezione.

Vengono utilizzate tre funzioni costo:
- c(u) = valore random scelto in un fissato range
- c(u) = |d(u)/2|
- una funzione costi che si ritiene adatta (?)

### Dataset utilizzato

### Installazione


### Esecuzione
