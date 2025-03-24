from crewai import Agent, Task, Crew
from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

def create_crew(customer: str, person: str, inquiry: str):
    # Agente que responde o cliente
    atendimento = Agent(
        role="Agente de Suporte",
        goal="Responder de forma clara, completa e simpática",
        backstory=f"Você atende clientes como {customer}. Seja direto e profissional.",
        tools=[search_tool],
        allow_delegation=False,
        verbose=True
    )

    # Agente que coleta dados e envia relatórios (placeholder, não envia ainda)
    dados = Agent(
        role="Analista de Dados de Suporte",
        goal="Analisar mensagens recebidas e gerar relatório de leads, dúvidas e NPS",
        backstory="Você organiza os dados dos atendimentos e prepara resumos diários.",
        verbose=True
    )

    # Agente que revisa tom e clareza
    revisor = Agent(
        role="Editor de Linguagem",
        goal="Revisar tom, ortografia e clareza do atendimento",
        backstory="Você garante que as mensagens tenham o tom certo da empresa.",
        verbose=True
    )

    # Tarefa principal de atendimento
    task = Task(
        description=f"{person} da empresa {customer} perguntou: {inquiry}. Responda da melhor forma possível.",
        expected_output="Uma resposta clara, completa e simpática.",
        agent=atendimento
    )

    crew = Crew(
        agents=[atendimento, revisor, dados],
        tasks=[task],
        verbose=True,
        memory=True
    )

    return crew
