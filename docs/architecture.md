# Arquitetura da Solução

```mermaid
flowchart LR
    U[Aluno] --> UI[Interface Streamlit/Web]
    UI --> CA[Context Agent]
    CA --> GWA[Generative Word Agent]
    GWA --> SA[Safety & Trust Agent]
    SA --> LA[Linguistic Agent]
    LA --> PA[Pedagogical Agent]
    PA --> UI
    UI --> PR[Registro de Progresso]

    CA --> AI[Gemma/Ollama]
    GWA --> AI
```

## Camadas

- Interface
- Orquestração
- Agentes
- Gateway de IA
- Dados pedagógicos
- Segurança e progresso

## Estratégia técnica

No hackathon, a demo pode rodar com mock determinístico ou Ollama local. A arquitetura permite trocar o provedor de IA sem alterar os agentes.
