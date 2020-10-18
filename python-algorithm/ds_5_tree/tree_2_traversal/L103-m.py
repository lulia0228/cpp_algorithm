# -*- coding: utf-8 -*-


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        que = []
        level = 0
        que.append(root)
        while que!= []:
            level += 1
            tmp = []
            for _ in range(len(que)):
                cur = que.pop(0)
                tmp.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            if level%2 == 0:
                res.append(tmp[::-1])
            else:
                res.append(tmp)
        return res