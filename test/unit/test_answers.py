import pytest

from answers import Answers


@pytest.fixture
def answers():
    return Answers()


class TestAnswers:
    def test_get_and_capitalise_second_letter_of_string(self, answers):
        assert answers.get_and_capitalise_second_letter_of_string("test") == "E"

        assert answers.get_and_capitalise_second_letter_of_string("145434") == "4"

    def test_get_third_and_fourth_letters_of_string(self, answers):
        assert answers.get_third_and_fourth_letters_of_string("test") == "st"

        assert answers.get_third_and_fourth_letters_of_string("JNiUnfon") == "iU"
