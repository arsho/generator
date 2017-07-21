# -*- coding: utf-8 -*-
def generate(length = 0):
    """
    Generates a strong password. The length can be defined by user.

    The password is a combination of uppercase letters, lowercase letters,
    numbers and symbols. If the length is not defined by user then it will
    generate minimum 8 length password.

    :param length: int. Optional argument of the password length.
    :return: string. Returns the generated password of user defined length if given.
    :raise valueError: Raises an exception if the length is not integer number
    """
    return "password"

def strength(password):
    """
    Returns the strength of a string as a password in range 0-100.

    :param password: string. Mandatory argument.
    :return: float. The strength of the password between 0-100.
    :raise valueError: Raises an exception if the argument is not defined.
    """

    return 0.8