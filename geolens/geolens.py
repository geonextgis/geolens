"""Main module."""

import string
import random

def generate_random_password(length=10, upper=False, digits=False, punctuation=False):
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
    digit = string.digits
    lucky_number = "".join(random.choice(digit) for i in range(length))
    return int(lucky_number)
