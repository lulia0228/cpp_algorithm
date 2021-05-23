# -*- coding: utf-8 -*-
# 深度优先遍历即可

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 先序遍历，记录下最大值和最小值
class Solution:
    maxvalue = 0

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.dfs(root, 0, 100001)
        return self.maxvalue

    def dfs(self, node, maxv, minv):
        if not node:
            self.maxvalue = max(maxv - minv, self.maxvalue)
        else:
            maxv, minv = max(maxv, node.val), min(minv, node.val)
            self.dfs(node.left, maxv, minv)
            self.dfs(node.right, maxv, minv)