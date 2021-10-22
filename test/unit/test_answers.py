import pytest

import random
from datetime import datetime
from string import ascii_uppercase, ascii_lowercase

from quiz import Answers


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

    def test_string_length_in_a_sentence(self, answers):
        assert answers.string_length_in_a_sentence("eeaa") == "Your string is 4 characters long!"

        assert answers.string_length_in_a_sentence("new_length") == "Your string is 10 characters long!"

    def test_get_minutes_from_datetime(self, answers):
        now = datetime.now()

        assert answers.get_minutes_from_datetime(now) == now.minute

    # From this point on, parameters passed to Answer methods should be dynamically generated
    # to prevent hard-coding the method return values using `if` statements

    def test_is_all_uppercase(self, answers):
        all_upper_string = "".join([random.choice(ascii_uppercase) for i in range(random.randint(1, 11))])
        all_lower_string = "".join([random.choice(ascii_lowercase) for i in range(random.randint(1, 11))])

        mixed_string = ""
        mixed_string += "".join([random.choice(ascii_uppercase) for i in range(random.randint(1, 5))])
        mixed_string += "".join([random.choice(ascii_lowercase) for i in range(random.randint(1, 5))])
        mixed_string = list(mixed_string)
        random.shuffle(mixed_string)
        mixed_string = "".join(char for char in mixed_string)

        assert answers.is_all_uppercase(all_upper_string)
        assert not answers.is_all_uppercase(all_lower_string)
        assert not answers.is_all_uppercase(mixed_string)

    def test_both_numbers_are_even(self, answers):
        even_numbers = [random.randrange(-100, 100, 2), random.randrange(-100, 100, 2)]
        odd_numbers = [random.randrange(-99, 101, 2), random.randrange(-99, 101, 2)]

        assert answers.both_numbers_are_even(*even_numbers)
        assert not answers.both_numbers_are_even(*odd_numbers)

        assert not answers.both_numbers_are_even(even_numbers[0], odd_numbers[0])
        assert not answers.both_numbers_are_even(odd_numbers[0], even_numbers[0])
