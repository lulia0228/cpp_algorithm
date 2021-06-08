#--coding:utf-8--
#
# return a array which include all ans for op3
# @param op int整型二维数组 operator
# @return int整型一维数组
#

class Solution:
    def __init__(self):
        self.stk = []
        self.min_stk = []

    def getMinStack(self, op):
        # write code here
        res = []
        for p in op:
            if p[0] == 1:
                self.stk.append(p[1])
                if not self.min_stk:
                    self.min_stk.append(p[1])
                else:
                    self.min_stk.append(min(self.min_stk[-1], p[1]))
            elif p[0] == 2:
                self.stk.pop(-1)
                self.min_stk.pop(-1)
            elif p[0] == 3:
                res.append(self.min_stk[-1])

        return res