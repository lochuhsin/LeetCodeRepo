import random
"""
This is my first solution, however the operation getRandom
Runs in linear time(converting keys to arr)
"""


class RandomizedSet:

    def __init__(self):
        self.dic = {}

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False

        self.dic[val] = None
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False

        del self.dic[val]
        return True

    def getRandom(self) -> int:
        val = list(self.dic.keys())
        return random.choice(val)

"""
using technique, arr + hashtable
The key point is at the remove function
move the element in list to the last
and change the index position in dictionary
"""
from random import choice


class RandomizedSet():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            # move the last element to the place idx of the element to delete
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            # delete the last element
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)