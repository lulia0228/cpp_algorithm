# -*- coding: utf-8 -*-


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        que = []
        que.append(root)
        while que != []:
            sz = len(que) # 必须设个变量提前记录，否则在循环中会改变
            for i in range(sz):
                cur = que.pop(0)
                if i != sz-1:
                    cur.next = que[0]
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return root