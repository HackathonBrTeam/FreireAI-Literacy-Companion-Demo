"""FreireAI Literacy Companion - MVP Streamlit.

Aplicativo demonstrativo para o Gemma 4 Good Hackathon.
"""

import streamlit as st

from app.agents.context_agent import ContextAgent
from app.agents.generative_word_agent import GenerativeWordAgent
from app.agents.linguistic_agent import LinguisticAgent
from app.agents.pedagogical_agent import PedagogicalAgent
from app.agents.safety_trust_agent import SafetyTrustAgent
from app.services.ai_gateway import AIGateway


st.set_page_config(
    page_title="FreireAI Literacy Companion",
    page_icon="📚",
    layout="centered",
)


def initialize_state() -> None:
    """Inicializa o estado da sessão para manter o fluxo do aluno."""
    defaults = {
        "step": 1,
        "learner_name": "",
        "target_language": "Português",
        "context_answer": "",
        "selected_word": None,
        "lesson": None,
        "progress": [],
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def next_step(step: int) -> None:
    """Avança o fluxo para uma etapa específica."""
    st.session_state.step = step


def render_header() -> None:
    """Renderiza o cabeçalho do aplicativo."""
    st.title("📚 FreireAI Literacy Companion")
    st.caption("Alfabetização multilíngue inspirada em Paulo Freire e apoiada por Gemma.")


def render_step_1() -> None:
    """Tela inicial de boas-vindas."""
    st.subheader("Tela 1: Boas-vindas")
    st.write("Toque em começar para iniciar sua jornada de alfabetização.")
    if st.button("🎙️ Começar", use_container_width=True):
        next_step(2)


def render_step_2() -> None:
    """Coleta identificação básica e idioma desejado."""
    st.subheader("Tela 2: Identificação")

    st.session_state.learner_name = st.text_input(
        "Qual é o seu nome?",
        value=st.session_state.learner_name,
        placeholder="Ex.: João",
    )

    st.session_state.target_language = st.selectbox(
        "Em qual idioma você quer aprender?",
        ["Português", "Inglês", "Espanhol", "Francês"],
        index=["Português", "Inglês", "Espanhol", "Francês"].index(st.session_state.target_language),
    )

    if st.button("Continuar", use_container_width=True):
        next_step(3)


def render_step_3() -> None:
    """Pergunta freireana para descobrir temas significativos."""
    learner_name = st.session_state.learner_name or "estudante"
    st.subheader("Tela 3: Sondagem freireana")
    st.write(f"{learner_name}, me fale um pouco sobre você.")

    st.session_state.context_answer = st.text_area(
        "O que você mais gosta de fazer na sua comunidade?",
        value=st.session_state.context_answer,
        placeholder="Ex.: Eu gosto de jogar bola, ajudar em casa e ir ao trabalho.",
    )

    if st.button("Gerar palavra geradora", use_container_width=True):
        ai = AIGateway()
        context_agent = ContextAgent(ai)
        word_agent = GenerativeWordAgent(ai)
        safety_agent = SafetyTrustAgent()

        context = context_agent.extract_context(st.session_state.context_answer)
        word = word_agent.select_word(context, st.session_state.target_language)
        validation = safety_agent.validate_word(word)

        if validation["is_safe"]:
            st.session_state.selected_word = word
            next_step(4)
        else:
            st.warning(validation["message"])


def render_step_4() -> None:
    """Apresenta palavra geradora e família silábica."""
    word = st.session_state.selected_word

    st.subheader("Tela 4: Palavra geradora")
    st.success(f"Palavra geradora: **{word['word'].upper()}**")
    st.write(word["reason"])

    linguistic_agent = LinguisticAgent()
    lesson = linguistic_agent.build_lesson(word["word"], st.session_state.target_language)
    st.session_state.lesson = lesson

    st.markdown("### Sílabas")
    st.write(" + ".join(lesson["syllables"]))

    st.markdown("### Família silábica")
    st.write(", ".join(lesson["syllabic_family"]))

    if st.button("Praticar descoberta", use_container_width=True):
        next_step(5)


def render_step_5() -> None:
    """Atividade de combinação de sílabas."""
    lesson = st.session_state.lesson

    st.subheader("Tela 5: Descoberta")
    st.write("Combine sílabas para criar novas palavras.")

    st.info(f"Exemplo: {' + '.join(lesson['syllables'])} = {lesson['word'].upper()}")

    answer = st.text_input("Digite a palavra formada:")
    if st.button("Verificar", use_container_width=True):
        pedagogical_agent = PedagogicalAgent()
        feedback = pedagogical_agent.evaluate_answer(answer, lesson["word"])

        st.session_state.progress.append(feedback)

        if feedback["correct"]:
            st.success(feedback["message"])
            next_step(6)
        else:
            st.warning(feedback["message"])


def render_step_6() -> None:
    """Tela de conquista e próxima palavra."""
    lesson = st.session_state.lesson

    st.subheader("Tela 6: Conquista")
    st.balloons()
    st.success(f"Parabéns! Você formou **{lesson['word'].upper()}**.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Repetir", use_container_width=True):
            next_step(5)

    with col2:
        if st.button("Próxima palavra", use_container_width=True):
            st.session_state.selected_word = None
            st.session_state.lesson = None
            next_step(3)

    st.markdown("### Progresso")
    st.write(f"Atividades realizadas: {len(st.session_state.progress)}")


def main() -> None:
    """Orquestra as telas do MVP."""
    initialize_state()
    render_header()

    steps = {
        1: render_step_1,
        2: render_step_2,
        3: render_step_3,
        4: render_step_4,
        5: render_step_5,
        6: render_step_6,
    }

    steps[st.session_state.step]()


if __name__ == "__main__":
    main()
