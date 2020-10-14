#--coding:utf-8--
'''
@Time   : 2020/10/14
@Author : No Name
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    res = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.cal_depth(root)
        return self.res

    def cal_depth(self, root):
        if root == None:
            return 0
        l_h = self.cal_depth(root.left)
        r_h = self.cal_depth(root.right)
        self.res = max(self.res, l_h+r_h)
        return max(l_h, r_h)+1