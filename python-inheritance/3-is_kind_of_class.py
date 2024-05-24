#!/usr/bin/python3
def factorial(n):
    """
    This function calculates the factorial of a given number.
    It uses a recursive approach to compute the factorial.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
