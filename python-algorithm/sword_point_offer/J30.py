#--coding:utf-8--

# 最小值栈 同leetcode155

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk1 = []
        self.stk2 = []

    def push(self, x: int) -> None:
        self.stk1.append(x)
        if self.stk2 == []:
            self.stk2.append(x)
        elif self.stk2[-1] < x:
            self.stk2.append(self.stk2[-1])
        else:
            self.stk2.append(x)

    def pop(self) -> None:
        self.stk1.pop(-1)
        self.stk2.pop(-1)

    def top(self) -> int:
        return self.stk1[-1]

    def min(self) -> int:
        return self.stk2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()