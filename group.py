"""
created by Nagaj at 29/05/2021
"""
from core import BaseMixin


class Group(BaseMixin):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.members = self.objs

    def __str__(self):
        return self.name
