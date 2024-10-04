##code_refactor.py: 
#Contiene l'agente principale che utilizza un tool di refactoring per suggerire e applicare modifiche al codice.
from crewai import Agent
from tools.refactor_tool import RefactorTool


##Agente di refactoring: 
# Questo agente utilizza il RefactorTool per analizzare il codice sorgente e suggerire refactoring 
# (ad esempio, rimozione di duplicati, ottimizzazione della complessità ciclomatica).
class CodeRefactorAgent(Agent):
    def __init__(self):
        refactor_tool = RefactorTool()
        super().__init__(
            role='Code Refactor',
            goal='Analyze and refactor the provided source code to improve its structure and maintainability.',
            tools=[refactor_tool],
            verbose=True,
            allow_delegation=True
        )

    ##Metodi suggest_refactor e apply_refactor: 
    # Questi metodi consentono di suggerire refactoring (ad esempio, "questo metodo è troppo lungo") 
    # e applicare direttamente le modifiche (ad esempio, riorganizzare il codice).
    def suggest_refactor(self, code_data):
        return self.tools[0].suggest_refactor(code_data)

    def apply_refactor(self, code_data):
        return self.tools[0].apply_refactor(code_data)
