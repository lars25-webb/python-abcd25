"""
This file contains the functions you shall implement to solve the lab.
Implement them one by one and check if they pass all tests.

Execute the lab using `python3 lab.py` in the terminal and review the output.
"""


def hello():
    """
    Returns the string "Hello world".

    Returns:
        str: "Hello world".
    """
    return"Hello world"


def magic_number():
    """
    Returns the integer value 42.

    Returns:
        int: The integer value 42.
    """
    return 42


def float_str(string_number):
    """
    Returns the float number of the incoming string.

    Arguments:
        number (str): The number to cast to float.

    Returns:
        float: The float number.
    """
    return float(string_number)


def string_length(word):
    """
    Returns the length of the incoming string.

    Arguments:
        word (str): The string to use.

    Returns:
        int: The length of the string.
    """
    return len(word)


def round_pi(pi):
    """
    Returns the value of PI, rounded to three decimals.

    Arguments:
        pi (float): The value of PI to round.
    Returns:
        float: The value of PI, rounded to three decimals.
    """
    return round(pi, 3)


def concat_strings(word1, word2):
    """
    Returns a concatenated string of the incoming strings, with a space between the words.

    Arguments:
        word1 (str): The first string to use.
        word2 (str): The second string to use.

    Returns:
        str: The concatenated string.
    """
    return word1 + " " + word2

def char_at_position(word):
    """
    Returns the character at index 4 of the incoming string.
    Hint: String indexing starts at 0.

    Arguments:
        word (str): The string to use.

    Returns:
        str: The character at index 4 in the incoming string.
    """
    return word[4]


def divide_string_number():
    """
    Assign the following values to variables. String '30' and integer 5.
    Convert the string to an integer and divide it by the integer.
    Round the result to the nearest integer and return it.
    Hint: int() and round()

    Returns:
        int: The rounded result of int('30') / 5.
    """
    result = round(int('30') / 5)
    return result


def even_or_odd(n):
    """
    Determines whether the given integer is even or odd.

    Arguments:
        n (int): The integer to check.

    Returns:
        str: "Even" if `n` is divisible by 2, otherwise "Odd".
    """
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


def password_check(password):
    """
    Checks the length of the given password string.

    Arguments:
        password (str): The password to check.

    Returns:
        str: "Too short" if the password length is less than 5, otherwise "OK".
    """
    if len(password) < 5:  # noqa: PLR2004
        return "Too short"
    else:
        return "OK"
