#!/usr/bin/env python3
'''
module to contain the index_range function
'''


def index_range(page: int, page_size: int) -> tuple:
    '''
    index_range - calculates the range of indexes for a particular paination

    args:
        @page: integer representing page number
        @page_size: integer representing number of items per page

    return: a tupple of the range of indexes to return
    '''
    upper_index: int = page_size * page
    lower_index: int = upper_index - page_size

    return (lower_index, upper_index)
