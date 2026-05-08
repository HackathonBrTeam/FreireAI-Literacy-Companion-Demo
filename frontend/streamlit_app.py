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
    "Português (Brasil)": "pt",
    "Español": "es",
    "English": "en",
}

DEFAULT_LANGUAGE = "en"


def normalize_language(value):
    language = (value or "").strip().lower()
    if not language:
        return DEFAULT_LANGUAGE

    primary_language = language.split(",", 1)[0].split(";", 1)[0].split("-", 1)[0].split("_", 1)[0]
    if primary_language in {"pt", "es", "en"}:
        return primary_language
    return DEFAULT_LANGUAGE


def detect_user_language():
    context = getattr(st, "context", None)
    if context is None:
        return DEFAULT_LANGUAGE

    locale = getattr(context, "locale", None)
    if locale:
        return normalize_language(locale)

    headers = getattr(context, "headers", {}) or {}
    accept_language = headers.get("accept-language") or headers.get("Accept-Language")
    return normalize_language(accept_language)


def language_index(language_code):
    codes = list(LANGUAGES.values())
    try:
        return codes.index(language_code)
    except ValueError:
        return codes.index(DEFAULT_LANGUAGE)


TEXT = {
    "pt": {
        "caption": "Apoio para transformar uma conversa real em atividade de alfabetização crítica.",
        "role": "A FreireIA não substitui o educador. Ela ajuda a escutar o aluno, organizar o que apareceu na conversa e sugerir uma palavra para criar uma atividade de alfabetização.",
        "api_missing": "Configure GEMINI_API_KEY em .streamlit/secrets.toml ou no arquivo .env para iniciar a demo.",
        "language": "Idioma da atividade",
        "how_to": "Como usar com o educador",
        "how_steps": ["Converse com o aluno", "Registre o que apareceu", "Escolha uma palavra", "Aplique a atividade"],
        "model": "Modelo configurado",
        "steps": ["1. Escutar", "2. Criar atividade", "3. Registrar resultado"],
        "session": "sessão",
        "step1_title": "1. Escutar o aluno",
        "step1_help": "Use esta tela durante ou logo depois da conversa.",
        "prepare": "Preparar a conversa",
        "guide": """
**Convite inicial**

Comece com uma conversa tranquila. Diga ao aluno que ele pode falar, apontar, desenhar ou escolher imagens. O importante é entender o que faz parte da vida dele.

**O que observar**

Preste atenção em palavras repetidas, temas que aparecem com emoção, gestos, imagens escolhidas e situações ligadas a trabalho, casa, família, transporte, saúde ou comunidade.
""",
        "questions_title": "Perguntas já exploradas",
        "questions": [
            "Como foi seu dia hoje?",
            "Que palavras aparecem muito na sua rotina?",
            "O que você gostaria de conseguir ler melhor?",
            "Que lugar, pessoa ou trabalho é importante para você?",
            "Tem alguma palavra que você vê sempre e gostaria de entender ou escrever?",
        ],
        "record": "Registrar o que aconteceu",
        "educator_noticed": "O que o educador percebeu?",
        "educator_placeholder": "Ex.: aluno adulto, trabalha em mercado, chega cansado, quer ler mensagens no celular.",
        "learner_said": "O que o aluno falou, escreveu ou apontou?",
        "learner_placeholder": "Ex.: eu pego ônibus cedo, trabalho o dia todo e quero ajudar minha família.",
        "noticed": "O que chamou atenção?",
        "observations": ["Falou com segurança", "Ficou em silêncio", "Apontou para imagens", "Pareceu cansado", "Pareceu animado", "Pediu ajuda para ler", "Misturou idiomas"],
        "themes": "Imagens ou temas escolhidos",
        "cards": ["Casa", "Trabalho", "Família", "Ônibus", "Água", "Escola", "Comida", "Saúde", "Bairro"],
        "next_action": "Próxima ação",
        "suggest_words": "Sugerir palavras geradoras",
        "need_input": "Registre pelo menos uma fala, observação ou imagem escolhida.",
        "listening_spinner": "Organizando a escuta...",
        "suggestion": "Sugestão da FreireIA",
        "choose_word_title": "Escolher a palavra geradora",
        "choose_word_help": "Escolha uma palavra que faça sentido para o aluno. Você pode usar uma sugestão ou digitar outra.",
        "quick_suggestions": "Sugestões rápidas",
        "other_word": "Outra palavra, se preferir",
        "other_word_placeholder": "Ex.: mercado, celular, descanso",
        "use_word": "Usar esta palavra e criar atividade",
        "step2_title": "2. Criar uma atividade",
        "step2_help": "Depois da escuta, escolha uma palavra geradora. A atividade deve começar pelo sentido da palavra no mundo do aluno, antes das sílabas.",
        "chosen_word": "Qual palavra vocês escolheram?",
        "chosen_word_placeholder": "Ex.: trabalho, ônibus, casa, água",
        "activity_context": "Contexto para adaptar a atividade",
        "activity_context_placeholder": "Cole aqui um resumo da escuta, se quiser adaptar melhor a atividade.",
        "scene": "Cena para observar com o aluno",
        "scene_placeholder": "Ex.: Uma pessoa esperando ônibus cedo para chegar ao trabalho.",
        "scene_help": "Use esta cena como codificação visual: uma imagem, objeto ou situação para conversar antes das sílabas.",
        "create_activity": "Criar atividade de alfabetização",
        "need_word": "Digite a palavra escolhida antes de criar a atividade.",
        "activity_spinner": "Criando atividade...",
        "activity": "Atividade sugerida",
        "go_record": "Registrar resultado da sessão",
        "step3_title": "3. Registrar resultado",
        "step3_help": "Ao final da conversa, registre a caminhada do aluno e o que ficou aberto para o próximo encontro.",
        "recognized": "Reconheceu a palavra escolhida",
        "wrote": "Tentou escrever a palavra",
        "related": "Relacionou a palavra com a própria vida",
        "sentence_help": "Criou uma frase com ajuda do educador",
        "meaningful_speech": "Fala significativa do aluno",
        "meaningful_placeholder": "Ex.: Eu trabalho muito, mas queria ter mais tempo para estudar.",
        "limit_situation": "Situação-limite percebida ou hipótese para investigar",
        "limit_placeholder": "Ex.: cansaço no trajeto, pouco tempo para estudar, vergonha de ler mensagens.",
        "open_question": "Pergunta que ficou aberta para o próximo encontro",
        "open_question_placeholder": "Ex.: O tempo de descanso do aluno é respeitado?",
        "learner_sentence": "Frase ou registro produzido pelo aluno",
        "learner_sentence_placeholder": "Ex.: O trabalho ajuda minha família, mas eu também preciso descansar.",
        "success": "Sessão concluída: houve escuta, palavra geradora e evidência de aprendizagem.",
        "continue": "Tudo bem se nem todos os itens forem marcados. Use o registro para planejar o próximo encontro.",
        "memory": "Memória do Círculo de Cultura",
        "memory_help": "Gere uma memória da caminhada para guardar, compartilhar com a equipe ou planejar o próximo encontro.",
        "generate_memory": "Gerar memória",
        "download_memory": "Baixar memória em Markdown",
        "usage_title": "Consumo estimado",
        "input_tokens": "Tokens de entrada",
        "output_tokens": "Tokens de saída",
        "total_tokens": "Tokens totais",
        "estimated_spent": "Valor estimado usado",
        "estimated_remaining": "Saldo estimado",
        "usage_note": "Estimativa local da sessão. O saldo real deve ser conferido no Google Billing.",
        "reset_usage": "Zerar contador",
        "usage_section": "Uso da IA",
        "consent_title": "Antes de usar a demo",
        "consent_intro": "Esta é uma versão de validação por convite. Use exemplos fictícios ou dados mínimos, sem registrar informações sensíveis de alunos.",
        "consent_check": "Entendi que esta demo não substitui o educador, não deve receber dados sensíveis e será usada apenas para avaliação.",
        "consent_button": "Começar avaliação",
        "feedback_title": "Impressões sobre a demo",
        "feedback_help": "Registre suas impressões para ajudar a melhorar a FreireIA.",
        "feedback_profile": "Seu perfil",
        "feedback_profile_options": ["Educador(a)", "Gestor(a)", "Pesquisador(a)", "Estudante", "Outro"],
        "feedback_rating": "A demo foi útil para imaginar uma prática real?",
        "feedback_helped": "O que mais ajudou?",
        "feedback_confusing": "O que ficou confuso ou difícil?",
        "feedback_change": "Que melhoria você sugere antes de testar com alunos reais?",
        "feedback_contact": "Contato, se quiser receber retorno",
        "feedback_form": "Enviar feedback pelo formulário",
        "feedback_markdown": "Gerar registro de feedback",
        "download_feedback": "Baixar feedback em Markdown",
        "feedback_ready": "Registro de feedback gerado.",
        "yes": "Sim",
        "no": "Não",
        "not_recorded": "Não registrado",
        "not_generated": "Não gerada",
    },
    "es": {
        "caption": "Apoyo para transformar una conversación real en una actividad de alfabetización crítica.",
        "role": "FreireIA no sustituye al educador. Ayuda a escuchar al estudiante, organizar lo que apareció en la conversación y sugerir una palabra para crear una actividad de alfabetización.",
        "api_missing": "Configura GEMINI_API_KEY en .streamlit/secrets.toml o en el archivo .env para iniciar la demo.",
        "language": "Idioma de la actividad",
        "how_to": "Cómo usar con el educador",
        "how_steps": ["Converse con el estudiante", "Registre lo que apareció", "Elija una palabra", "Aplique la actividad"],
        "model": "Modelo configurado",
        "steps": ["1. Escuchar", "2. Crear actividad", "3. Registrar resultado"],
        "session": "sesión",
        "step1_title": "1. Escuchar al estudiante",
        "step1_help": "Use esta pantalla durante o justo después de la conversación.",
        "prepare": "Preparar la conversación",
        "guide": """
**Invitación inicial**

Comience con una conversación tranquila. Dígale al estudiante que puede hablar, señalar, dibujar o elegir imágenes. Lo importante es entender qué forma parte de su vida.

**Qué observar**

Preste atención a palabras repetidas, temas que aparecen con emoción, gestos, imágenes elegidas y situaciones ligadas al trabajo, casa, familia, transporte, salud o comunidad.
""",
        "questions_title": "Preguntas ya exploradas",
        "questions": [
            "¿Cómo fue tu día hoy?",
            "¿Qué palabras aparecen mucho en tu rutina?",
            "¿Qué te gustaría poder leer mejor?",
            "¿Qué lugar, persona o trabajo es importante para ti?",
            "¿Hay alguna palabra que ves siempre y te gustaría entender o escribir?",
        ],
        "record": "Registrar lo que ocurrió",
        "educator_noticed": "¿Qué percibió el educador?",
        "educator_placeholder": "Ej.: estudiante adulto, trabaja en mercado, llega cansado, quiere leer mensajes en el celular.",
        "learner_said": "¿Qué dijo, escribió o señaló el estudiante?",
        "learner_placeholder": "Ej.: tomo el autobús temprano, trabajo todo el día y quiero ayudar a mi familia.",
        "noticed": "¿Qué llamó la atención?",
        "observations": ["Habló con seguridad", "Quedó en silencio", "Señaló imágenes", "Pareció cansado", "Pareció animado", "Pidió ayuda para leer", "Mezcló idiomas"],
        "themes": "Imágenes o temas elegidos",
        "cards": ["Casa", "Trabajo", "Familia", "Autobús", "Agua", "Escuela", "Comida", "Salud", "Barrio"],
        "next_action": "Próxima acción",
        "suggest_words": "Sugerir palabras generadoras",
        "need_input": "Registre al menos una frase, observación o imagen elegida.",
        "listening_spinner": "Organizando la escucha...",
        "suggestion": "Sugerencia de FreireIA",
        "choose_word_title": "Elegir la palabra generadora",
        "choose_word_help": "Elija una palabra que tenga sentido para el estudiante. Puede usar una sugerencia o escribir otra.",
        "quick_suggestions": "Sugerencias rápidas",
        "other_word": "Otra palabra, si prefiere",
        "other_word_placeholder": "Ej.: mercado, celular, descanso",
        "use_word": "Usar esta palabra y crear actividad",
        "step2_title": "2. Crear una actividad",
        "step2_help": "Después de la escucha, elija una palabra generadora. La actividad debe comenzar por el sentido de la palabra en el mundo del estudiante, antes de las sílabas.",
        "chosen_word": "¿Qué palabra eligieron?",
        "chosen_word_placeholder": "Ej.: trabajo, autobús, casa, agua",
        "activity_context": "Contexto para adaptar la actividad",
        "activity_context_placeholder": "Pegue aquí un resumen de la escucha, si quiere adaptar mejor la actividad.",
        "scene": "Escena para observar con el estudiante",
        "scene_placeholder": "Ej.: Una persona esperando el autobús temprano para llegar al trabajo.",
        "scene_help": "Use esta escena como codificación visual: una imagen, objeto o situación para conversar antes de las sílabas.",
        "create_activity": "Crear actividad de alfabetización",
        "need_word": "Escriba la palabra elegida antes de crear la actividad.",
        "activity_spinner": "Creando actividad...",
        "activity": "Actividad sugerida",
        "go_record": "Registrar resultado de la sesión",
        "step3_title": "3. Registrar resultado",
        "step3_help": "Al final de la conversación, registre el recorrido del estudiante y lo que quedó abierto para el próximo encuentro.",
        "recognized": "Reconoció la palabra elegida",
        "wrote": "Intentó escribir la palabra",
        "related": "Relacionó la palabra con su propia vida",
        "sentence_help": "Creó una frase con ayuda del educador",
        "meaningful_speech": "Frase significativa del estudiante",
        "meaningful_placeholder": "Ej.: Trabajo mucho, pero quisiera tener más tiempo para estudiar.",
        "limit_situation": "Situación-límite percibida o hipótesis para investigar",
        "limit_placeholder": "Ej.: cansancio en el trayecto, poco tiempo para estudiar, vergüenza de leer mensajes.",
        "open_question": "Pregunta que quedó abierta para el próximo encuentro",
        "open_question_placeholder": "Ej.: ¿Se respeta el tiempo de descanso del estudiante?",
        "learner_sentence": "Frase o registro producido por el estudiante",
        "learner_sentence_placeholder": "Ej.: El trabajo ayuda a mi familia, pero también necesito descansar.",
        "success": "Sesión concluida: hubo escucha, palabra generadora y evidencia de aprendizaje.",
        "continue": "Está bien si no todos los elementos fueron marcados. Use el registro para planear el próximo encuentro.",
        "memory": "Memoria del Círculo de Cultura",
        "memory_help": "Genere una memoria del recorrido para guardar, compartir con el equipo o planear el próximo encuentro.",
        "generate_memory": "Generar memoria",
        "download_memory": "Descargar memoria en Markdown",
        "usage_title": "Consumo estimado",
        "input_tokens": "Tokens de entrada",
        "output_tokens": "Tokens de salida",
        "total_tokens": "Tokens totales",
        "estimated_spent": "Valor estimado usado",
        "estimated_remaining": "Saldo estimado",
        "usage_note": "Estimación local de la sesión. El saldo real debe verificarse en Google Billing.",
        "reset_usage": "Reiniciar contador",
        "usage_section": "Uso de IA",
        "consent_title": "Antes de usar la demo",
        "consent_intro": "Esta es una versión de validación por invitación. Use ejemplos ficticios o datos mínimos, sin registrar información sensible de estudiantes.",
        "consent_check": "Entiendo que esta demo no sustituye al educador, no debe recibir datos sensibles y será usada solo para evaluación.",
        "consent_button": "Comenzar evaluación",
        "feedback_title": "Impresiones sobre la demo",
        "feedback_help": "Registre sus impresiones para ayudar a mejorar FreireIA.",
        "feedback_profile": "Su perfil",
        "feedback_profile_options": ["Educador(a)", "Gestor(a)", "Investigador(a)", "Estudiante", "Otro"],
        "feedback_rating": "¿La demo fue útil para imaginar una práctica real?",
        "feedback_helped": "¿Qué fue lo que más ayudó?",
        "feedback_confusing": "¿Qué quedó confuso o difícil?",
        "feedback_change": "¿Qué mejora sugiere antes de probar con estudiantes reales?",
        "feedback_contact": "Contacto, si desea recibir respuesta",
        "feedback_form": "Enviar feedback por el formulario",
        "feedback_markdown": "Generar registro de feedback",
        "download_feedback": "Descargar feedback en Markdown",
        "feedback_ready": "Registro de feedback generado.",
        "yes": "Sí",
        "no": "No",
        "not_recorded": "No registrado",
        "not_generated": "No generada",
    },
    "en": {
        "caption": "Support for turning a real conversation into a critical literacy activity.",
        "role": "FreireIA does not replace the educator. It helps listen to the learner, organize what emerged in the conversation, and suggest a word to create a literacy activity.",
        "api_missing": "Configure GEMINI_API_KEY in .streamlit/secrets.toml or the .env file to start the demo.",
        "language": "Activity Language",
        "how_to": "How to Use With the Educator",
        "how_steps": ["Talk with the learner", "Record what emerged", "Choose a word", "Apply the activity"],
        "model": "Configured model",
        "steps": ["1. Listen", "2. Create Activity", "3. Record Result"],
        "session": "session",
        "step1_title": "1. Listen to the learner",
        "step1_help": "Use this screen during or right after the conversation.",
        "prepare": "Prepare the conversation",
        "guide": """
**Opening invitation**

Start with a calm conversation. Tell the learner they can speak, point, draw, or choose images. The important thing is to understand what is part of their life.

**What to observe**

Pay attention to repeated words, emotionally charged themes, gestures, selected images, and situations related to work, home, family, transportation, health, or community.
""",
        "questions_title": "Questions already explored",
        "questions": [
            "How was your day today?",
            "What words appear often in your routine?",
            "What would you like to read better?",
            "What place, person, or work is important to you?",
            "Is there a word you often see and would like to understand or write?",
        ],
        "record": "Record what happened",
        "educator_noticed": "What did the educator notice?",
        "educator_placeholder": "Ex.: adult learner, works at a market, arrives tired, wants to read phone messages.",
        "learner_said": "What did the learner say, write, or point to?",
        "learner_placeholder": "Ex.: I take the bus early, work all day, and want to help my family.",
        "noticed": "What stood out?",
        "observations": ["Spoke confidently", "Stayed silent", "Pointed to images", "Seemed tired", "Seemed excited", "Asked for help reading", "Mixed languages"],
        "themes": "Images or themes chosen",
        "cards": ["Home", "Work", "Family", "Bus", "Water", "School", "Food", "Health", "Neighborhood"],
        "next_action": "Next action",
        "suggest_words": "Suggest generative words",
        "need_input": "Record at least one statement, observation, or selected image.",
        "listening_spinner": "Organizing the listening...",
        "suggestion": "FreireIA suggestion",
        "choose_word_title": "Choose the generative word",
        "choose_word_help": "Choose a word that makes sense for the learner. You can use a suggestion or type another one.",
        "quick_suggestions": "Quick suggestions",
        "other_word": "Another word, if preferred",
        "other_word_placeholder": "Ex.: market, phone, rest",
        "use_word": "Use this word and create activity",
        "step2_title": "2. Create an activity",
        "step2_help": "After listening, choose a generative word. The activity should begin with the word's meaning in the learner's world, before syllables.",
        "chosen_word": "Which word did you choose?",
        "chosen_word_placeholder": "Ex.: work, bus, home, water",
        "activity_context": "Context to adapt the activity",
        "activity_context_placeholder": "Paste a summary of the listening here if you want to adapt the activity.",
        "scene": "Scene to observe with the learner",
        "scene_placeholder": "Ex.: A person waiting for the bus early to get to work.",
        "scene_help": "Use this scene as visual codification: an image, object, or situation to discuss before syllables.",
        "create_activity": "Create literacy activity",
        "need_word": "Type the chosen word before creating the activity.",
        "activity_spinner": "Creating activity...",
        "activity": "Suggested activity",
        "go_record": "Record session result",
        "step3_title": "3. Record result",
        "step3_help": "At the end of the conversation, record the learner's journey and what remains open for the next meeting.",
        "recognized": "Recognized the chosen word",
        "wrote": "Tried to write the word",
        "related": "Connected the word to their own life",
        "sentence_help": "Created a sentence with educator support",
        "meaningful_speech": "Meaningful learner statement",
        "meaningful_placeholder": "Ex.: I work a lot, but I wish I had more time to study.",
        "limit_situation": "Perceived limit-situation or hypothesis to investigate",
        "limit_placeholder": "Ex.: tired commute, little time to study, shame around reading messages.",
        "open_question": "Question left open for the next meeting",
        "open_question_placeholder": "Ex.: Is the learner's rest time respected?",
        "learner_sentence": "Sentence or record produced by the learner",
        "learner_sentence_placeholder": "Ex.: Work helps my family, but I also need to rest.",
        "success": "Session complete: listening, generative word, and learning evidence were recorded.",
        "continue": "It is okay if not every item is checked. Use the record to plan the next meeting.",
        "memory": "Memory of the Culture Circle",
        "memory_help": "Generate a memory of the journey to keep, share with the team, or plan the next meeting.",
        "generate_memory": "Generate memory",
        "download_memory": "Download memory as Markdown",
        "usage_title": "Estimated usage",
        "input_tokens": "Input tokens",
        "output_tokens": "Output tokens",
        "total_tokens": "Total tokens",
        "estimated_spent": "Estimated amount used",
        "estimated_remaining": "Estimated balance",
        "usage_note": "Local session estimate. Check the real balance in Google Billing.",
        "reset_usage": "Reset counter",
        "usage_section": "AI usage",
        "consent_title": "Before using the demo",
        "consent_intro": "This is an invite-based validation version. Use fictional examples or minimal data, without recording sensitive learner information.",
        "consent_check": "I understand this demo does not replace the educator, should not receive sensitive data, and will be used only for evaluation.",
        "consent_button": "Start evaluation",
        "feedback_title": "Demo impressions",
        "feedback_help": "Record your impressions to help improve FreireIA.",
        "feedback_profile": "Your profile",
        "feedback_profile_options": ["Educator", "Manager", "Researcher", "Learner", "Other"],
        "feedback_rating": "Was the demo useful for imagining a real practice?",
        "feedback_helped": "What helped the most?",
        "feedback_confusing": "What was confusing or difficult?",
        "feedback_change": "What improvement do you suggest before testing with real learners?",
        "feedback_contact": "Contact, if you want a follow-up",
        "feedback_form": "Send feedback through the form",
        "feedback_markdown": "Generate feedback record",
        "download_feedback": "Download feedback as Markdown",
        "feedback_ready": "Feedback record generated.",
        "yes": "Yes",
        "no": "No",
        "not_recorded": "Not recorded",
        "not_generated": "Not generated",
    },
}


