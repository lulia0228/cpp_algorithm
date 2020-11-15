# -*- coding: utf-8 -*-

# 同leetcode 226 判断树是对称的

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isSym(root, root)

    def isSym(self, A, B):
        if A == None and B == None:
            return True
        if A == None or B == None:
            return False
        if A.val != B.val:
            return False
        return self.isSym(A.left, B.right) and self.isSym(A.right, B.left)