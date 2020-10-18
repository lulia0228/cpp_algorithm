# -*- coding: utf-8 -*-


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return res
        stk = []
        idx = 0
        while stk!= [] or root != None:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop(-1)
            idx += 1
            if idx == k:
                return root.val
            root = root.right