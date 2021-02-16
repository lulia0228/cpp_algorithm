# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    flag = True
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root):
            if root == None: return 0
            lt = depth(root.left)
            rt = depth(root.right)
            if abs(lt - rt) > 1:
                self.flag = False
            return max(lt, rt) + 1
        depth(root)
        return self.flag


