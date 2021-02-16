# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root == None: return res
        que = []
        que.append(root)
        level = 0
        while que:
            sz = len(que)
            tmp = []
            for i in range(sz):
                t_node = que.pop(0)
                tmp.append(t_node.val)
                if t_node.left: que.append(t_node.left)
                if t_node.right: que.append(t_node.right)
            if level % 2 == 0:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            level += 1
        return res


