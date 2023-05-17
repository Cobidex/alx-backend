#!/usr/bin/env python3
'''
contains the LRUCache class definition
'''
from base_caching import BaseCaching
from collections import OrderedDict, deque


class LRUCache(BaseCaching):
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
            if key in self.cache_data:
                del self.cache_data[key]
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            queue = deque(self.cache_data)
            disc_key = queue.popleft()
            del self.cache_data[disc_key]
            print(f"DISCARD: {disc_key}")

    def get(self, key):
        '''
        returns value linked to key
        '''
        if key and key in self.cache_data:
            item = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = item
        return self.cache_data.get(key)
