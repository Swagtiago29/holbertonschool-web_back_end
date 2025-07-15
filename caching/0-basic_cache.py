#!/usr/bin/python3
from base_catching import BaseCaching
"""Task 0 - Basic dictionary"""

class BasicCache(BaseCaching):
    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item
    def get(self, key):
        if self.cache_data is None or key is None:
            return None
        return self.cache_data[key]