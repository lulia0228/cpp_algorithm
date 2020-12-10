# -*- coding: utf-8 -*-

# 7 由前序和中序遍历复原二叉树  和leetcode105一样

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    record = {}

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        for i in range(len(inorder)):
            self.record[inorder[i]] = i
        return self.my_build(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)

    def my_build(self, pre, ino, p_lt, p_rt, i_lt, i_rt):
        if p_lt > p_rt:
            return None
        # 当前根节点在前序列表中的索引
        root_pre = p_lt
        # 找到根节点在中序列表中的索引
        root_ino = self.record[pre[root_pre]]
        root = TreeNode(pre[root_pre])
        # 左子树节点数目
        n_left = root_ino - i_lt
        root.left = self.my_build(pre, ino, p_lt + 1, p_lt + n_left, i_lt, root_ino - 1)
        root.right = self.my_build(pre, ino, p_lt + n_left + 1, p_rt, root_ino + 1, i_rt)
        return root



