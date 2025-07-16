#!/usr/bin/python3
"""Task 1 - FIFO caching"""
BaseCaching = __import__('base_caching').BaseCaching

class LIFOCache(BaseCaching):
    """LIFO (Last-In, First-Out) Cache implementation"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        if key in self.cache_data:
             self.cache_data[key] = item
             return
        if len(self.cache_data) >= self.MAX_ITEMS:
            last_item = next(reversed(self.cache_data))
            self.cache_data.pop(last_item, None)
            print(f"DISCARD: {last_item}" )

        self.cache_data[key] = item

    def get(self, key):
        if key is None:
            return None
        return self.cache_data.get(key)
