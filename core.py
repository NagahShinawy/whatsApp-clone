"""
created by Nagaj at 29/05/2021
"""

from abc import ABC


class BaseMixin(ABC):

    def __init__(self):
        self.objs = []

    def __len__(self):
        return len(self.objs)

    def __getitem__(self, item):
        return self.objs[item]

    def __contains__(self, item):
        return item in self.objs
