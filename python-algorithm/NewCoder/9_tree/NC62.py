# -*- coding: utf-8 -*-

class Solution:
    flag = True
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot: return True
        self.cal_depth(pRoot)
        return self.flag

    def cal_depth(self, root):
        if not root: return 0
        lt_depth = self.cal_depth(root.left)
        rt_depth = self.cal_depth(root.right)
        if abs(lt_depth - rt_depth) > 1:
            self.flag = False
        return max(lt_depth, rt_depth) + 1