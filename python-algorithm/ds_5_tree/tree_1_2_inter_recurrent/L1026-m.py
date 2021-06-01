# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxvalue = 0

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.dfs(root, 0, 10e5)
        return self.maxvalue

    def dfs(self, node, maxv, minv):
        if not node:
            self.maxvalue = max(maxv - minv, self.maxvalue)
        else:
            maxv, minv = max(maxv, node.val), min(minv, node.val)
            self.dfs(node.left, maxv, minv)
            self.dfs(node.right, maxv, minv)