load_dotenv(ROOT_DIR / ".env")


CONFIG_KEYS = [
    "GEMINI_API_KEY",
    "GEMINI_MODEL",
    "GEMINI_MAX_OUTPUT_TOKENS",
    "GEMINI_BUDGET_BRL",
    "GEMINI_INPUT_BRL_PER_1M_TOKENS",
    "GEMINI_OUTPUT_BRL_PER_1M_TOKENS",
    "FEEDBACK_FORM_URL",
    "FREIREIA_REQUIRE_CONSENT",
]


def secret_value(name):
    try:
        value = st.secrets.get(name)
    except Exception:
        return None
    if value is None:
        return None
    return str(value)


def config_value(name, default=""):
    value = secret_value(name)
    if value:
        return value
    return os.getenv(name, default)


def sync_config_to_env():
    for key in CONFIG_KEYS:
        value = secret_value(key)
        if value:
            os.environ[key] = value


def extract_text(response):
    if hasattr(response, "text"):
        return response.text
    return str(response)


def get_float_env(name, default):
    raw_value = config_value(name, str(default)).replace(",", ".").strip()
    try:
        return float(raw_value)
    except ValueError:
        return float(default)


def initialize_usage_state():
    defaults = {
        "usage_input_tokens": 0,
        "usage_output_tokens": 0,
        "usage_total_tokens": 0,
        "usage_estimated_spent_brl": 0.0,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def response_usage(response):
    usage = getattr(response, "usage_metadata", None)
    if usage is None:
        return 0, 0, 0

    input_tokens = getattr(usage, "prompt_token_count", 0) or 0
    output_tokens = getattr(usage, "candidates_token_count", 0) or 0
    total_tokens = getattr(usage, "total_token_count", 0) or input_tokens + output_tokens
    return int(input_tokens), int(output_tokens), int(total_tokens)


def register_usage(response):
    input_tokens, output_tokens, total_tokens = response_usage(response)
    input_rate = get_float_env("GEMINI_INPUT_BRL_PER_1M_TOKENS", 0)
    output_rate = get_float_env("GEMINI_OUTPUT_BRL_PER_1M_TOKENS", 0)
    spent = (input_tokens / 1_000_000 * input_rate) + (output_tokens / 1_000_000 * output_rate)

    st.session_state["usage_input_tokens"] += input_tokens
    st.session_state["usage_output_tokens"] += output_tokens
    st.session_state["usage_total_tokens"] += total_tokens
    st.session_state["usage_estimated_spent_brl"] += spent


def format_brl(value):
    return f"R$ {value:,.4f}".replace(",", "X").replace(".", ",").replace("X", ".")


def render_usage_summary(container, t):
    budget = get_float_env("GEMINI_BUDGET_BRL", 0)
    spent = st.session_state["usage_estimated_spent_brl"]
    remaining = max(budget - spent, 0) if budget > 0 else 0

    with container:
        st.divider()
        st.markdown(f"**{t['usage_title']}**")
        st.caption(t["usage_note"])
        st.metric(t["total_tokens"], f"{st.session_state['usage_total_tokens']:,}".replace(",", "."))
        st.caption(f"{t['input_tokens']}: {st.session_state['usage_input_tokens']:,}".replace(",", "."))
        st.caption(f"{t['output_tokens']}: {st.session_state['usage_output_tokens']:,}".replace(",", "."))
        st.caption(f"{t['estimated_spent']}: {format_brl(spent)}")
        st.caption(f"{t['estimated_remaining']}: {format_brl(remaining)}")
        if st.button(t["reset_usage"]):
            for key in ["usage_input_tokens", "usage_output_tokens", "usage_total_tokens"]:
                st.session_state[key] = 0
            st.session_state["usage_estimated_spent_brl"] = 0.0
            st.rerun()


def show_generation_error(exc):
    error_message = str(exc)
    if "API_KEY_INVALID" in error_message:
        st.error("A chave da API foi rejeitada. Atualize o arquivo .env e reinicie a demo.")
        return
    if "RESOURCE_EXHAUSTED" in error_message or "quota" in error_message.lower():
        st.error("A chave está válida, mas a cota do projeto acabou ou ainda não foi liberada.")
        return
    if "UNAVAILABLE" in error_message or "high demand" in error_message.lower():
        st.error("O modelo está temporariamente sobrecarregado. Aguarde alguns segundos e clique novamente. Os dados preenchidos foram preservados na tela.")
        return
    if "not found" in error_message.lower() and "model" in error_message.lower():
        st.error("O modelo configurado não está disponível. Verifique GEMINI_MODEL no .env.")
        return
    st.error(f"Não foi possível gerar a resposta: {error_message}")


def build_word_options(selected_cards, lang):
    defaults = {
        "pt": ["trabalho", "ônibus", "família", "casa", "água", "saúde", "escola"],
        "es": ["trabajo", "autobús", "familia", "casa", "agua", "salud", "escuela"],
        "en": ["work", "bus", "family", "home", "water", "health", "school"],
    }
    card_words = [card.lower() for card in selected_cards]
    options = []
    for word in card_words + defaults[lang]:
        if word and word not in options:
            options.append(word)
    return options


def scene_suggestion(word, context, lang):
    word = (word or "").strip().lower()
    scenes = {
        "pt": {
            "trabalho": "Uma pessoa chegando ao trabalho cedo, com sinais de cansaço e compromisso.",
            "ônibus": "Um ponto de ônibus cheio no início do dia, com pessoas indo trabalhar.",
            "família": "Uma mesa simples em casa, com pessoas conversando depois de um dia de trabalho.",
            "casa": "A entrada de uma casa no bairro do aluno, com objetos do cotidiano.",
            "água": "Uma torneira, balde ou caixa d'água em uma cena de cuidado com a casa.",
            "saúde": "Uma pessoa esperando atendimento ou cuidando de alguém da família.",
            "escola": "Uma sala simples com caderno, lápis e uma palavra escrita no quadro.",
        },
        "es": {
            "trabajo": "Una persona llegando temprano al trabajo, con señales de cansancio y compromiso.",
            "autobús": "Una parada de autobús llena al inicio del día, con personas yendo a trabajar.",
            "familia": "Una mesa sencilla en casa, con personas conversando después de un día de trabajo.",
            "casa": "La entrada de una casa del barrio del estudiante, con objetos cotidianos.",
            "agua": "Un grifo, balde o tanque de agua en una escena de cuidado del hogar.",
            "salud": "Una persona esperando atención o cuidando a alguien de la familia.",
            "escuela": "Un aula sencilla con cuaderno, lápiz y una palabra escrita en la pizarra.",
        },
        "en": {
            "work": "A person arriving early at work, showing tiredness and commitment.",
            "bus": "A crowded bus stop early in the day, with people going to work.",
            "family": "A simple table at home, with people talking after a workday.",
            "home": "The entrance of a learner's home, with everyday objects.",
            "water": "A faucet, bucket, or water tank in a scene of home care.",
            "health": "A person waiting for care or helping someone in the family.",
            "school": "A simple classroom with notebook, pencil, and a word on the board.",
        },
    }
    fallbacks = {
        "pt": f"Uma cena do cotidiano do aluno relacionada à palavra '{word or 'escolhida'}'.",
        "es": f"Una escena cotidiana del estudiante relacionada con la palabra '{word or 'elegida'}'.",
        "en": f"An everyday scene from the learner's life related to the word '{word or 'chosen'}'.",
    }
    fallback = fallbacks[lang]
    if context:
        fallback += {
            "pt": " Use elementos do contexto registrado pelo educador.",
            "es": " Use elementos del contexto registrado por el educador.",
            "en": " Use elements from the context recorded by the educator.",
        }[lang]
    return scenes[lang].get(word, fallback)


def yes_no(value, lang):
    return TEXT[lang]["yes"] if value else TEXT[lang]["no"]


def build_report(data, lang):
    t = TEXT[lang]
    return f"""# {t["memory"]}

## {t["chosen_word"]}

{data["palavra_geradora"] or t["not_recorded"]}

## Escuta inicial / Initial listening / Escucha inicial

**{t["educator_noticed"]}**

{data["contexto_educador"] or t["not_recorded"]}

**{t["learner_said"]}**

{data["fala_aluno"] or t["not_recorded"]}

## {t["suggestion"]}

{data["mediacao"] or t["not_generated"]}

## {t["activity"]}

{data["exercicio"] or t["not_generated"]}

## {t["scene"]}

{data["cena_visual"] or t["not_recorded"]}

## Caminhada observada / Observed journey / Camino observado

**{t["meaningful_speech"]}**

{data["fala_significativa"] or t["not_recorded"]}

**{t["limit_situation"]}**

{data["situacao_limite"] or t["not_recorded"]}

**{t["open_question"]}**

{data["pergunta_aberta"] or t["not_recorded"]}

## Evidências de aprendizagem / Learning evidence / Evidencias de aprendizaje

- {t["recognized"]}: {yes_no(data["conhece"], lang)}
- {t["wrote"]}: {yes_no(data["escreve"], lang)}
- {t["related"]}: {yes_no(data["fala"], lang)}
- {t["sentence_help"]}: {yes_no(data["frase"], lang)}

## {t["learner_sentence"]}

{data["frase_aluno"] or t["not_recorded"]}

## {t["usage_section"]}

- {t["input_tokens"]}: {data["usage_input_tokens"]}
- {t["output_tokens"]}: {data["usage_output_tokens"]}
- {t["total_tokens"]}: {data["usage_total_tokens"]}
- {t["estimated_spent"]}: {data["usage_estimated_spent_brl"]}
- {t["estimated_remaining"]}: {data["usage_estimated_remaining_brl"]}

_{t["usage_note"]}_
"""


def report_file_name(lang):
    prefixes = {
        "pt": "memoria_circulo_cultura",
        "es": "memoria_circulo_cultura",
        "en": "culture_circle_memory",
    }
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefixes[lang]}_{timestamp}.md"


