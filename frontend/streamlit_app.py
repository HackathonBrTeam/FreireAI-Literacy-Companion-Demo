import os
import sys
from datetime import datetime
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from main import FreireIA


LANGUAGES = {
    "Portugues (Brasil)": "pt",
    "Espanol": "es",
    "English": "en",
}

OBSERVATIONS = [
    "Falou com seguranca",
    "Ficou em silencio",
    "Apontou para imagens",
    "Pareceu cansado",
    "Pareceu animado",
    "Pediu ajuda para ler",
    "Misturou idiomas",
]

LIFE_CARDS = [
    "Casa",
    "Trabalho",
    "Familia",
    "Onibus",
    "Agua",
    "Escola",
    "Comida",
    "Saude",
    "Bairro",
]

FREIREIA_ROLE = (
    "A FreireIA nao substitui o educador. Ela ajuda a escutar o aluno, organizar "
    "o que apareceu na conversa e sugerir uma palavra para criar uma atividade de alfabetizacao."
)

DEFAULT_LISTENING_GUIDE = """
**Convite inicial**

Comece com uma conversa tranquila. Diga ao aluno que ele pode falar, apontar, desenhar ou escolher imagens. O importante e entender o que faz parte da vida dele.

**Perguntas para escutar**

- Como foi seu dia hoje?
- Que palavras aparecem muito na sua rotina?
- O que voce gostaria de conseguir ler melhor?
- Que lugar, pessoa ou trabalho e importante para voce?
- Tem alguma palavra que voce ve sempre e gostaria de entender ou escrever?

**O que observar**

Preste atencao em palavras repetidas, temas que aparecem com emocao, gestos, imagens escolhidas e situacoes ligadas a trabalho, casa, familia, transporte, saude ou comunidade.
"""


load_dotenv(ROOT_DIR / ".env")


def extract_text(response):
    if hasattr(response, "text"):
        return response.text
    return str(response)


def show_generation_error(exc):
    error_message = str(exc)
    if "API_KEY_INVALID" in error_message:
        st.error("A chave da API foi rejeitada. Atualize o arquivo .env e reinicie a demo.")
        return

    if "RESOURCE_EXHAUSTED" in error_message or "quota" in error_message.lower():
        st.error("A chave esta valida, mas a cota do projeto acabou ou ainda nao foi liberada.")
        return

    if "not found" in error_message.lower() and "model" in error_message.lower():
        st.error("O modelo configurado nao esta disponivel. Verifique GEMINI_MODEL no .env.")
        return

    st.error(f"Nao foi possivel gerar a resposta: {error_message}")


def build_word_options(selected_cards):
    defaults = ["trabalho", "onibus", "familia", "casa", "agua", "saude", "escola"]
    card_words = [card.lower() for card in selected_cards]
    options = []
    for word in card_words + defaults:
        if word and word not in options:
            options.append(word)
    return options


def yes_no(value):
    return "Sim" if value else "Nao"


def build_report(
    contexto_educador,
    fala_aluno,
    palavra_geradora,
    mediacao,
    exercicio,
    fala_significativa,
    situacao_limite,
    pergunta_aberta,
    conhece,
    escreve,
    fala,
    frase,
    frase_aluno,
):
    return f"""# Memoria do Circulo de Cultura

## Palavra geradora

{palavra_geradora or "Nao registrada"}

## Escuta inicial

**O que o educador percebeu**

{contexto_educador or "Nao registrado"}

**O que o aluno falou, escreveu ou apontou**

{fala_aluno or "Nao registrado"}

## Sugestao da FreireIA

{mediacao or "Nao gerada"}

## Atividade proposta

{exercicio or "Nao gerada"}

## Caminhada observada

**Fala significativa do aluno**

{fala_significativa or "Nao registrada"}

**Situacao-limite percebida ou hipotese para investigar**

{situacao_limite or "Nao registrada"}

**Pergunta que ficou aberta**

{pergunta_aberta or "Nao registrada"}

## Evidencias de aprendizagem

- Reconheceu a palavra escolhida: {yes_no(conhece)}
- Tentou escrever a palavra: {yes_no(escreve)}
- Falou sobre o sentido da palavra na propria vida: {yes_no(fala)}
- Criou uma frase com ajuda do educador: {yes_no(frase)}

## Frase ou registro produzido pelo aluno

{frase_aluno or "Nao registrado"}

## Proximo encontro

Retomar a palavra geradora, reler a fala significativa do aluno e aprofundar a pergunta que ficou aberta.
"""


def report_file_name():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"memoria_circulo_cultura_{timestamp}.md"


