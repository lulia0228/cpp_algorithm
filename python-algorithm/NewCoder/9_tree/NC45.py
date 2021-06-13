# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def threeOrders(self, root):
        # write code here
        def preOrder(root):
            res = []
            if not root: return res
            stk = [(root, "go")]
            while stk:
                cur_nd = stk.pop()
                if cur_nd[1] == "print":
                    res.append(cur_nd[0].val)
                else:
                    if cur_nd[0].right:
                        stk.append((cur_nd[0].right, "go"))
                    if cur_nd[0].left:
                        stk.append((cur_nd[0].left, "go"))
                    stk.append((cur_nd[0], "print"))
            return res

        def inOrder(root):
            res = []
            if not root: return res
            stk = [(root, "go")]
            while stk:
                cur_nd = stk.pop()
                if cur_nd[1] == "print":
                    res.append(cur_nd[0].val)
                else:
                    if cur_nd[0].right:
                        stk.append((cur_nd[0].right, "go"))
                    stk.append((cur_nd[0], "print"))
                    if cur_nd[0].left:
                        stk.append((cur_nd[0].left, "go"))
            return res

        def postOrder(root):
            res = []
            if not root: return res
            stk = [(root, "go")]
            while stk:
                cur_nd = stk.pop()
                if cur_nd[1] == "print":
                    res.append(cur_nd[0].val)
                else:
                    stk.append((cur_nd[0], "print"))
                    if cur_nd[0].right:
                        stk.append((cur_nd[0].right, "go"))
                    if cur_nd[0].left:
                        stk.append((cur_nd[0].left, "go"))
            return res

        res = []
        if not root: return res
        res.append(preOrder(root))
        res.append(inOrder(root))
        res.append(postOrder(root))
        return res