# -*- coding: utf-8 -*-
class Solution:
    def maxDepth(self , root ):
        # write code here
        if not root: return 0
        lt_depth = self.maxDepth(root.left)
        rt_depth = self.maxDepth(root.right)
        return max(lt_depth, rt_depth) + 1