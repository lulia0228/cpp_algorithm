# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 9:40
# @Author  : No Name

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