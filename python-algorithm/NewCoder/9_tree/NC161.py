# -*- coding: utf-8 -*-

class Solution:
    def inorderTraversal(self , root ):
        # write code here
        if not root: return []
        stk = []
        res = []
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            res.append(root.val)
            root = root.right
        return res