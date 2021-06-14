# -*- coding: utf-8 -*-

class Solution:
    def isContains(self, root1, root2):
        # write code here
        if not root1: return False
        if self.ifSame(root1, root2):
            return True
        flag1 = self.isContains(root1.left, root2)
        flag2 = self.isContains(root1.right, root2)
        return flag1 or flag2

    def ifSame(self, r1, r2):
        if not r1 and not r2: return True
        if not r1 or not r2: return False
        if r1.val != r2.val: return False
        return self.ifSame(r1.left, r2.left) and self.ifSame(r1.right, r2.right)