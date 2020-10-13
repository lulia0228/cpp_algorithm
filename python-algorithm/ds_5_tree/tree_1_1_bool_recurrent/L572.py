#--coding:utf-8--
'''
@Time   : 2020/10/13
@Author : No Name
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s == None :
            return False
        # 判断当前节点作为根节点的2棵树是否相等
        if self.equal_tree(s,t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def equal_tree(self, r1, r2):
        if r1 == None and r2 == None:
            return True
        if r1 == None or r2 == None:
            return False
        if r1.val != r2.val:
            return False
        return self.equal_tree(r1.left, r2.left) and self.equal_tree(r1.right, r2.right)