def feedback_file_name(lang):
    prefixes = {
        "pt": "feedback_freireia",
        "es": "feedback_freireia",
        "en": "freireia_feedback",
    }
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefixes[lang]}_{timestamp}.md"


def build_feedback(data, lang):
    t = TEXT[lang]
    return f"""# {t["feedback_title"]}

## {t["feedback_profile"]}

{data["profile"]}

## {t["feedback_rating"]}

{data["rating"]}/5

## {t["feedback_helped"]}

{data["helped"] or t["not_recorded"]}

## {t["feedback_confusing"]}

{data["confusing"] or t["not_recorded"]}

## {t["feedback_change"]}

{data["change"] or t["not_recorded"]}

## {t["feedback_contact"]}

{data["contact"] or t["not_recorded"]}
"""


def render_consent_gate(t):
    require_consent = config_value("FREIREIA_REQUIRE_CONSENT", "true").lower() not in {"0", "false", "no"}
    if not require_consent or st.session_state.get("consent_ok"):
        return

    st.markdown(f"### {t['consent_title']}")
    st.warning(t["consent_intro"])
    accepted = st.checkbox(t["consent_check"])
    if st.button(t["consent_button"], type="primary", disabled=not accepted):
        st.session_state["consent_ok"] = True
        st.rerun()
    st.stop()


