#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        return a dictionary of containing page info
        even if database is altered
        """
        dataset: list = []
        idx_data: Dict[int, List] = self.indexed_dataset()
        keys: list = list(idx_data.keys())
        assert index + page_size < len(keys), 'out of range'
        assert index < len(keys)

        if index not in idx_data:
            start_idx = keys[index]
        else:
            start_idx = index

        end_idx: int = start_idx + page_size

        for i in range(start_idx, end_idx):
            if i not in idx_data:
                dataset.append(idx_data[keys[i]])
            else:
                dataset.append(idx_data[i])

        next_idx: int = index + page_size

        if index not in keys:
            next_idx = keys[next_idx]

        return {
                "index": index,
                "next_index": next_idx,
                "page_size": len(dataset),
                "data": dataset
                }
