#!/usr/bin/env python3
'''
module contains the sever class and get_page method
it also contains a copy of the index_range function
'''


import csv
import math
from typing import List


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


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        returns the appropriate page of dataset
        '''
        assert type(page) == int and type(page_size) == int, 'args must be ints'
        assert page > 0 and page_size > 0, 'args must not be zero'
        indexes: tuple = index_range(page, page_size)

        if indexes[1] > len(self.dataset()):
            return []
        return self.dataset()[indexes[0]:indexes[1]]
