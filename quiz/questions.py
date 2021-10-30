from abc import ABC


class Questions(ABC):
    """
    Each of the functions below (the individual sections that start with `def` and end with `return NotImplemented`)
    should be copied and pasted at the bottom of the answers file.
    To answer the question once it is has been copied there, replace `NotImplemented` with the value that the question
    is looking for. Any code that is needed to create that value can be written in the space directly above the
    `return` line, and if multiple lines are needed it is fine to add more lines in that space
    """

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

        return NotImplemented

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
        This function should receive a string, and return the following string:
        "Your string is X characters long!", replacing X with the length of the input string
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
    - `If`, `elif` and `else` statements
    - `and`, `or` and `not` statements
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

        return NotImplemented

    def only_one_number_is_even(self, number_1, number_2):
        """
        This function should receive two numbers, and return a boolean indicating
        whether only one of them is even
        """

        return NotImplemented

    # 3.1. Pyglatin
    """
    New concepts covered:
    - Index slicing
    - str.isalpha()
    """

    # 4. Functions
    """
    New concepts covered:
    - Creating a function
    - type()
    """

    def make_function_that_returns_object_type(self):
        """
        This function should return another new function.
        The new function should have one parameter, which will receive an object,
        and should return the type of that object
        """

        return NotImplemented

    # 4.1 Taking a Vacation
    """
    New concepts covered:
    - 
    """

    # 5. Lists and Dictionaries
    """
    New concepts covered:
    - Lists
    - Dictionaries
    - Indexing for lists & dictionaries
    - Index slicing
    - `for` loops
    - Mutability
    """

    def count_matching_list_items(self, target_list, value_to_match):
        """
        This function should receive a list and another variable, and return how many times the value
        of that variable can be found in the list.
        For example, if target_list is ["k", "e", "k", "w"] and value_to_match is "k", this function should return 2
        """

        return NotImplemented

    def are_all_keys_in_dict(self, list_of_keys, target_dict):
        """
        This function should receive a list and a dictionary. For each item in the list, the function should check if
        that item exists as a key in the dictionary. If all items in the list are also keys in the dictionary,
        the function should return True. However, if any item in the list is missing from the dictionary,
        the function should return False.

        The typical way to solve this question uses the `in` keyword. If you are not familiar with this keyword,
        return to this question once you have learned how to use it
        """

        return NotImplemented

    # 5.1. A Day at the Supermarket
    """
    New concepts covered:
    - 
    """

    # 6. Student Becomes the Teacher
    """
    New concepts covered:
    - 
    """

    # 7. Lists and Functions
    """
    New concepts covered:
    - 
    """

    # 7.1. Battleship!
    """
    New concepts covered:
    - 
    """

    # 8. Loops
    """
    New concepts covered:
    - `while` loops
    - `break` statements
    """

    def get_final_value(self, target_function):
        """
        This function should receive a target function, and should call the target function repeatedly until
        it returns a value that is not `None`. Once a value that is not `None` has been returned, this
        function should also return that value
        """

        return NotImplemented
