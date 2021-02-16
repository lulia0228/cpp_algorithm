# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s == None:
            return False
        if self.isEqual(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isEqual(self, r1, r2):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        if r1.val != r2.val:
            return False
        return self.isEqual(r1.left, r2.left) and self.isEqual(r1.right, r2.right)