st.set_page_config(
    page_title="FreireIA",
    page_icon="book",
    layout="wide",
)

st.title("FreireIA")
st.caption("Apoio para transformar uma conversa real em atividade de alfabetizacao critica.")
st.info(FREIREIA_ROLE)

with st.sidebar:
    st.header("Antes de comecar")
    env_api_key = os.getenv("GEMINI_API_KEY", "")
    api_key = st.text_input(
        "Chave da API",
        value=env_api_key,
        type="password",
        help="Usada apenas nesta sessao para gerar as sugestoes da demo.",
    ).strip()
    idioma_label = st.selectbox("Idioma da atividade", list(LANGUAGES.keys()))
    idioma = LANGUAGES[idioma_label]

    st.divider()
    st.markdown("**Como usar com o educador**")
    st.markdown("1. Converse com o aluno")
    st.markdown("2. Registre o que apareceu")
    st.markdown("3. Escolha uma palavra")
    st.markdown("4. Aplique a atividade")

if not api_key:
    st.info("Informe a chave da API na barra lateral para iniciar a demo.")
    st.stop()

try:
    freire = FreireIA(api_key=api_key)
except Exception as exc:
    st.error(f"Nao foi possivel iniciar a demo: {exc}")
    st.stop()

if "active_step" not in st.session_state:
    st.session_state["active_step"] = "1. Escutar"

step_cols = st.columns(3)
steps = ["1. Escutar", "2. Criar atividade", "3. Registrar resultado"]
for col, step in zip(step_cols, steps):
    with col:
        button_type = "primary" if st.session_state["active_step"] == step else "secondary"
        if st.button(step, type=button_type, use_container_width=True):
            st.session_state["active_step"] = step
            st.rerun()

passo_atual = st.session_state["active_step"]

if passo_atual == "1. Escutar":
    st.subheader("1. Escutar o aluno")
    st.write("Use esta tela durante ou logo depois da conversa.")

    guide_col, record_col = st.columns([1, 2])

    with guide_col:
        st.markdown("### Preparar a conversa")
        st.markdown(DEFAULT_LISTENING_GUIDE)

    with record_col:
        st.markdown("### Registrar o que aconteceu")
        contexto_educador = st.text_area(
            "O que o educador percebeu?",
            value=st.session_state.get("contexto_educador", ""),
            placeholder="Ex.: aluno adulto, trabalha em mercado, chega cansado, quer ler mensagens no celular.",
            height=120,
        )
        fala_aluno = st.text_area(
            "O que o aluno falou, escreveu ou apontou?",
            value=st.session_state.get("fala_aluno", ""),
            placeholder="Ex.: eu pego onibus cedo, trabalho o dia todo e quero ajudar minha familia.",
            height=120,
        )

        obs_col, card_col = st.columns(2)
        with obs_col:
            observacoes = st.multiselect("O que chamou atencao?", OBSERVATIONS)
        with card_col:
            cartoes = st.multiselect("Imagens ou temas escolhidos", LIFE_CARDS)

        if st.button("Sugerir palavras geradoras", type="primary"):
            if not contexto_educador.strip() and not fala_aluno.strip() and not cartoes:
                st.warning("Registre pelo menos uma fala, observacao ou imagem escolhida.")
            else:
                st.session_state["contexto_educador"] = contexto_educador
                st.session_state["fala_aluno"] = fala_aluno
                with st.spinner("Organizando a escuta..."):
                    try:
                        response = freire.mediar_dialogo(
                            contexto_educador=contexto_educador,
                            fala_aluno=fala_aluno,
                            sinais_observados=observacoes,
                            cartoes_escolhidos=cartoes,
                            idioma=idioma,
                        )
                        st.session_state["mediacao"] = extract_text(response)
                    except Exception as exc:
                        show_generation_error(exc)

    if "mediacao" in st.session_state:
        st.markdown("### Sugestao da FreireIA")
        st.markdown(st.session_state["mediacao"])

        st.markdown("### Escolher a palavra geradora")
        st.write("Escolha uma palavra que faca sentido para o aluno. Voce pode usar uma sugestao ou digitar outra.")
        word_options = build_word_options(cartoes)
        palavra_sugerida = st.selectbox("Sugestoes rapidas", word_options)
        palavra_livre = st.text_input(
            "Outra palavra, se preferir",
            placeholder="Ex.: mercado, celular, descanso",
        )
        palavra_escolhida = (palavra_livre or palavra_sugerida).strip()

        if st.button("Usar esta palavra e criar atividade", type="primary"):
            st.session_state["palavra_geradora"] = palavra_escolhida
            st.session_state["active_step"] = "2. Criar atividade"
            st.rerun()

