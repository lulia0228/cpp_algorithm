# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    flag = True
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root):
            if root == None:
                return 0
            lt = depth(root.left)
            rt = depth(root.right)
            if abs(lt-rt)>1:
                self.flag = False
            return max(lt, rt)+1
        depth(root)
        return self.flag
