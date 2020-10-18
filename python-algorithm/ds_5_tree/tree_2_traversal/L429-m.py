# -*- coding: utf-8 -*-


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        que = []
        que.append(root)
        while que!= []:
            tmp = []
            sz = len(que)
            for i in range(sz):
                cur = que.pop(0)
                tmp.append(cur.val)
                for node in cur.children:
                    if node:
                        que.append(node)
            res.append(tmp)
        return res