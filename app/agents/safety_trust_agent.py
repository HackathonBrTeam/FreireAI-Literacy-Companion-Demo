"""Agente de segurança, confiança e explicabilidade."""


class SafetyTrustAgent:
    """Valida se a palavra é adequada para o contexto educacional."""

    BLOCKED_WORDS = {
        "violência",
        "arma",
        "droga",
        "ódio",
    }

    def validate_word(self, word_payload: dict) -> dict:
        """Valida a palavra geradora antes de exibir ao aluno."""
        word = word_payload.get("word", "").lower().strip()

        if not word:
            return {
                "is_safe": False,
                "message": "Não foi possível selecionar uma palavra geradora segura.",
            }

        if word in self.BLOCKED_WORDS:
            return {
                "is_safe": False,
                "message": "A palavra selecionada não é adequada para esta atividade.",
            }

        return {
            "is_safe": True,
            "message": "Palavra aprovada para uso pedagógico.",
        }
