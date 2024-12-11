#!/usr/bin/env python3
"""
    Calculate the start and end indices for a given page and page size.

    This function takes in a page number and a page size, and computes
    the indices that correspond to the start and end positions of the
    items for that page in a paginated list.

    Args:
    page (int): The page number (1-based index).
    page_size (int): The number of items per page.

    Returns:
    Tuple[int, int]: A tuple containing two integers:
        - The starting index of the items on the given page.
        - The ending index (exclusive) of the items on the given page.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    calculates the start and end indices
    """
    res = ((page - 1) * page_size, page * page_size)
    return res
