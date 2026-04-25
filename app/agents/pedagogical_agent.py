"""Agente pedagógico adaptativo."""

import unicodedata


class PedagogicalAgent:
    """Avalia respostas e devolve feedback simples e acolhedor."""

    def evaluate_answer(self, answer: str, expected_word: str) -> dict:
        """Compara resposta do aluno com a palavra esperada."""
        clean_answer = self._normalize(answer)
        clean_expected = self._normalize(expected_word)

        if clean_answer == clean_expected:
            return {
                "correct": True,
                "message": "Muito bem! Você reconheceu e formou a palavra corretamente.",
                "next_difficulty": "normal",
            }

        return {
            "correct": False,
            "message": "Quase lá. Tente observar as sílabas e montar a palavra novamente.",
            "next_difficulty": "review",
        }

    def _normalize(self, value: str) -> str:
        """Remove acentos e padroniza texto para comparação."""
        value = value.strip().lower()
        value = unicodedata.normalize("NFKD", value)
        return "".join(char for char in value if not unicodedata.combining(char))
