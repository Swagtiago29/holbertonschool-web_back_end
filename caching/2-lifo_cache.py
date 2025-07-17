#!/usr/bin/env python3
"""Task 1 - FIFO caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO (Last-In, First-Out) Cache implementation"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache.
        If the cache is full, discard the last item put in (LIFO).
        """
        if key is None or item is None:
            return

        if key not in self.cache_data and \
                len(self.cache_data) >= self.MAX_ITEMS:
            last_item = next(reversed(self.cache_data))
            self.cache_data.pop(last_item)
            print(f"DISCARD: {last_item}")

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item by key.
        """
        return self.cache_data.get(key, None)
