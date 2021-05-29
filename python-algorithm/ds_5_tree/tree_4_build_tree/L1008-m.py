# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        def my_build(pre, ino, p_lt, p_rt, i_lt, i_rt):
            if p_lt > p_rt:
                return None
            root_pre = p_lt
            root_ino = record[pre[root_pre]]
            root = TreeNode(pre[root_pre])
            n_left = root_ino - i_lt
            root.left = my_build(pre, ino, p_lt + 1, p_lt + n_left, i_lt, root_ino - 1)
            root.right = my_build(pre, ino, p_lt + n_left + 1, p_rt, root_ino + 1, i_rt)
            return root

        inorder = sorted(preorder)
        record = {}
        for i in range(len(inorder)):
            record[inorder[i]] = i

        return my_build(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)