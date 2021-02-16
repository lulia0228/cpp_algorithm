# -*- coding: utf-8 -*-
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        count = len(preorder)
        r_dic = {}
        for i in range(count):
            r_dic[inorder[i]] = i
        return self.my_build(preorder, inorder, 0, count-1, 0, count-1, r_dic)

    def my_build(self, pre, ino, p_lt, p_rt, i_lt, i_rt, r_dic):
        if p_lt > p_rt: return None
        root = TreeNode(pre[p_lt])
        inorder_idx_order = r_dic[pre[p_lt]]
        nums_of_left = inorder_idx_order-i_lt
        root.left = self.my_build(pre, ino, p_lt+1, p_lt+nums_of_left, i_lt, inorder_idx_order-1, r_dic)
        root.right = self.my_build(pre, ino, p_lt+nums_of_left+1, p_rt, inorder_idx_order+1, i_rt, r_dic)
        return root

