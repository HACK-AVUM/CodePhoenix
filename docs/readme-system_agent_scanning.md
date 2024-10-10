# Vulnerability Scanning Microservice 🔎

## Descrizione

Il microservizio di scansione delle vulnerabilità analizza il codice sorgente per identificare potenziali rischi di sicurezza. Utilizza agenti specializzati per eseguire scansioni approfondite e integrare i risultati in SonarQube per un monitoraggio e una gestione efficaci delle vulnerabilità.

## Architettura del Microservizio

Il microservizio è progettato per eseguire la scansione delle vulnerabilità in modo sequenziale. Gli agenti principali sono responsabili della scansione del codice e dell'integrazione dei risultati con SonarQube.

![Vulnerability Scanning Microservice](./doc-images-vulnerability/micro-vulnerability.png)

### Vulnerability Scanner

Questo agente si occupa di analizzare il codice sorgente per identificare vulnerabilità comuni e rischi di sicurezza.

1. **Input**: Riceve il codice sorgente da analizzare.
2. **Scanning**: Esegue la scansione del codice per identificare vulnerabilità comuni come SQL injection, XSS, CSRF e altre vulnerabilità della OWASP Top 10.
3. **Output**: Fornisce un report dettagliato delle vulnerabilità identificate.

```python
vulnerability_scanner = Agent(
    role='Vulnerability Scanner',
    goal='Scan code for potential security vulnerabilities',
    backstory="""You are an experienced security expert with a deep understanding of code vulnerabilities.
    Your expertise lies in identifying potential security risks in various programming languages.""",
    verbose=True,
    allow_delegation=False,
    llm=os.environ["LLM"],
)
```

#### WorkFlow - Vulnerability Scanner

![WorkFlow - Vulnerability Scanner](./doc-images-vulnerability/scanner-workflow.png)

### Parametri - Vulnerability Scanner

- **role**: Descrive il ruolo che l'agente deve avere all'interno del microservizio.
  - Esempio: 'Vulnerability Scanner'
- **goal**: Descrive l'obiettivo che l'agente deve raggiungere all'interno del microservizio.
  - Esempio: 'Scan code for potential security vulnerabilities'
- **backstory**: Riguarda l'aspetto del **prompt engineering** utilizzato per dare attributi in più agli agenti.
  - Esempio: "You are an experienced security expert with a deep understanding of code vulnerabilities. Your expertise lies in identifying potential security risks in various programming languages."
- **verbose**: Indica se l'agente deve fornire output dettagliati durante la sua esecuzione.
  - Esempio: `True`
- **allow_delegation**: Permette agli altri agenti che fanno parte di una **Crew** di scambiare gli output tra di loro.
  - Esempio: `False`
- **llm**: Rappresenta il core del tipo di Large Language Model utilizzato.
  - Esempio: `os.environ["LLM"]`

### SonarQube Integrator

Questo agente è responsabile dell'integrazione dei risultati della scansione delle vulnerabilità con SonarQube, mappando le vulnerabilità identificate nel sistema di tracciamento delle problematiche di SonarQube.

```python
sonarqube_integrator = Agent(
    role='SonarQube Integrator',
    goal='Integrate vulnerability scan results with SonarQube',
    backstory="""You are an expert in integrating security tools with SonarQube.
    You specialize in interpreting scan results and mapping them to SonarQube's issue tracking system.""",
    verbose=True,
    allow_delegation=False,
    llm=os.environ["LLM"],
)
```

#### WorkFlow - SonarQube Integrator

![WorkFlow - SonarQube Integrator](./doc-images-vulnerability/integrator-workflow.png)

### Parametri - SonarQube Integrator

- **role**: Descrive il ruolo che l'agente deve avere all'interno del microservizio.
  - Esempio: 'SonarQube Integrator'
- **goal**: Descrive l'obiettivo che l'agente deve raggiungere all'interno del microservizio.
  - Esempio: 'Integrate vulnerability scan results with SonarQube'
- **backstory**: Riguarda l'aspetto del **prompt engineering** utilizzato per dare attributi in più agli agenti.
  - Esempio: "You are an expert in integrating security tools with SonarQube. You specialize in interpreting scan results and mapping them to SonarQube's issue tracking system."
- **verbose**: Indica se l'agente deve fornire output dettagliati durante la sua esecuzione.
  - Esempio: `True`
- **allow_delegation**: Permette agli altri agenti che fanno parte di una **Crew** di scambiare gli output tra di loro.
  - Esempio: `False`
- **llm**: Rappresenta il core del tipo di Large Language Model utilizzato.
  - Esempio: `os.environ["LLM"]`

### Task - Vulnerability Scanner

```python
task1 = Task(
    description=f"""Scan the given code for potential security vulnerabilities.
    Identify common issues such as SQL injection, XSS, CSRF, and other OWASP Top 10 vulnerabilities.
    Code: {code}""",
    expected_output="Detailed report on identified vulnerabilities",
    agent=vulnerability_scanner,
)
```

#### Parametri - Task

- **description**: Descrive il compito che deve essere eseguito.
  - Esempio: "Scan the given code for potential security vulnerabilities. Identify common issues such as SQL injection, XSS, CSRF, and other OWASP Top 10 vulnerabilities. Code: {code}"
- **expected_output**: Descrive l'output atteso dopo l'esecuzione del task.
  - Esempio: "Detailed report on identified vulnerabilities"
- **agent**: L'agente responsabile dell'esecuzione del task.
  - Esempio: `vulnerability_scanner`

### Task - SonarQube Integrator

```python
task2 = Task(
    description="""Using the vulnerability scan results, integrate the findings with SonarQube.
    Map identified issues to SonarQube's rule set and prepare data for API submission.""",
    expected_output="SonarQube-compatible vulnerability report",
    agent=sonarqube_integrator
)
```

#### Parametri - Task

- **description**: Descrive il compito che deve essere eseguito.
  - Esempio: "Using the vulnerability scan results, integrate the findings with SonarQube. Map identified issues to SonarQube's rule set and prepare data for API submission."
- **expected_output**: Descrive l'output atteso dopo l'esecuzione del task.
  - Esempio: "SonarQube-compatible vulnerability report"
- **agent**: L'agente responsabile dell'esecuzione del task.
  - Esempio: `sonarqube_integrator`

### Crew - Vulnerability Scanning

La **crew** è composta dagli agenti responsabili delle scansioni delle vulnerabilità e dell'integrazione dei risultati.

```python
# Instantiate the crew for vulnerability scanning
scanning_crew = Crew(
    agents=[vulnerability_scanner,
            # sonarqube_integrator
            ],
    tasks=[task1,
           # task2
           ],
    verbose=True,
    process=Process.sequential
)
```

#### Parametri - Crew

- **agents**: L'insieme di agenti che vengono creati per eseguire il compito.
  - Esempio: `[vulnerability_scanner, sonarqube_integrator]`
- **tasks**: L'insieme dei vari task assegnati ai vari agenti.
  - Esempio: `[task1, task2]`
- **process**: Indica se il tipo di processo può essere sequenziale oppure no.
  - Esempio: `Process.sequential`
