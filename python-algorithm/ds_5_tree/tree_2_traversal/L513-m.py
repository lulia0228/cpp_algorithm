# -*- coding: utf-8 -*-


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        res = root.val
        que = []
        que.append(root)
        while que!= []:
            sz = len(que)
            for i in range(sz):
                cur = que.pop(0)
                if i == 0:
                    res = cur.val
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return res