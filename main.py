import os

from google import genai
from google.genai import types


DEFAULT_MODEL = "gemini-2.5-flash-lite"
DEFAULT_MAX_OUTPUT_TOKENS = 700


class FreireIA:
    def __init__(self, api_key, model_name=None):
        """O custo e delegado ao usuario via sua propria API Key."""
        self.model_name = model_name or os.getenv("GEMINI_MODEL") or DEFAULT_MODEL
        self.max_output_tokens = int(
            os.getenv("GEMINI_MAX_OUTPUT_TOKENS", DEFAULT_MAX_OUTPUT_TOKENS)
        )
        self.client = genai.Client(api_key=api_key)

    def _generate(self, prompt):
        return self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                max_output_tokens=self.max_output_tokens,
                temperature=0.7,
            ),
        )

    def iniciar_investigacao(self, idioma="pt"):
        prompt = f"""
        Voce e a FreireIA, uma co-mediadora entre educador e aluno.
        Crie um roteiro curto no idioma '{idioma}' para abrir uma sessao de escuta.
        Nao use nomes ficticios, colchetes, placeholders ou campos como [Nome].
        Escreva como orientacao para o educador, nao como fala direta da IA.

        Responda em secoes curtas:
        1. Convite inicial: uma frase simples que o educador pode adaptar
        2. Perguntas para escutar: cinco perguntas curtas
        3. O que observar: palavras que aparecem com emocao, repeticao ou gesto
        """
        return self._generate(prompt)

    def mediar_dialogo(
        self,
        contexto_educador,
        fala_aluno,
        sinais_observados=None,
        cartoes_escolhidos=None,
        idioma="pt",
    ):
        sinais = ", ".join(sinais_observados or [])
        cartoes = ", ".join(cartoes_escolhidos or [])
        prompt = f"""
        Voce e a FreireIA, uma solucao que atua como interlocutora e facilitadora
        entre educador e aluno. O educador permanece no controle pedagogico.

        Idioma da resposta: {idioma}

        Contexto informado pelo educador:
        {contexto_educador}

        Fala, escrita ou resposta do aluno:
        {fala_aluno}

        Sinais observados pelo educador:
        {sinais}

        Cartoes visuais ou escolhas por toque feitas pelo aluno:
        {cartoes}

        Gere uma resposta curta e estruturada:
        1. Sintese da escuta
        2. Possiveis palavras geradoras, com 1 linha de justificativa cada
        3. Proxima pergunta que o educador pode fazer
        4. Cuidados de acolhimento

        Evite respostas longas. Nao use placeholders.
        """
        return self._generate(prompt)

    def alfabetizar(self, palavra, contexto="", idioma="pt"):
        prompt = f"""
        Voce e a FreireIA, apoiando uma sessao de alfabetizacao critica.

        Palavra geradora: {palavra}
        Contexto do aluno: {contexto}
        Idioma da resposta: {idioma}

        Crie uma sequencia curta e pratica:
        1. Sentido social da palavra
        2. Duas perguntas para circulo de cultura
        3. Separacao silabica ou fonetica
        4. Uma atividade de leitura/escrita
        5. Uma frase critica modelo

        Mantenha linguagem simples e adequada para o educador aplicar com o aluno.
        """
        return self._generate(prompt)


# Exemplo de uso:
# app = FreireIA(api_key="USER_PROVIDED_KEY")
