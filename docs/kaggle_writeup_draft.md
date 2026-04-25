# FreireAI Literacy Companion

## Subtitle

A multi-agent Gemma-powered literacy companion inspired by Paulo Freire.

## Summary

FreireAI Literacy Companion is a multilingual literacy application that helps learners build reading and writing skills from words that matter in their own lives. Instead of starting from generic vocabulary, the app first asks about the learner's community, routine and interests. A multi-agent architecture then identifies a meaningful generative word, breaks it into syllables, creates syllabic families and guides the learner through discovery activities.

## Why it matters

Literacy is not only a technical skill. It is a path to autonomy, participation and dignity. Inspired by Paulo Freire's method, this project treats the learner's lived experience as the starting point for education.

## How Gemma is used

Gemma is positioned as the reasoning layer behind the agents that understand context, choose pedagogically meaningful words, generate activities and explain why each lesson was created.

## Architecture

The app uses six agents:
- Context Agent
- Generative Word Agent
- Linguistic Agent
- Pedagogical Agent
- Multimodal Agent
- Safety & Trust Agent

## Impact

The project targets adult literacy, migrant education, multilingual inclusion and low-connectivity learning scenarios.

## Technical execution

The MVP is implemented as a modular Streamlit app with a replaceable AI gateway. It can run with deterministic mock responses for demo reliability or connect to a local Gemma-compatible model through Ollama.
