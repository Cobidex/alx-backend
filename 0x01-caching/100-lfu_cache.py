#!/usr/bin/env python3
'''
contains the LFUCache class
'''
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''
    implementation of the LFU class
    '''
    def __init__(self):
        '''
        initializes the instance with methods and fields from the baeclass
        '''
        super().__init__()
        self.__tracker = {}

    def put(self, key, item):
        '''
        sets an element in the cache
        '''
        if key and item:
            if key in self.__tracker:
                self.__tracker[key] += 1
            else:
                self.__tracker[key] = 0
                self.cache_data[key] = item

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                disc_key = min(self.__tracker, key=self.__tracker.get)
                self.__tracker.pop(disc_key, None)
                self.cache_data.pop(disc_key, None)
                print(f"DISCARD: {disc_key}")

    def get(self, key):
        '''
        retrieves a key value
        '''
        if key:
            if key in self.__tracker:
                self.__tracker[key] += 1
        return self.cache_data.get(key)
