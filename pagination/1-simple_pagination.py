#!/usr/bin/env python3
"""
Module that gets names from a csv file when given page and page size
"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    res = ((page - 1) * page_size, page * page_size)
    return res

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Gets page
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start_row, end_row = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_row:end_row]
