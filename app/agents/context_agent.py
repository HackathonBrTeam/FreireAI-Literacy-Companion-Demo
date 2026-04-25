"""Agente responsável por entender o contexto do estudante."""

from app.services.ai_gateway import AIGateway


class ContextAgent:
    """Extrai temas significativos da fala inicial do aluno."""

    def __init__(self, ai_gateway: AIGateway) -> None:
        self.ai_gateway = ai_gateway

    def extract_context(self, learner_answer: str) -> dict:
        """Transforma a resposta do aluno em temas de interesse."""
        normalized_answer = learner_answer.strip()

        if not normalized_answer:
            normalized_answer = "gosto de casa, família, jogo e trabalho"

        themes = []
        for candidate in ["casa", "família", "jogo", "trabalho", "ônibus", "feira", "bola"]:
            if candidate in normalized_answer.lower():
                themes.append(candidate)

        if not themes:
            themes = ["casa", "jogo", "trabalho"]

        return {
            "raw_answer": normalized_answer,
            "themes": themes,
        }
