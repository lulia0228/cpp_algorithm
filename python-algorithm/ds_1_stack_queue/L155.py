# -*- coding: utf-8 -*-

# 这里是为了用list仿c++等语言的stack功能，所以不要使用python list的其它特性

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.min_stk:
            self.min_stk.append(val)
        else:
            if val >= self.min_stk[-1]:
                self.min_stk.append(self.min_stk[-1])
            else:
                self.min_stk.append(val)

    def pop(self) -> None:
        self.min_stk.pop()
        return self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()