def render_feedback_section(t, lang):
    st.divider()
    st.markdown(f"### {t['feedback_title']}")
    st.write(t["feedback_help"])

    feedback_url = config_value("FEEDBACK_FORM_URL", "").strip()
    if feedback_url:
        st.link_button(t["feedback_form"], feedback_url)

    with st.expander(t["feedback_markdown"]):
        profile = st.selectbox(t["feedback_profile"], t["feedback_profile_options"], key=f"feedback_profile_{lang}")
        rating = st.slider(t["feedback_rating"], min_value=1, max_value=5, value=4, key=f"feedback_rating_{lang}")
        helped = st.text_area(t["feedback_helped"], key=f"feedback_helped_{lang}")
        confusing = st.text_area(t["feedback_confusing"], key=f"feedback_confusing_{lang}")
        change = st.text_area(t["feedback_change"], key=f"feedback_change_{lang}")
        contact = st.text_input(t["feedback_contact"], key=f"feedback_contact_{lang}")

        if st.button(t["feedback_markdown"], key=f"feedback_generate_{lang}"):
            st.session_state["feedback_record"] = build_feedback(
                {
                    "profile": profile,
                    "rating": rating,
                    "helped": helped,
                    "confusing": confusing,
                    "change": change,
                    "contact": contact,
                },
                lang,
            )
            st.success(t["feedback_ready"])

        if "feedback_record" in st.session_state:
            st.download_button(
                t["download_feedback"],
                data=st.session_state["feedback_record"],
                file_name=feedback_file_name(lang),
                mime="text/markdown",
            )


