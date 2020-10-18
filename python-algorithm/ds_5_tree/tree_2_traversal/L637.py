# -*- coding: utf-8 -*-


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        if not root:
            return res
        que = []
        que.append(root)
        while que!= []:
            tmp = 0
            sz = len(que)
            for _ in range(sz):
                cur = que.pop(0)
                tmp += cur.val
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            res.append(tmp/sz)
        return res