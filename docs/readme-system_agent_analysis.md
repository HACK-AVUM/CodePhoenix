# System-Agent-Anlysis Microservice

## Descrizione

Il microservizio di Analisi utilizza un sistema multi-agente per analizzare il codice. Esistono due agenti principali che collaborano per eseguire un'analisi approfondita e valutare la complessità del codice:

1. **Code Analyzer**: Questo agente si occupa di analizzare il codice legacy, applicando la sua vasta esperienza per identificare problemi, suggerire miglioramenti e garantire la qualità del codice.
2. **Complex Analyzer**: Questo agente valuta la complessità del codice, fornendo metriche dettagliate che aiutano a comprendere meglio le aree più critiche e complesse del progetto.

## Architettura del Microservizio

Il microservizio è progettato per eseguire i task in maniera sequenziale. I task sono assegnati rispettivamente a Code Analyzer e Complex Analyzer, garantendo che l'analisi del codice venga effettuata in due fasi distinte ma complementari.

## Funzionamento

### Code Analyzer

1. **Input**: Riceve il codice legacy da analizzare.
2. **Analisi**: Applica tecniche di analisi statica per identificare problemi nel codice, come bug, vulnerabilità di sicurezza e violazioni delle best practice.
3. **Output**: Fornisce un report dettagliato con i problemi identificati e suggerimenti per miglioramenti.

### Complex Analyzer

1. **Input**: Riceve il codice da analizzare insieme al report prodotto dal Code Analyzer.
2. **Valutazione della Complessità**: Calcola varie metriche di complessità, come la complessità ciclomatica, la profondità dei blocchi nidificati e il numero di linee di codice.
3. **Output**: Fornisce un report con le metriche di complessità e suggerisce aree del codice che potrebbero beneficiare di un refactoring per ridurre la complessità.
