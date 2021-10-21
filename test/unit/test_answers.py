import pytest

from answers import Answers


@pytest.fixture
def answers():
    return Answers()


class TestAnswers:
    def test_example_question(self, answers):
        assert answers.example_question() == "example answer"

    def test_example_question_add_2(self, answers):
        assert answers.example_question_add_2(3) == 5

        assert answers.example_question_add_2(-1) == 1

    def test_add_new_string_to_string(self, answers):
        assert answers.add_new_string_to_string("is") == "isnew"

        assert answers.add_new_string_to_string("is not ") == "is not new"

    def test_multiply_numbers(self, answers):
        assert answers.multiply_numbers(5, 4) == 20

        assert answers.multiply_numbers(3, 6) == 18

    def test_get_and_capitalise_second_letter_of_string(self, answers):
        assert answers.get_and_capitalise_second_letter_of_string("test") == "E"

        assert answers.get_and_capitalise_second_letter_of_string("145434") == "4"

    def test_get_third_and_fourth_letters_of_string(self, answers):
        assert answers.get_third_and_fourth_letters_of_string("test") == "st"

        assert answers.get_third_and_fourth_letters_of_string("JNiUnfon") == "iU"
