# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None: return 0
        lt = self.maxDepth(root.left)
        rt = self.maxDepth(root.right)
        return max(lt, rt)+1