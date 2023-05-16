#!/usr/bin/env python3
'''
contains the LIFOCache class definition
'''
from base_caching import BaseCaching
stack = []


class LIFOCache(BaseCaching):
    '''
    uses the FIFO caching system
    '''
    def __init__(self):
        '''
        defines the class
        '''
        super().__init__()

    def put(self, key, item):
        '''
        assigns a value to dict key
        '''
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                disc_key = stack.pop()
                del self.cache_data[disc_key]
                print(f"DISCARD: {disc_key}")
            stack.append(key)

    def get(self, key):
        '''
        returns value linked to key
        '''
        return self.cache_data.get(key)
