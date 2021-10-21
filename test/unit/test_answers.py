import pytest

from answers import Answers


@pytest.fixture
def answers():
    return Answers()


class TestAnswers:
    def test_get_and_capitalise_second_letter_of_string(self, answers):
        assert answers.get_and_capitalise_second_letter_of_string("test") == "E"
