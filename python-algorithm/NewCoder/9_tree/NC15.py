# -*- coding: utf-8 -*-
import collections
class Solution:
    def levelOrder(self , root ):
        # write code here
        res = []
        if not root: return res
        q = collections.deque()
        q.append(root)
        while q:
            sz = len(q)
            tmp = []
            for _ in range(sz):
                cur_nd = q.popleft()
                tmp.append(cur_nd.val)
                if cur_nd.left:
                    q.append(cur_nd.left)
                if cur_nd.right:
                    q.append(cur_nd.right)
            res.append(tmp)
        return res