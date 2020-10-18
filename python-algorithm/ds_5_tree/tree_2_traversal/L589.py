# -*- coding: utf-8 -*-


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        self.mypre(root, res)
        return res

    def mypre(self, root, res):
        if not root:
            return
        res.append(root.val)
        for node in root.children:
            self.mypre(node, res)

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        stk = []
        stk.append([root, "go"])
        while stk != []:
            cur = stk.pop(-1)
            if cur[1] == "print":
                res.append(cur[0].val)
            else:
                for i in range(len(cur[0].children)-1, -1, -1):
                    stk.append([cur[0].children[i], "go"])
                stk.append([cur[0], "print"])
        return res