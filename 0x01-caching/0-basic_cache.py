#!/usr/bin/env python3
'''
contains the BasicCache class
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    a caching system implementation
    '''
    def __init__(self):
        '''
        initialize instance from baseclass
        '''
        super().__init__()

    def put(self, key, item):
        '''
        assign value to dict
        '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''
        returns assigned key value
        '''
        return self.cache_data.get(key)
