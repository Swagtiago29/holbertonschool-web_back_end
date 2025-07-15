#!/usr/bin/python3
from base_catching import BaseCaching

class FIFOCache(BaseCaching):
    def __init__(self):
        self.MAX_ITEMS = BaseCaching.MAX_ITEMS
        super().__init__()
    def put(self, key, item):
        if key is None or item is None:
            pass
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            for keys in self.cache_data:
                first_item = keys
                break
            self.cache_data.pop(first_item, None)
            print(f"DISCARD: {first_item}" )