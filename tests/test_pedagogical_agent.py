from app.agents.pedagogical_agent import PedagogicalAgent


def test_evaluate_correct_answer():
    agent = PedagogicalAgent()
    result = agent.evaluate_answer("JOGO", "jogo")

    assert result["correct"] is True


def test_evaluate_wrong_answer():
    agent = PedagogicalAgent()
    result = agent.evaluate_answer("casa", "jogo")

    assert result["correct"] is False
