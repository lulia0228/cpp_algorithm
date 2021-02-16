# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not self.isAttened(root):
            return None
        if self.isAttened(root.left):
            self.pruneTree(root.left)
        else:
            root.left = None
        if self.isAttened(root.right):
            self.pruneTree(root.right)
        else:
            root.right = None
        return root

    def isAttened(self, root):
        stk = []
        while stk or root:
            while root:
                # if root.val == 1:
                #     return True
                stk.append(root)
                root = root.left
            root = stk.pop(-1)
            if root.val == 1:
                return True
            root = root.right
        return False

# 更标准的解法（就是前序遍历）
class Solution1:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if not root.left and not root.right and root.val == 0:
            return None

        return root