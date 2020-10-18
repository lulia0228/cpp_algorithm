#--coding:utf-8--


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.cal_path(root)
        return self.res

    def cal_path(self, root):
        if root == None:
            return 0
        l_path = self.cal_path(root.left)
        r_path = self.cal_path(root.right)
        if root.left and root.left.val == root.val:
            l_num = l_path+1
        else:
            l_num = 0
        if root.right and root.right.val == root.val:
            r_num = r_path+1
        else:
            r_num = 0
        self.res = max(self.res, l_num+r_num)
        return max(l_num, r_num)

