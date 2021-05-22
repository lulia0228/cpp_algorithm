#--coding:utf-8--
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        pre = None
        min_sub = float("inf")
        stk = []
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            if pre:
                min_sub = min(min_sub, root.val-pre.val)
            pre = root
            root = root.right
        return min_sub