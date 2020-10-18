# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 17:56
# @Author  : No Name

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归不停的拆分左右子树
class Solution:
    dic = {}
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        sz = len(preorder)
        for i in range(sz):
            self.dic[inorder[i]] = i
        return self.myBuildTree(preorder, inorder, 0, sz-1, 0, sz-1)

    def myBuildTree(self, preorder, inorder, p_lt, p_rt, i_lt, i_rt):
        # 递归终止条件
        if p_lt > p_rt:
            return None
        # 找到当前根节点在两个遍历中的索引
        p_root = p_lt
        i_root = self.dic[preorder[p_root]]
        # 创建当前根节点
        root = TreeNode(preorder[p_root])
        # 左子树中节点数目
        num_lt = i_root-i_lt
        # 递归建树
        root.left = self.myBuildTree(preorder, inorder, p_lt+1, p_lt+num_lt, i_lt, i_root-1)
        root.right = self.myBuildTree(preorder, inorder, p_lt+num_lt+1, p_rt, i_root+1, i_rt)
        return root