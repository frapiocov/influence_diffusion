
## 🌐 Progetto Reti Sociali
--------
Scelto un grafo G=(V,E), un intero k, una funzione costi c: V->N
- Determinare il seed set massimale S con c(S) <= k.
- Si fa girare il processo di attivazione e si determina l’insieme dei nodi attivati Inf[S].
- Rappresentare con grafici i risultati ottenuti 
    - per ogni fissata funzione costi c: V->N
    - al variare del costo budget k del seed set S devono essere rappresentati i valori di |Inf[S]| per diversi algoritmi di selezione del seed set S.

Le funzione costi da utilizzare devono essere tre per ogni:
- c(u) = valore random scelto in un fissato range
- c(u) = |d(u)/2|
- una funzione costi che si ritiene adatta

