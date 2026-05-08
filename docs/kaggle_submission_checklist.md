# Kaggle Submission Checklist

Use this checklist before submitting FreireIA to the Gemma 4 Good Hackathon.

## Required Assets

- Kaggle writeup with problem, solution, architecture, impact, and limitations.
- Short video pitch showing the problem, the live workflow, and why Gemma 4 matters.
- Public code repository with setup instructions and no committed secrets.
- Live demo URL, preferably private during validation and public/accessible for judging.
- Media gallery with screenshots of the three-step workflow and generated memory record.

## Judging Alignment

### Impact and Vision

- State the specific problem: adult literacy educators need help turning real conversations into critical literacy activities without replacing their pedagogical role.
- Name the primary user: educator or mentor working in adult literacy, EJA, migrant education, or community learning.
- Show the social-good path: better listening, contextual generative words, learner voice preserved, and lower preparation friction.
- Include safety boundaries: no sensitive learner data in the demo, consent gate, educator remains responsible for decisions.

### Video Pitch and Storytelling

- Open with a realistic educator scenario.
- Show the full loop: listening notes -> generative words -> activity -> memory of the Culture Circle.
- Keep the model call visible through generated suggestions, not as a generic chatbot.
- Close with what a pilot would measure: educator usefulness, clarity, learner relevance, and privacy readiness.

### Technical Depth and Execution

- Explain that FreireIA uses Gemma 4 through Google AI Studio for the hackathon demo.
- Highlight multilingual support for PT-BR, ES, and EN.
- Mention session usage tracking, configurable model settings, Streamlit secrets support, and downloadable learning records.
- Be transparent about current scope: this is a proof of concept, not a production student-record system.

## Final Repository Check

- `.env` and `.streamlit/secrets.toml` are not committed.
- `.streamlit/secrets.toml.example` contains placeholders only.
- README setup works from a fresh environment.
- `docs/test_plan.md` has been used at least once with the deployed demo.
- Screenshots and demo URL match the current UI.
