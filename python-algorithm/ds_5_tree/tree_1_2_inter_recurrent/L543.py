#--coding:utf-8--

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = -float("inf")
        self.transval(root)
        return self.res

    def transval(self, root):
        if not root: return 0
        lt_max = self.transval(root.left)
        rt_max = self.transval(root.right)
        self.res = max(self.res, lt_max+rt_max)
        return max(lt_max, rt_max)+1