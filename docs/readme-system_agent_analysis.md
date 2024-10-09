# System-Agent-Anlysis Microservice 🔍

## Descrizione

Il microservizio di Analisi utilizza un sistema multi-agente per analizzare il codice. Esistono due agenti principali che collaborano per eseguire un'analisi approfondita e valutare la complessità del codice.

## Architettura del Microservizio

Il microservizio è progettato per eseguire i task in maniera sequenziale. I task sono assegnati rispettivamente a Code Analyzer e Complex Analyzer, garantendo che l'analisi del codice venga effettuata in due fasi distinte ma complementari.


![Analysis Microservice](./doc-images-analysis//micro-analysis.png)

### Code Analyzer

Questo agente si occupa di analizzare il codice legacy, applicando la sua vasta esperienza per identificare problemi, suggerire miglioramenti e garantire la qualità del codice.

1. **Input**: Riceve il codice legacy da analizzare.
2. **Analisi**: Applica tecniche di analisi statica per identificare problemi nel codice, come bug, vulnerabilità di sicurezza e violazioni delle best practice.
3. **Output**: Fornisce un report dettagliato con i problemi identificati e suggerimenti per miglioramenti.

```python
code_analyst = Agent(
        role='Legacy Code Analyst',
        goal='Analyze and understand legacy code structure and functionality',
        backstory="""You are an experienced developer with decades of experience in analyzing legacy systems.
        Your expertise lies in dissecting complex programs and understanding their core logic.""",
        verbose=True,
        allow_delegation=False,
        llm=os.environ["LLM"],
    )
```

#### WorkFlow - Code Analyzer

![WorkFlow - Code Analyzer](./doc-images-analysis/analyzer-workflow.png)


### Complex Analyzer

Questo agente valuta la complessità del codice, fornendo metriche dettagliate che aiutano a comprendere meglio le aree più critiche e complesse del progetto.

1. **Input**: Riceve il codice da analizzare insieme al report prodotto dal Code Analyzer.
2. **Valutazione della Complessità**: Calcola varie metriche di complessità, come la complessità ciclomatica, la profondità dei blocchi nidificati e il numero di linee di codice.
3. **Output**: Fornisce un report con le metriche di complessità e suggerisce aree del codice che potrebbero beneficiare di un refactoring per ridurre la complessità.

```python
    complexity_assessor = Agent(
        role='Code Complexity Assessor',
        goal='Evaluate the overall complexity of the legacy codebase',
        backstory="""You are an expert in software metrics and complexity analysis.
        You specialize in assessing code complexity across different languages and providing actionable insights.""",
        verbose=True,
        allow_delegation=False,
        llm=os.environ["LLM"],
    )
```



#### WorkFlow - Code Analyzer

![WorkFlow - Evaluation Analyzer](./doc-images-analysis/evaluation-workflow.png)


### Parametri - Code Analyzer & Complex Analyzer

- **role** : Descrive il ruolo che l'agente deve avere all'interno
- **goal** : Descrive l'obiettivo che l'agente deve raggiungere all'interno del microservizio
- **backstory** : Riguarda l'aspetto del **prompt engineering** utilizzato per poter dare attributi in più agli agenti
- **allow_delegation** : permette agli altri agenti che fanno parte di una **Crew** di poter scambiare gli output tra di loro.
- **LLM**: rappresenta il core del tipo di Large Language Model che abbiamo utilizzato 