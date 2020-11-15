# -*- coding: utf-8 -*-

class CQueue:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def appendTail(self, value: int) -> None:
        self.stk1.append(value)

    def deleteHead(self) -> int:
        if not self.stk1 and not self.stk2:
            return -1
        if not self.stk2:
            while self.stk1:
                self.stk2.append(self.stk1.pop(-1))
        return self.stk2.pop(-1)

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()