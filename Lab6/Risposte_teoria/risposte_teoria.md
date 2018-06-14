### Domanda 3
#### - Complessità:
Consideriamo solo un piccola frazione dei punti n totali nel dataset ed assumiamo che l'algoritmo **HierarchicalClustering**
utilizzi solo **FastClosestPair**.
Quest'ultimo ha complessità **O(n log(n))** perciò l'algoritmo del clustering gerarchico avrà una complessità totale **O((n-k)(n log(n)))** dovendo produrre k cluster.
L'algoritmo di clustering **K-Means** invece, dovendo creare k cluster con al massimo q interazioni, ha una complessità dell'ordine **O(q n k)** .

#### - Tempi asintotici d'esecuzione:
Dal punto di vista dei tempi asintotici, assumendo che **K-Means** utilizzi sempre un numero piccolo di interazioni q, si può approssimare il tempo asintotico ad un'**esecuzione lineare** sul numero dei punti n. Per quanto riguarda l'algoritmo 
**HierarchicalClustering** invece, con k cluster, il numero di iterazioni che esso deve eseguire è _(n-k)_, ma si può approssimare ad n, con la precondizione di un k molto piccolo.
Di conseguenza il tempo asintotico totale di clustering gerarchico diventa **O(n^2(log(n)))** .

È facile concludere che il metodo di clustering più veloce, quando il numero dei cluster in output è molto piccolo, è sicuramente **K-Means**. 


