# -*- coding: utf-8 -*-
# @Time    : 2020/10/2 9:07
# @Author  : Heng Li
# @File    : L155.py
# @Software: PyCharm

# 这里是为了用list仿c++等语言的stack功能，所以不要使用python list的其它特性

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr1 = []
        # 额外维护一个栈记录当前最小值
        self.arr2 = []

    def push(self, x: int) -> None:
        self.arr1.append(x)
        if self.arr2 == []:
            self.arr2.append(x)
        else:
            if self.arr2[-1] <= x:
                self.arr2.append(self.arr2[-1])
            else:
                self.arr2.append(x)

    def pop(self) -> None:
        self.arr1.pop(-1)
        self.arr2.pop(-1)

    def top(self) -> int:
        return self.arr1[-1]

    def getMin(self) -> int:
        return self.arr2[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()