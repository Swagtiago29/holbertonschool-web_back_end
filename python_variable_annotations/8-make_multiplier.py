#!/usr/bin/env python3
from typing import Callable

"""
This module provides a function for creating multiplier functions.

It includes the function `make_multiplier`, which takes a float `multiplier`
as an argument and returns a new function that multiplies its input by this
multiplier. The resulting function can be used to perform the multiplication
on different values.

The module demonstrates the use of higher-order functions in Python, where
a function returns another function. The returned function "remembers" the
`multiplier` value it was created with and applies it when called.

Example usage:
    multiply_by_3 = make_multiplier(3.0)
    result = multiply_by_3(4.0)  # result will be 12.0
    multiply_by_5 = make_multilpier(5.0)
    result2 = multiply_by_5(4.0)  # result2 will be 20.0

This module is useful for creating custom multiplier functions dynamically
based on a given multiplier value.
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a given number by a specified
    multiplier.

    Args:
        multiplier (float): The multiplier value that will be used to multiply
                             the input value.

    Returns:
        Callable[[float], float]: A function that takes a float as input and
                                  returns the product of the input and the
                                  multiplier.
    """
    def multi(x: float) -> float:
        """
        Multiplies the input value by the multiplier.

        Args:
            x (float): The value to be multiplied.

        Returns:
            float: The result of multiplying the input value by the multiplier.
        """
        return x * multiplier

    return multi
