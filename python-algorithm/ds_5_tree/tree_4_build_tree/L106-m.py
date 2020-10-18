# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 18:15
# @Author  : No Name

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    dic = {}
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        sz = len(postorder)
        for i in range(sz):
            self.dic[inorder[i]] = i
        return self.myBuildTree(postorder, inorder, 0, sz-1, 0, sz-1)

    def myBuildTree(self, postorder, inorder, p_lt, p_rt, i_lt, i_rt):
        # 递归终止条件
        if p_lt > p_rt:
            return None
        # 找到当前根节点在两个遍历中的索引
        p_root = p_rt
        i_root = self.dic[postorder[p_root]]
        # 创建当前根节点
        root = TreeNode(postorder[p_root])
        # 左子树中节点数目
        num_lt = i_root-i_lt
        # 递归建树
        root.left = self.myBuildTree(postorder, inorder, p_lt, p_lt+num_lt-1, i_lt, i_root-1) # 都是取闭区间值
        root.right = self.myBuildTree(postorder, inorder, p_lt+num_lt, p_rt-1, i_root+1, i_rt)
        return root