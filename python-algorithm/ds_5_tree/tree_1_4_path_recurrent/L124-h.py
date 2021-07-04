# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -float("inf")
        self.transval(root)
        return self.res

    def transval(self, root):
        if not root:
            return 0

        lt_max = self.transval(root.left)
        rt_max = self.transval(root.right)

        self.res = max(self.res, root.val)
        self.res = max(self.res, lt_max + root.val + rt_max)
        self.res = max(self.res, lt_max + root.val)
        self.res = max(self.res, root.val + rt_max)

        # 如果2个子树中的路径最大值都小于0；就不要子树路径
        return max(0, max(lt_max, rt_max)) + root.val