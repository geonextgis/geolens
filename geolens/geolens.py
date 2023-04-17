"""Main module."""

import string
import random

def generate_random_password(length=10, upper=False, digits=False, punctuation=False):
    """Generates a random password of a given length.

    Args:
        length (int, optional): The length of the string to generate. Defaults to 10.
        upper (bool, optional): Whether to include uppercase letters. Defaults to False.
        digits (bool, optional): Whether to include digits. Defaults to False.
        punctuation (bool, optional): Whether to include punctuation. Defaults to False.

    Returns:
        str: The generated password.
    """
    letters = string.ascii_lowercase
    if upper:
        letters += string.ascii_uppercase
    if digits:
        letters += string.digits
    if punctuation:
        letters += string.punctuation
    password = "".join(random.choice(letters) for i in range(length))
    return password


def generate_lucky_number(length=1):
    """Generates a random number of given length.

    Args:
        length (int, optional): The length of the number to generate. Defaults to 1.

    Returns:
        int: The generated number.
    """
    digit = string.digits
    lucky_number = "".join(random.choice(digit) for i in range(length))
    return int(lucky_number)
