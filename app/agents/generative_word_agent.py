"""Agente que escolhe a palavra geradora."""

from app.services.ai_gateway import AIGateway


class GenerativeWordAgent:
    """Seleciona uma palavra significativa e pedagogicamente útil."""

    def __init__(self, ai_gateway: AIGateway) -> None:
        self.ai_gateway = ai_gateway

    def select_word(self, context: dict, target_language: str) -> dict:
        """Escolhe palavra geradora com base no contexto do aluno."""
        themes = context.get("themes", [])

        priority = ["jogo", "casa", "trabalho", "bola", "feira", "família", "ônibus"]
        chosen = next((word for word in priority if word in themes), themes[0] if themes else "casa")

        return {
            "word": chosen,
            "language": target_language,
            "reason": (
                f"Escolhi '{chosen}' porque aparece no contexto do aluno e pode gerar "
                "atividades com sílabas, imagens, fala e novas palavras."
            ),
        }
