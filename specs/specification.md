# Spec: FreireIA - Consciência Multilíngue
## 1. Visão Geral
Sistema de alfabetização baseado na pedagogia de Paulo Freire, utilizando o modelo Gemma 4. A solução é centrada no usuário, que provê sua própria infraestrutura de IA (Bring Your Own Key/Auth).

## 2. Requisitos Funcionais
- **Módulo de Investigação:** O agente deve coletar o "universo vocabular" do aluno.
- **Círculo de Cultura Digital:** Geração de debates críticos sobre temas sociais antes da codificação silábica.
- **Multilinguismo:** Suporte nativo para PT-BR, ES e EN.
- **Delegação de Custos:** Integração via SDK do Google AI / Vertex AI onde o usuário autentica sua conta.

## 3. Arquitetura de Agentes (SDD)
- **Investigator Agent:** Identifica palavras geradoras através de diálogo.
- **Educational Architect:** Planeja a sequência didática (Sílaba -> Palavra -> Frase -> Mundo).
- **Voice Validator:** Utiliza capacidades multimodais do Gemma 4 para validar pronúncia.

## 4. Definição de Pronto (Definition of Done)
- O aluno deve ser capaz de identificar e escrever a palavra geradora e aplicá-la em uma frase crítica.
