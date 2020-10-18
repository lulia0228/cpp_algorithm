# -*- coding: utf-8 -*-


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        self.mypost(root, res)
        return res

    def mypost(self, root, res):
        if not root:
            return
        for node in root.children:
            self.mypost(node, res)
        res.append(root.val)

# 通用写法
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
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
                stk.append([cur[0], "print"])
                for i in range(len(cur[0].children)-1, -1, -1):
                    stk.append([cur[0].children[i], "go"])
        return res