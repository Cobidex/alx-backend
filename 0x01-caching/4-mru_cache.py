#!/usr/bin/env python3
'''
contains the MRUCache class definition
'''
from base_caching import BaseCaching
from collections import OrderedDict, deque


class MRUCache(BaseCaching):
    '''
    uses the LRU caching system
    '''
    def __init__(self):
        '''
        defines the class
        '''
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)

    def put(self, key, item):
        '''
        assigns a value to dict key
        '''
        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    queue = deque(self.cache_data)
                    disc_key = queue.pop()
                    del self.cache_data[disc_key]
                    print(f"DISCARD: {disc_key}")

            if key in self.cache_data:
                del self.cache_data[key]
            self.cache_data[key] = item

    def get(self, key):
        '''
        returns value linked to key
        '''
        if key and key in self.cache_data:
            item = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = item
        return self.cache_data.get(key)
