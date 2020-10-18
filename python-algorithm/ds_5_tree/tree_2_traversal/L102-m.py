# -*- coding: utf-8 -*-


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            res.append(tmp)
        return res