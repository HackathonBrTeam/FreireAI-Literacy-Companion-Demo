"""Gateway simples para alternar entre mock e Ollama."""

import os
from typing import Any

import requests
from dotenv import load_dotenv


load_dotenv()


class AIGateway:
    """Centraliza chamadas de IA para facilitar troca entre mock, Ollama ou API futura."""

    def __init__(self) -> None:
        self.provider = os.getenv("AI_PROVIDER", "mock").lower()
        self.ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.ollama_model = os.getenv("OLLAMA_MODEL", "gemma3:4b")

    def generate(self, prompt: str) -> str:
        """Gera resposta textual a partir do provedor configurado."""
        if self.provider == "ollama":
            return self._generate_ollama(prompt)

        return self._generate_mock(prompt)

    def _generate_mock(self, prompt: str) -> str:
        """Resposta determinística para demo sem dependência externa."""
        prompt_lower = prompt.lower()

        if "palavra geradora" in prompt_lower:
            return "jogo"

        return "Resposta simulada para o MVP."

    def _generate_ollama(self, prompt: str) -> str:
        """Executa chamada local ao Ollama."""
        payload: dict[str, Any] = {
            "model": self.ollama_model,
            "prompt": prompt,
            "stream": False,
        }

        response = requests.post(
            f"{self.ollama_base_url}/api/generate",
            json=payload,
            timeout=60,
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()
