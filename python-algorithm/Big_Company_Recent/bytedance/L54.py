# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 逆中序遍历
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        cnt = 0
        stk = []
        while root or stk:
            while root:
                stk.append(root)
                root = root.right
            root = stk.pop(-1)
            cnt += 1
            if cnt == k:
                return root.val
            root = root.left



