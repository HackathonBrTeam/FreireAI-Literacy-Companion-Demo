"""Agente linguístico para sílabas e famílias silábicas."""

from app.data.syllable_rules import SYLLABLE_DATABASE


class LinguisticAgent:
    """Gera estrutura linguística simples para a palavra selecionada."""

    def build_lesson(self, word: str, target_language: str) -> dict:
        """Cria uma mini lição com sílabas, família silábica e exemplos."""
        normalized_word = word.lower().strip()
        data = SYLLABLE_DATABASE.get(normalized_word)

        if data is None:
            data = {
                "syllables": [normalized_word],
                "syllabic_family": [normalized_word],
                "examples": [normalized_word],
            }

        return {
            "word": normalized_word,
            "language": target_language,
            "syllables": data["syllables"],
            "syllabic_family": data["syllabic_family"],
            "examples": data["examples"],
        }
