# -*- coding: utf-8 -*-

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        stk = []
        pre, idx, min_abs = 0, 0, float("inf")
        while stk != [] or root != None:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop(-1)
            idx += 1
            if idx == 1: # 遍历第一个值时候不处理
                pass
            else:
                min_abs = min(min_abs, abs(root.val-pre))
            pre = root.val
            root = root.right
        return min_abs