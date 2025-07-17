#!/usr/bin/env python3
"""mru_cache.py"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRU (Most Recently Used)
    """
    def __init__(self):
        """Initialize the cache with an empty OrderedDict."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache.
        """
        if key is None or item is None:
            return None
        if key not in self.cache_data and \
                len(self.cache_data) >= self.MAX_ITEMS:
            first_item = next(reversed(self.cache_data))
            self.cache_data.pop(first_item)
            print(f"DISCARD: {first_item}")

        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """
        Retrieve an item by key.
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
