# -*- coding: utf-8 -*-
import collections
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot: return []
        res = []
        q = collections.deque()
        q.append(pRoot)
        while q:
            sz = len(q)
            tmp = []
            for _ in range(sz):
                cur = q.popleft()
                tmp.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(tmp)
        return res