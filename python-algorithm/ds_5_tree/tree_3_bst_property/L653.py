# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 16:50
# @Author  : No Name

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        s = []
        stk = []
        while stk != [] or root != None :
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop(-1)
            if k-root.val in s:
                return True
            s.append(root.val)
            root = root.right
        return False