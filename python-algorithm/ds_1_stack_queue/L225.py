# -*- coding: utf-8 -*-


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que1 = []
        self.que2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # 新元素从que2进，通过交换使得每次输入新的元素后
        # 所有元素在que1中按照顺序倒排，que2清空
        self.que2.append(x)
        while self.que1 != []:
            self.que2.append(self.que1.pop(0))
        tmp_que = self.que1 # 此时que1已经是空队列
        self.que1 = self.que2
        self.que2 = tmp_que

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.que1.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.que1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.que1 == []

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()