# -*- coding: utf-8 -*-

import collections
class Solution:
    def zigzagLevelOrder(self , root ):
        # write code here
        res = []
        if not root: return res
        q = collections.deque()
        q.append(root)
        level = 0
        while q:
            sz = len(q)
            tmp = []
            level += 1
            for _ in range(sz):
                cur_nd = q.popleft()
                tmp.append(cur_nd.val)
                if cur_nd.left:
                    q.append(cur_nd.left)
                if cur_nd.right:
                    q.append(cur_nd.right)
            if level%2 == 0:
                res.append(tmp[::-1])
            else:
                res.append(tmp)
        return res