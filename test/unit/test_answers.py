import pytest

import random
from datetime import datetime
from string import ascii_uppercase, ascii_lowercase

from quiz import Answers


@pytest.fixture
def answers():
    return Answers()

@pytest.fixture
def random_params():
    class RandomParams:
        def __init__(self):
            self.magnitude = 10
            """
            The above atribute is an arbitrary value which determines how big and varied method outputs are.
            It should not be set to less than 5
            """

        @property
        def letter_list(self):
            return self._get_letter_list()

        @property
        def upper_letter_list(self):
            return self._get_letter_list(upper=True, lower=False)

        @property
        def lower_letter_list(self):
            return self._get_letter_list(upper=False, lower=True)

        @property
        def int_list(self):
            return [random.randrange(-self.magnitude, self.magnitude) for i in range(self.magnitude)]

        @property
        def even_int_list(self):
            is_magnitude_odd = self.magnitude % 2 != 0

            return [
                random.randrange(-self.magnitude + is_magnitude_odd, self.magnitude + is_magnitude_odd, 2)
                for i in range(self.magnitude)
            ]

        @property
        def odd_int_list(self):
            is_magnitude_even = self.magnitude % 2 == 0

            return [
                random.randrange(-self.magnitude + is_magnitude_even, self.magnitude + is_magnitude_even, 2)
                for i in range(self.magnitude)
            ]

        @property
        def bool_list(self):
            source = (True, False)

            return [random.choice((True, False)) for i in range(self.magnitude)]

        def _get_letter_list(self, upper=True, lower=True):
            source = ""
            result = []

            if upper:
                source += ascii_uppercase
                # This will ensure that at least one char is upper if uppercase letters are included
                result.append(random.choice(ascii_uppercase))
            if lower:
                source += ascii_lowercase
                # Same here for lowercase letters
                result.append(random.choice(ascii_lowercase))

            chars_needed = self.magnitude - (upper + lower)
            return result + [random.choice(source) for i in range(chars_needed)]

    return RandomParams()


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

    def test_is_all_uppercase(self, answers, random_params):
        assert answers.is_all_uppercase("".join(random_params.upper_letter_list))
        assert not answers.is_all_uppercase("".join(random_params.lower_letter_list))
        assert not answers.is_all_uppercase("".join(random_params.letter_list))

    def test_both_numbers_are_even(self, answers, random_params):
        even_ints = random_params.even_int_list
        odd_ints = random_params.odd_int_list

        with open("log.txt", "w") as f:
            f.write(str(even_ints[:2]))
        assert answers.both_numbers_are_even(*even_ints[:2])
        assert not answers.both_numbers_are_even(*odd_ints[:2])

        assert not answers.both_numbers_are_even(even_ints[2], odd_ints[2])
        assert not answers.both_numbers_are_even(odd_ints[3], even_ints[3])

    def test_only_one_number_is_even(self, answers, random_params):
        even_ints = random_params.even_int_list
        odd_ints = random_params.odd_int_list

        assert not answers.only_one_number_is_even(*even_ints[:2])
        assert not answers.only_one_number_is_even(*odd_ints[:2])

        assert answers.only_one_number_is_even(even_ints[2], odd_ints[2])
        assert answers.only_one_number_is_even(odd_ints[3], even_ints[3])

    def test_make_function_that_returns_object_type(self, answers, random_params):
        generated_func = answers.make_function_that_returns_object_type()

        # Commented out the below check because if someone figures out they can do this, they deserve a pass
        # assert generated_func is not type

        params = [
            *random_params.int_list[:3],
            *random_params.letter_list[:3],
            *random_params.bool_list[:3],
            Exception, KeyError, ValueError,
            lambda: None, lambda: True, lambda: False, lambda: "", lambda: 0
        ]
        random.shuffle(params)

        for obj in params:
            assert generated_func(obj) == type(obj)

    def test_count_matching_list_items(self, answers, random_params):
        for i in range(10):
            target_list = random_params.letter_list
            value_to_match = random.choice(target_list)
            match_count = random.randint(1, 10)

            target_list = list(filter(lambda obj: obj is not value_to_match, target_list))
            target_list += [value_to_match] * match_count

            assert answers.count_matching_list_items(target_list, value_to_match) == match_count

    def test_are_all_keys_in_dict(self, answers, random_params):
        letters = random_params.letter_list

        list_of_keys = random_params.int_list
        target_dict = {k: random.choice(letters) for k in list_of_keys}

        assert answers.are_all_keys_in_dict(list_of_keys, target_dict)

        list_of_keys = random_params.int_list
        target_dict = {k: random.choice(letters) for k in list_of_keys}
        del target_dict[random.choice(list_of_keys)]

        assert not answers.are_all_keys_in_dict(list_of_keys, target_dict)

        list_of_keys = random_params.int_list
        target_dict = {}

        assert not answers.are_all_keys_in_dict(list_of_keys, target_dict)
