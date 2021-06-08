#--coding:utf-8--

class Solution:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def push(self, node):
        # write code here
        self.stk1.append(node)

    def pop(self):
        # return xx
        if not self.stk1 and not self.stk2:
            return None
        if not self.stk2:
            while self.stk1:
                self.stk2.append(self.stk1.pop(-1))
        return self.stk2.pop(-1)
