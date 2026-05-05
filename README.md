# FreireIA - Literacy Companion

FreireIA is a literacy companion built for the Gemma 4 Good Hackathon. The project explores how Paulo Freire's pedagogy can be combined with small, accessible AI models to support critical literacy, multilingual education, and community-based learning.

The demo focuses on a mediated learning flow involving three participants: the educator, the learner, and FreireIA. The solution does not replace the educator. It acts as an interlocutor and facilitator that helps listen to the learner, organize multimodal signals, suggest generative words, and transform the conversation into a critical literacy activity.

## Demo Goal

The hackathon version is designed to prove the concept quickly and clearly:

- Use Gemma 4 as the main pedagogical model for the final demo.
- Provide a simple Streamlit interface for educators and mentors.
- Show a mediated session between educator, learner, and FreireIA.
- Support Portuguese, Spanish, and English learning activities.
- Keep the pedagogical flow explicit: investigation -> generative word -> culture circle -> literacy exercise -> learning evidence.
- Demonstrate social impact for adult literacy, community education, migrants, and low-resource learning contexts.

During early development, the app can use Gemini as a fallback model while the Gemma 4 runtime is prepared. For the hackathon submission, the core generation path should run on Gemma 4.

## Current Architecture

```text
.
|-- main.py                  # Core FreireIA logic and model call
|-- frontend/
|   `-- streamlit_app.py     # Streamlit demo interface
|-- specs/
|   `-- specification.md     # Product and agent requirements
|-- docs/
|   `-- Documentation.pdf    # Supporting documentation
|-- requirements.txt
|-- .env.example
`-- README.md
```

## Setup

Create and activate a Python environment, then install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Create a local `.env` file from `.env.example`:

```env
GEMINI_API_KEY=your_google_ai_studio_key_here
GEMINI_MODEL=gemini-2.5-flash-lite
GEMINI_MAX_OUTPUT_TOKENS=700
```

The `.env` file is intentionally ignored by Git. Do not commit API keys.

Run the demo:

```powershell
streamlit run frontend\streamlit_app.py
```

Open:

```text
http://localhost:8501
```

## Version Plan

### Version 0 - Hackathon Demo

Purpose: create a compelling, low-friction demo for judges.

Planned characteristics:

- Streamlit interface.
- Gemma 4 as the primary model path.
- Gemini fallback only for development or emergency demo recovery.
- Mediated interaction with educator notes, learner speech/text, observed signals, and visual/touch cards.
- AI-assisted suggestion of generative words.
- Generated culture-circle discussion.
- Generated literacy activity by language.
- Checklist for the definition of done: identify the word, write the word, explain its meaning, and apply it in a critical sentence.
- Visible model/runtime information in the app.

### Version 1 - Pilot With Educators

Purpose: test the tool with real educators, NGOs, EJA programs, and community learning groups.

Planned characteristics:

- Class/session management.
- Saved learning activities.
- Reusable generative-word history.
- Teacher notes and learner progress tracking.
- Better multilingual prompts for PT-BR, ES, and EN.
- Offline or low-connectivity deployment option.
- Privacy-first data handling.

### Version 2 - Product

Purpose: evolve from demo to deployable literacy platform.

Planned characteristics:

- Model provider abstraction: local Gemma, hosted Gemma, Vertex AI, or fallback APIs.
- Multi-tenant accounts for schools, NGOs, and public programs.
- Role-based access for educators, coordinators, and learners.
- Analytics for learning progress without exposing sensitive learner data.
- Voice validation module for pronunciation practice.
- Content safety and educator review controls.
- Deployment options for SaaS, institutional hosting, or community/offline mode.

## Model Strategy

The preferred production architecture is model-provider based:

```text
Frontend
   |
FreireIA pedagogical core
   |
Model provider
   |-- Gemma 4 local or cloud runtime
   |-- Vertex AI endpoint
   `-- Gemini fallback
```

This keeps the pedagogy independent from any single API. For the hackathon, Gemma 4 should be the main path because it is part of the prize premise. For product evolution, the provider layer allows cost, privacy, and performance trade-offs.

## Pedagogical Flow

1. Investigation: collect the learner's vocabulary universe.
2. Mediation: combine educator notes, learner expression, observed signals, and touch/image choices.
3. Generative word: select a word connected to the learner's lived reality.
4. Culture circle: discuss the social meaning of the word before technical literacy work.
5. Literacy exercise: decompose the word into syllables or phonetic units.
6. Critical sentence: the learner applies the word in a meaningful phrase.
7. Evidence: the educator checks whether the learning objective was achieved.

## Cost Direction

For the demo, the recommended direction is a local or short-lived cloud GPU runtime for Gemma 4, activated only during testing and presentation. This keeps costs controlled while satisfying the hackathon premise.

For Gemini fallback testing, keep a small monthly budget in Google Cloud, create alerts, and cap model output with `GEMINI_MAX_OUTPUT_TOKENS`.

For a future product, the best path is to support multiple deployment modes:

- Community mode: local or shared low-cost Gemma runtime.
- SaaS mode: hosted model endpoint with usage controls.
- Institutional mode: deployment for schools, NGOs, foundations, or public literacy programs.

## Security Notes

- Never commit `.env`.
- Rotate API keys that were exposed in screenshots or shared channels.
- Keep learner data minimal during the demo.
- Add explicit consent and data-retention controls before real pilots.
