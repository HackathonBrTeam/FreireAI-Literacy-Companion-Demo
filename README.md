# FreireIA - Literacy Companion

FreireIA is a literacy companion built for the Gemma 4 Good Hackathon. The project explores how Paulo Freire's pedagogy can be combined with small, accessible AI models to support critical literacy, multilingual education, and community-based learning.

The demo focuses on a mediated learning flow involving three participants: the educator, the learner, and FreireIA. The solution does not replace the educator. It acts as an interlocutor and facilitator that helps listen to the learner, organize multimodal signals, suggest generative words, surface investigative questions and possible limit-situations, and transform the conversation into a critical literacy activity.

## Demo Goal

The hackathon version is designed to prove the concept quickly and clearly:

- Use Gemma 4 as the main pedagogical model for the final demo.
- Provide a simple Streamlit interface for educators and mentors.
- Show a mediated session between educator, learner, and FreireIA.
- Support Portuguese, Spanish, and English learning activities.
- Keep the pedagogical flow explicit: listening -> generative word -> investigative questions -> culture circle -> literacy activity -> Memory of the Culture Circle.
- Demonstrate social impact for adult literacy, community education, migrants, and low-resource learning contexts.

The demo is configured to use Gemma 4 through Google AI Studio. Gemini can remain a development fallback, but the hackathon path should keep Gemma 4 as the core generation model.

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
GEMINI_MODEL=gemma-4-26b-a4b-it
GEMINI_MAX_OUTPUT_TOKENS=700
GEMINI_BUDGET_BRL=10.00
GEMINI_INPUT_BRL_PER_1M_TOKENS=0.40
GEMINI_OUTPUT_BRL_PER_1M_TOKENS=1.75
```

The `.env` file is intentionally ignored by Git. Do not commit API keys.

The budget and token-rate fields are used only by the Streamlit demo to estimate local session consumption. The real balance must still be checked in Google Billing.

For Streamlit Community Cloud, configure these same values in the app secrets instead of using `.env`. Use `.streamlit/secrets.toml.example` as the reference format.

Run the demo:

```powershell
streamlit run frontend\streamlit_app.py
```

Open:

```text
http://localhost:8501
```

## Invite-Based Validation

To publish the demo for invited educators or interested reviewers:

1. Push the repository to GitHub without `.env`.
2. Create the app in Streamlit Community Cloud.
3. Use `frontend/streamlit_app.py` as the main file path.
4. Keep the app private while testing with invited users.
5. Configure the app secrets with the values from `.streamlit/secrets.toml.example`.
6. Add a `FEEDBACK_FORM_URL` pointing to a Google Forms, Microsoft Forms, Typeform, or similar survey.
7. Invite users by email through the Streamlit sharing settings.

The app includes a consent screen for invited validation. It reminds testers to use fictional examples or minimal data and avoid sensitive learner information. Feedback can be sent through the configured external form, or generated as a Markdown file during live testing.

Suggested external feedback questions:

- What was your role during the test?
- At what moment did FreireIA help the most?
- At what moment did the interface feel confusing?
- Would this support a real literacy session?
- What should change before testing with real learners?

## Version Plan

### Version 0 - Hackathon Demo

Purpose: create a compelling, low-friction demo for judges.

Planned characteristics:

- Streamlit interface.
- Gemma 4 as the primary model path.
- `gemma-4-26b-a4b-it` as the default demo model through Google AI Studio.
- Gemini fallback only for development or emergency demo recovery.
- Mediated interaction with educator notes, learner speech/text, observed signals, and visual/touch cards.
- Checklist-style listening prompts and observation cards to reduce reading friction during the session.
- Visual progress indicator across the three educator-facing steps.
- AI-assisted suggestion of generative words.
- AI-assisted investigative questions and possible limit-situations.
- Culture-circle activity with visual codification suggestions.
- Literacy activity by language.
- Narrative learning record with learner voice, open question, and observed evidence.
- Downloadable `Memoria do Circulo de Cultura` in Markdown.

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
   |-- Gemma 4 through Google AI Studio
   |-- Gemma 4 local or cloud runtime
   |-- Vertex AI endpoint
   `-- Gemini fallback
```

This keeps the pedagogy independent from any single API. For the hackathon, Gemma 4 should be the main path because it is part of the prize premise. For product evolution, the provider layer allows cost, privacy, and performance trade-offs.

## Pedagogical Flow

1. Investigation: collect the learner's vocabulary universe.
2. Mediation: combine educator notes, learner expression, observed signals, and touch/image choices.
3. Generative word: select a word connected to the learner's lived reality.
4. Investigative questions: turn the learner's context into questions instead of fixed definitions.
5. Limit-situations: identify possible constraints or contradictions to investigate further.
6. Visual codification: suggest an image, scene, or object to support critical dialogue.
7. Literacy exercise: decompose the word into syllables or phonetic units.
8. Critical sentence: the learner applies the word in a meaningful phrase.
9. Memory of the Culture Circle: the educator records learner voice, evidence, open questions, and next steps.

## Cost Direction

For the demo, the recommended direction is a local or short-lived cloud GPU runtime for Gemma 4, activated only during testing and presentation. This keeps costs controlled while satisfying the hackathon premise.

For Gemini fallback testing, keep a small monthly budget in Google Cloud, create alerts, and cap model output with `GEMINI_MAX_OUTPUT_TOKENS`.

The Streamlit interface shows an estimated usage panel with input tokens, output tokens, total tokens, estimated amount used, and estimated remaining balance. This panel is based on token metadata returned by the API and the local `.env` budget/rate values; it is not a live billing statement.

For a future product, the best path is to support multiple deployment modes:

- Community mode: local or shared low-cost Gemma runtime.
- SaaS mode: hosted model endpoint with usage controls.
- Institutional mode: deployment for schools, NGOs, foundations, or public literacy programs.

## Security Notes

- Never commit `.env`.
- Rotate API keys that were exposed in screenshots or shared channels.
- Keep learner data minimal during the demo.
- Add explicit consent and data-retention controls before real pilots.
