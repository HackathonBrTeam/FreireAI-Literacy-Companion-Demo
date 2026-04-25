from app.agents.linguistic_agent import LinguisticAgent


def test_build_lesson_for_jogo():
    agent = LinguisticAgent()
    lesson = agent.build_lesson("jogo", "Português")

    assert lesson["word"] == "jogo"
    assert lesson["syllables"] == ["JO", "GO"]
    assert "JO" in lesson["syllabic_family"]
