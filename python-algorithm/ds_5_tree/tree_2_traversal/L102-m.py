# -*- coding: utf-8 -*-

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res
        q = collections.deque()
        q.append(root)
        while q:
            sz = len(q)
            tmp = []
            for i in range(sz):
                cur_nd = q.popleft()
                tmp.append(cur_nd.val)
                if cur_nd.left:
                    q.append(cur_nd.left)
                if cur_nd.right:
                    q.append(cur_nd.right)
            res.append(tmp)
        return res