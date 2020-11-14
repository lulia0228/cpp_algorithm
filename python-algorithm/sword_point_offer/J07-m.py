# -*- coding: utf-8 -*-

# 7 由前序和中序遍历复原二叉树  和leetcode105一样

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        sz = len(preorder)
        record = {}
        for i in range(sz):
            record[inorder[i]] = i
        return self.myBuild(preorder, inorder, 0, sz - 1, 0, sz - 1, record)

    def myBuild(self, preorder, inorder, p_lt, p_rt, i_lt, i_rt, record):
        if p_lt > p_rt:
            return None
        # 当前根节点在前序列表中的索引
        p_root = p_lt
        # 找到根节点在中序列表中的索引
        i_root = record[preorder[p_root]]
        root = TreeNode(preorder[p_root])
        # 左子树节点数目
        num_lt = i_root - i_lt
        root.left = self.myBuild(preorder, inorder, p_lt + 1, p_lt + num_lt, i_lt, i_root - 1, record)
        root.right = self.myBuild(preorder, inorder, p_lt + num_lt + 1, p_rt, i_root + 1, i_rt, record)

        return root




