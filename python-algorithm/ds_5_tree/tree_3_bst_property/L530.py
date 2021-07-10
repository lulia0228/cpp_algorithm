# -*- coding: utf-8 -*-

# 同783
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ans = float("inf")
        pre = None
        stk = []
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            if pre:
                ans = min(ans, abs(root.val-pre.val))
            pre = root
            root = root.right
        return ans