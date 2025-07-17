#!/usr/bin/env python3
"""Task 0 - Basic dictionary"""
BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that inherits from BaseCaching.

    This cache has no limit on the number of items it can store.
    """

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key: The key under which to store the item.
            item: The item to store.

        Does nothing if either key or item is None.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item by key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key, or None if key is None or not found.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
