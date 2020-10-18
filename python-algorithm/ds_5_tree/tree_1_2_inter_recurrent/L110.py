#--coding:utf-8--


# 110 判断平衡二叉树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    flag = True
    def isBalanced(self, root: TreeNode) -> bool:
        self.defy(root)
        return self.flag

    def defy(self, root):
        if root == None:
            return 0
        l_h = self.defy(root.left)
        r_h = self.defy(root.right)
        if abs(l_h-r_h)>1:
            self.flag = False
        return max(l_h, r_h)+1



