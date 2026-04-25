# FreireAI Literacy Companion

Aplicativo de alfabetização multilíngue inspirado no método de Paulo Freire, usando Gemma 4 e arquitetura multiagente para transformar a realidade do aluno em uma trilha personalizada de leitura, fala, sílabas e descoberta.

## Proposta para o Gemma 4 Good Hackathon

**Tese:** a alfabetização começa quando a IA aprende primeiro o mundo do aluno.

O aplicativo conversa com o estudante, identifica palavras significativas do seu contexto — família, trabalho, casa, transporte, jogo, comunidade — e transforma essas palavras em atividades de alfabetização no idioma desejado.

## Trilhas-alvo

- Main Track
- Future of Education
- Digital Equity & Inclusivity
- Safety & Trust
- Possível trilha técnica: Ollama, LiteRT ou llama.cpp

## Funcionalidades do MVP

- Identificação do idioma desejado
- Conversa inicial baseada no contexto do aluno
- Seleção de palavra geradora
- Quebra silábica
- Família silábica
- Formação de novas palavras
- Áudio e microinterações
- Registro simples de progresso
- Explicação pedagógica da escolha da palavra

## Arquitetura multiagente

1. **Context Agent**: entende o contexto de vida do aluno.
2. **Generative Word Agent**: escolhe a palavra geradora.
3. **Linguistic Agent**: gera sílabas, famílias silábicas e exemplos.
4. **Pedagogical Agent**: adapta a dificuldade.
5. **Multimodal Agent**: organiza texto, imagem e voz.
6. **Safety & Trust Agent**: valida segurança, explicabilidade e adequação.

## Instalação local

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt
```

## Execução

```bash
streamlit run streamlit_app.py
```

## Uso com Ollama

Instale o Ollama e baixe um modelo compatível com Gemma:

```bash
ollama pull gemma3:4b
```

Depois configure o arquivo `.env` com base no `.env.example`.

## Estrutura

```text
freireai-literacy-companion/
├── app/
│   ├── agents/
│   ├── services/
│   ├── ui/
│   └── data/
├── docs/
├── specs/
├── tests/
├── assets/
├── streamlit_app.py
├── requirements.txt
└── README.md
```

## Entregáveis do hackathon

- Demo funcional
- Repositório público
- Vídeo de até 3 minutos
- Writeup Kaggle de até 1.500 palavras
- Galeria de mídia