if passo_atual == "2. Criar atividade":
    st.subheader("2. Criar uma atividade")
    st.write(
        "Depois da escuta, escolha uma palavra geradora. A atividade deve comecar pelo "
        "sentido da palavra no mundo do aluno, antes das silabas."
    )

    palavra = st.text_input(
        "Qual palavra voces escolheram?",
        value=st.session_state.get("palavra_geradora", ""),
        placeholder="Ex.: trabalho, onibus, casa, agua",
    )
    contexto_para_exercicio = st.text_area(
        "Contexto para adaptar a atividade",
        value=st.session_state.get("contexto_educador", ""),
        placeholder="Cole aqui um resumo da escuta, se quiser adaptar melhor a atividade.",
        height=110,
    )

    if st.button("Criar atividade de alfabetizacao", type="primary"):
        if not palavra.strip():
            st.warning("Digite a palavra escolhida antes de criar a atividade.")
        else:
            st.session_state["palavra_geradora"] = palavra.strip()
            with st.spinner("Criando atividade..."):
                try:
                    response = freire.alfabetizar(
                        palavra=palavra.strip(),
                        contexto=contexto_para_exercicio,
                        idioma=idioma,
                    )
                    st.session_state["exercicio"] = extract_text(response)
                except Exception as exc:
                    show_generation_error(exc)

    if "exercicio" in st.session_state:
        st.markdown("### Atividade sugerida")
        st.markdown(st.session_state["exercicio"])

        if st.button("Registrar resultado da sessao", type="primary"):
            st.session_state["active_step"] = "3. Registrar resultado"
            st.rerun()

if passo_atual == "3. Registrar resultado":
    st.subheader("3. Registrar resultado")
    st.write("Ao final da conversa, registre a caminhada do aluno e o que ficou aberto para o proximo encontro.")

    conhece = st.checkbox("Reconheceu a palavra escolhida", key="conhece_palavra")
    escreve = st.checkbox("Tentou escrever a palavra", key="escreveu_palavra")
    fala = st.checkbox("Relacionou a palavra com a propria vida", key="explicou_sentido")
    frase = st.checkbox("Criou uma frase com ajuda do educador", key="criou_frase")

    progresso = sum([conhece, escreve, fala, frase]) / 4
    st.progress(progresso)

    fala_significativa = st.text_area(
        "Fala significativa do aluno",
        key="fala_significativa",
        placeholder="Ex.: Eu trabalho muito, mas queria ter mais tempo para estudar.",
    )

    situacao_limite = st.text_area(
        "Situacao-limite percebida ou hipotese para investigar",
        key="situacao_limite",
        placeholder="Ex.: cansaco no trajeto, pouco tempo para estudar, vergonha de ler mensagens.",
    )

    pergunta_aberta = st.text_area(
        "Pergunta que ficou aberta para o proximo encontro",
        key="pergunta_aberta",
        placeholder="Ex.: O tempo de descanso do aluno e respeitado?",
    )

    frase_aluno = st.text_area(
        "Frase ou registro produzido pelo aluno",
        key="frase_aluno",
        placeholder="Ex.: O trabalho ajuda minha familia, mas eu tambem preciso descansar.",
    )

    if progresso == 1:
        st.success("Sessao concluida: houve escuta, palavra geradora e evidencia de aprendizagem.")
    else:
        st.info("Tudo bem se nem todos os itens forem marcados. Use o registro para planejar o proximo encontro.")

    st.markdown("### Memoria do Circulo de Cultura")
    st.write("Gere uma memoria da caminhada para guardar, compartilhar com a equipe ou planejar o proximo encontro.")

    if st.button("Gerar memoria"):
        st.session_state["relatorio"] = build_report(
            contexto_educador=st.session_state.get("contexto_educador", ""),
            fala_aluno=st.session_state.get("fala_aluno", ""),
            palavra_geradora=st.session_state.get("palavra_geradora", ""),
            mediacao=st.session_state.get("mediacao", ""),
            exercicio=st.session_state.get("exercicio", ""),
            fala_significativa=fala_significativa,
            situacao_limite=situacao_limite,
            pergunta_aberta=pergunta_aberta,
            conhece=conhece,
            escreve=escreve,
            fala=fala,
            frase=frase,
            frase_aluno=frase_aluno,
        )

    if "relatorio" in st.session_state:
        st.markdown(st.session_state["relatorio"])
        st.download_button(
            "Baixar memoria em Markdown",
            data=st.session_state["relatorio"],
            file_name=report_file_name(),
            mime="text/markdown",
        )
