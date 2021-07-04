# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归不停的拆分左右子树
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_root_idxs = {}
        for i,n in enumerate(inorder):
            inorder_root_idxs[n] = i
        return self.build(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1, inorder_root_idxs)

    def build(self, pro, ino, p_lt, p_rt, i_lt, i_rt, root_idx_dic):
        if p_lt>p_rt: return
        root_val = pro[p_lt]
        ino_root_idx = root_idx_dic[root_val]
        nums_of_left = ino_root_idx-i_lt
        root = TreeNode(root_val)
        root.left = self.build(pro, ino, p_lt+1, p_lt+nums_of_left, i_lt, ino_root_idx-1, root_idx_dic)
        root.right = self.build(pro, ino, p_lt+nums_of_left+1, p_rt, ino_root_idx+1, i_rt, root_idx_dic)
        return root