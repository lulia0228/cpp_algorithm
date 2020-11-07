# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if not root.left:
                root = root.right
            else:
                # 找左子树最右边的节点
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right
                # 将原来的右子树接到左子树的最右边节点
                tmp.right = root.right
                # 将原来的左子树插入到原来的右子树的地方
                root.right = root.left
                root.left = None
                root = root.right
