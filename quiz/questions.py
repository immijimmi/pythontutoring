from abc import ABC


class Questions(ABC):

    # Example questions #

    def example_question(self):
        """
        This function should return the string "example answer"
        """

        return NotImplemented

    def example_question_add_2(self, number):
        """
        This function should receive a number, and return the provided number with 2 added to it
        """

    # Course Questions #
    """
    These questions are structured around the Python 2 course on codecademy
    """

    # 1. Python Syntax
    """
    New concepts covered:
    - Variables
    - Basic data types
    - String concatenation
    - Arithmetic
    - Debugging errors
    """

    def add_new_string_to_string(self, string):
        """
        This function should receive a string, and
        return that string with the string 'new' joined to the end
        """

        return NotImplemented

    def multiply_numbers(self, number_1, number_2):
        """
        This function should receive two numbers, and return
        the multiple of those numbers
        """

        return NotImplemented

    # 2. Strings and Console Output
    """
    New concepts covered:
    - String indexing
    - String methods
    - Converting non-string data to strings
    - String formatting
    """

    def get_and_capitalise_second_letter_of_string(self, string):
        """
        This function should receive a string at least 2 characters long,
        and return the capital of the second character
        """

        return NotImplemented

    def get_third_and_fourth_letters_of_string(self, string):
        """
        This function should receive a string at least 4 characters long,
        and return the third and fourth characters joined together.

        The simplest solution to this problem uses indexing in a way that has not been
        covered by this point in the codecademy course
        """

        return NotImplemented

    def string_length_in_a_sentence(self, string):
        """
        This function should receive a string, and print the sentence:
        "Your string is X characters long!", replacing X with the length of the string
        """

        return NotImplemented

    # 2.1. Date and Time
    """
    New concepts covered:
    - Datetime data type
    - Formatting datetimes
    - Getting the current date and time
    """

    def get_minutes_from_datetime(self, datetime_value):
        """
        This function should receive a datetime, and return just the minutes
        """

        return NotImplemented

    # 3. Conditionals and Control Flow
    """
    New concepts covered:
    - Comparison operators
    - If, elif and else statements
    - and, or and not statements
    - Truthiness
    """

    def is_all_uppercase(self, string):
        """
        This function should receive a string of letters, and return a boolean (True or False) indicating
        if all the letters in the string are uppercase
        """

        return NotImplemented

    def both_numbers_are_even(self, number_1, number_2):
        """
        This function should receive two numbers, and return a boolean indicating
        whether they are both even numbers (have a remainder of 0 when divided by 2)
        """

        raise NotImplemented