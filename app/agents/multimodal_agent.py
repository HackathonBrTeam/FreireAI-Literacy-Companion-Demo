"""Agente multimodal para preparar recursos de texto, imagem e áudio."""


class MultimodalAgent:
    """Prepara sugestões de recursos multimodais para a lição."""

    def build_assets(self, word: str) -> dict:
        """Retorna metadados que podem ser usados pela interface."""
        return {
            "word": word,
            "image_prompt": f"Ilustração simples e educativa da palavra {word}",
            "audio_text": f"Vamos ler juntos: {word}",
        }
