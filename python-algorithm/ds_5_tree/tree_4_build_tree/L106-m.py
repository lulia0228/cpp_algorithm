# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        sz = len(inorder)
        ino_idx_dic = {}
        for i, val in enumerate(inorder):
            ino_idx_dic[val] = i
        return self.my_build(postorder, inorder, 0, sz-1, 0, sz-1, ino_idx_dic)

    def my_build(self, postorder, inorder, pos_lt, pos_rt, ino_left, ino_rt, ino_idx_dic):
        if pos_lt>pos_rt:
            return None
        root_val = postorder[pos_rt]
        # 找到当前根节点在两个遍历中的索引
        ino_root_idx = ino_idx_dic[root_val]
        # 左子树中节点数目
        nums_of_left = ino_root_idx-ino_left
        # 创建当前根节点
        root = TreeNode(root_val)
        root.left = self.my_build(postorder, inorder, pos_lt,
                    pos_lt+nums_of_left-1, ino_left, ino_root_idx-1, ino_idx_dic)
        root.right = self.my_build(postorder, inorder,
                    pos_lt+nums_of_left, pos_rt-1, ino_root_idx+1, ino_rt, ino_idx_dic)

        return root

