#!/usr/bin/env python3
"""lru_cache.py"""
BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRU (Least Recently Used)
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        if key is None or item is None: 
            return None
        if key not in self.cache_data and len(self.cache_data) >= self.MAX_ITEMS:
            first_item = next(iter(self.cache_data))
            self.cache_data.pop(first_item)
            print(f"DISCARD: {first_item}")

        self.cache_data[key] = item
        self.cache_data.move_to_end(key)
    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
