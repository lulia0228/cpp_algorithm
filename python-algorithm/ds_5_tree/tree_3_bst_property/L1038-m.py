# -*- coding: utf-8 -*-

# 同538
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sum_ = 0
        stk = []
        nd = root
        while stk!=[] or root!=None:
            while root!=None:
                stk.append(root)
                root = root.right
            root = stk.pop()
            tmp =  root.val
            root.val += sum_
            sum_ += tmp
            root = root.left
        return nd