st.set_page_config(page_title="FreireIA", page_icon="book", layout="wide")

st.markdown(
    """
    <style>
    .stButton > button { min-height: 2.8rem; font-weight: 650; }
    textarea, input, label, p, li { font-size: 1rem !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

sync_config_to_env()
initialize_usage_state()

with st.sidebar:
    detected_language = detect_user_language()
    selected_language = st.selectbox(
        "Idioma / Language / Idioma",
        list(LANGUAGES.keys()),
        index=language_index(detected_language),
    )
    idioma = LANGUAGES[selected_language]
    t = TEXT[idioma]
    api_key = config_value("GEMINI_API_KEY", "").strip()

    st.divider()
    st.markdown(f"**{t['how_to']}**")
    for idx, step in enumerate(t["how_steps"], start=1):
        st.markdown(f"{idx}. {step}")
    st.caption(f"{t['model']}: {config_value('GEMINI_MODEL', 'gemma-4-26b-a4b-it')}")
    usage_container = st.container()
    render_usage_summary(usage_container, t)

st.title("FreireIA")
st.caption(t["caption"])
st.info(t["role"])
render_consent_gate(t)

if not api_key:
    st.info(t["api_missing"])
    st.stop()

try:
    freire = FreireIA(api_key=api_key)
except Exception as exc:
    st.error(f"Não foi possível iniciar a demo: {exc}")
    st.stop()

if "active_step_index" not in st.session_state:
    st.session_state["active_step_index"] = 0

step_cols = st.columns(3)
progress_values = [0.33, 0.66, 1.0]
for index, step in enumerate(t["steps"]):
    with step_cols[index]:
        button_type = "primary" if st.session_state["active_step_index"] == index else "secondary"
        if st.button(step, type=button_type, use_container_width=True):
            st.session_state["active_step_index"] = index
            st.rerun()

step_index = st.session_state["active_step_index"]
st.progress(progress_values[step_index])
st.caption(f"{t['steps'][step_index]} - {int(progress_values[step_index] * 100)}% {t['session']}")

if step_index == 0:
    st.subheader(t["step1_title"])
    st.write(t["step1_help"])
    guide_col, record_col = st.columns([1, 2])

    with guide_col:
        st.markdown(f"### {t['prepare']}")
        st.markdown(t["guide"])
        st.markdown(f"### {t['questions_title']}")
        for index, question in enumerate(t["questions"]):
            st.checkbox(question, key=f"listening_question_{idioma}_{index}")

    with record_col:
        st.markdown(f"### {t['record']}")
        contexto_educador = st.text_area(t["educator_noticed"], value=st.session_state.get("contexto_educador", ""), placeholder=t["educator_placeholder"], height=120)
        fala_aluno = st.text_area(t["learner_said"], value=st.session_state.get("fala_aluno", ""), placeholder=t["learner_placeholder"], height=120)

        st.markdown(f"### {t['noticed']}")
        observation_cols = st.columns(3)
        observacoes = []
        for index, observation in enumerate(t["observations"]):
            with observation_cols[index % 3]:
                if st.checkbox(observation, key=f"observation_{idioma}_{index}"):
                    observacoes.append(observation)

        st.markdown(f"### {t['themes']}")
        card_cols = st.columns(3)
        cartoes = []
        for index, card in enumerate(t["cards"]):
            with card_cols[index % 3]:
                if st.checkbox(card, key=f"life_card_{idioma}_{index}"):
                    cartoes.append(card)

        st.markdown(f"### {t['next_action']}")
        if st.button(t["suggest_words"], type="primary"):
            if not contexto_educador.strip() and not fala_aluno.strip() and not cartoes:
                st.warning(t["need_input"])
            else:
                st.session_state["contexto_educador"] = contexto_educador
                st.session_state["fala_aluno"] = fala_aluno
                with st.spinner(t["listening_spinner"]):
                    try:
                        response = freire.mediar_dialogo(contexto_educador, fala_aluno, observacoes, cartoes, idioma=idioma)
                        register_usage(response)
                        st.session_state["mediacao"] = extract_text(response)
                        st.rerun()
                    except Exception as exc:
                        show_generation_error(exc)

    if "mediacao" in st.session_state:
        st.markdown(f"### {t['suggestion']}")
        st.markdown(st.session_state["mediacao"])
        st.markdown(f"### {t['choose_word_title']}")
        st.write(t["choose_word_help"])
        palavra_sugerida = st.selectbox(t["quick_suggestions"], build_word_options(cartoes, idioma))
        palavra_livre = st.text_input(t["other_word"], placeholder=t["other_word_placeholder"])
        palavra_escolhida = (palavra_livre or palavra_sugerida).strip()
        if st.button(t["use_word"], type="primary"):
            st.session_state["palavra_geradora"] = palavra_escolhida
            st.session_state["active_step_index"] = 1
            st.rerun()

if step_index == 1:
    st.subheader(t["step2_title"])
    st.write(t["step2_help"])
    palavra = st.text_input(t["chosen_word"], value=st.session_state.get("palavra_geradora", ""), placeholder=t["chosen_word_placeholder"])
    contexto_para_exercicio = st.text_area(t["activity_context"], value=st.session_state.get("contexto_educador", ""), placeholder=t["activity_context_placeholder"], height=110)
    cena_visual = st.text_area(
        t["scene"],
        value=st.session_state.get("cena_visual", scene_suggestion(st.session_state.get("palavra_geradora", ""), contexto_para_exercicio, idioma)),
        placeholder=t["scene_placeholder"],
        height=90,
        help=t["scene_help"],
    )
    st.session_state["cena_visual"] = cena_visual
    st.markdown(f"### {t['next_action']}")
    if st.button(t["create_activity"], type="primary"):
        if not palavra.strip():
            st.warning(t["need_word"])
        else:
            st.session_state["palavra_geradora"] = palavra.strip()
            with st.spinner(t["activity_spinner"]):
                try:
                    response = freire.alfabetizar(palavra.strip(), contexto_para_exercicio, cena_visual, idioma=idioma)
                    register_usage(response)
                    st.session_state["exercicio"] = extract_text(response)
                    st.rerun()
                except Exception as exc:
                    show_generation_error(exc)
    if "exercicio" in st.session_state:
        st.markdown(f"### {t['activity']}")
        st.markdown(st.session_state["exercicio"])
        if st.button(t["go_record"], type="primary"):
            st.session_state["active_step_index"] = 2
            st.rerun()

if step_index == 2:
    st.subheader(t["step3_title"])
    st.write(t["step3_help"])
    conhece = st.checkbox(t["recognized"], key=f"conhece_{idioma}")
    escreve = st.checkbox(t["wrote"], key=f"escreve_{idioma}")
    fala = st.checkbox(t["related"], key=f"fala_{idioma}")
    frase = st.checkbox(t["sentence_help"], key=f"frase_{idioma}")
    st.progress(sum([conhece, escreve, fala, frase]) / 4)

    fala_significativa = st.text_area(t["meaningful_speech"], key=f"fala_significativa_{idioma}", placeholder=t["meaningful_placeholder"])
    situacao_limite = st.text_area(t["limit_situation"], key=f"situacao_limite_{idioma}", placeholder=t["limit_placeholder"])
    pergunta_aberta = st.text_area(t["open_question"], key=f"pergunta_aberta_{idioma}", placeholder=t["open_question_placeholder"])
    frase_aluno = st.text_area(t["learner_sentence"], key=f"frase_aluno_{idioma}", placeholder=t["learner_sentence_placeholder"])

    if sum([conhece, escreve, fala, frase]) == 4:
        st.success(t["success"])
    else:
        st.info(t["continue"])

    st.markdown(f"### {t['memory']}")
    st.write(t["memory_help"])
    if st.button(t["generate_memory"]):
        budget = get_float_env("GEMINI_BUDGET_BRL", 0)
        spent = st.session_state["usage_estimated_spent_brl"]
        st.session_state["relatorio"] = build_report(
            {
                "contexto_educador": st.session_state.get("contexto_educador", ""),
                "fala_aluno": st.session_state.get("fala_aluno", ""),
                "palavra_geradora": st.session_state.get("palavra_geradora", ""),
                "mediacao": st.session_state.get("mediacao", ""),
                "exercicio": st.session_state.get("exercicio", ""),
                "cena_visual": st.session_state.get("cena_visual", ""),
                "fala_significativa": fala_significativa,
                "situacao_limite": situacao_limite,
                "pergunta_aberta": pergunta_aberta,
                "conhece": conhece,
                "escreve": escreve,
                "fala": fala,
                "frase": frase,
                "frase_aluno": frase_aluno,
                "usage_input_tokens": f"{st.session_state['usage_input_tokens']:,}".replace(",", "."),
                "usage_output_tokens": f"{st.session_state['usage_output_tokens']:,}".replace(",", "."),
                "usage_total_tokens": f"{st.session_state['usage_total_tokens']:,}".replace(",", "."),
                "usage_estimated_spent_brl": format_brl(spent),
                "usage_estimated_remaining_brl": format_brl(max(budget - spent, 0) if budget > 0 else 0),
            },
            idioma,
        )
    if "relatorio" in st.session_state:
        st.markdown(st.session_state["relatorio"])
        st.download_button(t["download_memory"], data=st.session_state["relatorio"], file_name=report_file_name(idioma), mime="text/markdown")

render_feedback_section(t, idioma)
