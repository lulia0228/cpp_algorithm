#--coding:utf-8--

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 == None : return False
        if self.checkSubTree(t1.left, t2):
            return True
        if self.checkSubTree(t1.right, t2):
            return True
        return self.IsSame(t1, t2)

    def IsSame(self, t1, t2):
        if t1 == None and t2 == None:
            return True
        if t1 == None or t2 == None:
            return False
        if t1.val != t2.val:
            return False
        return self.IsSame(t1.left, t2.left) and self.IsSame(t1.right, t2.right)
