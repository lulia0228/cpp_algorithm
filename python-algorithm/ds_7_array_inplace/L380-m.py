# -*- coding: utf-8 -*-
# @Time    : 2020/10/4 20:05
# @Author  : No Name

class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.a = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.d:
            return False
        self.d[val] = len(self.a)
        self.a.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.d:
            return False
        # 在数组中 把要删除的值和最后一个交换
        self.a[self.d[val]] = self.a[-1]
        self.d[self.a[-1]] = self.d[val]
        self.a.pop(-1)
        self.d.pop(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randint(0, len(self.a) - 1)
        return self.a[idx]

        # Your RandomizedSet object will be instantiated and called as such:
        # obj = RandomizedSet()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()