#!/usr/bin/env python3
"""Task 0 - Basic dictionary"""
BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that inherits from BaseCaching.
    It has no limit on the number of items it can store.
    """
    def put(self, key, item):
        """
        Assign the item value to the key in the cache_data dictionary.
        Do nothing if key or item is None.
        """
        if key is not None or item is  not None:
            self.cache_data[key] = item
    def get(self, key):
        """
        Return the value in cache_data linked to key.
        Return None if key is None or doesn't exist.
        """
        if key is None:
            return
        return self.cache_data.get(key)
