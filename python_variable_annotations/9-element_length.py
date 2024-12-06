#!/usr/bin/env python3
"""
This module contains a function `element_length` that processes a list of
iterable elements and returns a list of tuples. Each tuple consists of the
original element and its corresponding length.

Functions:
    element_length(lst: List[Iterable]) -> List[Tuple[Iterable, int]]:
        Takes a list of iterable elements and returns a list of tuples, where
        each tuple contains an element from the input list and its length.

Example usage:
    element_length(['apple', 'banana', 'cherry'])
    # Returns: [('apple', 5), ('banana', 6), ('cherry', 6)]
"""
from typing import List, Iterable, Tuple


def element_length(lst: List[Iterable]) -> List[Tuple[Iterable, int]]:
    """
    Given a list of iterable elements, return a list of tuples where each tupl
    contains the element from the input list and its corresponding length.

    Args:
        lst (List[Iterable]): A list of iterable elements (e.g., strings, list

    Returns:
        List[Tuple[Iterable, int]]: A list of tuples, where each tuple contain
                                    an element from the input list and the
                                    length of that element (as an integer).
    
    Example:
        element_length(['apple', 'banana', 'cherry'])
        # Returns: [('apple', 5), ('banana', 6), ('cherry', 6)]
    """
    return [(i, len(i)) for i in lst]
