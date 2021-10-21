from abc import ABC


class Questions(ABC):
    def get_and_capitalise_second_letter_of_string(self, string):
        """
        This function should receive a string at least 2 characters long,
        and return the capital of the second character
        """

        return NotImplemented

    def get_third_and_fourth_letters_of_string(self, string):
        """
        This function should receive a string at least 4 characters long,
        and return the third and fourth characters joined together
        """

        return NotImplemented

    def add_new_string_to_string(self, string):
        """
        This function should receive a string, and
        return that string with the string 'new' joined to the end
        """

        return NotImplemented
