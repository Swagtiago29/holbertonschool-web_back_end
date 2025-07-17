#!/usr/bin/python3
"""Task 1 - FIFO caching"""
BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that implements FIFO (First-In, First-Out) eviction.
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache.
        If the cache is full, discard the first item put in (FIFO).
        """
        if key is None or item is None:
            return
        
        if key not in self.cache_data and len(self.cache_data) >= self.MAX_ITEMS:
            for keys in self.cache_data:
                first_item = keys
                break
            self.cache_data.pop(first_item)
            print(f"DISCARD: {first_item}" )

        self.cache_data[key] = item

    def get(self, key):
        return self.cache_data.get(key, None)