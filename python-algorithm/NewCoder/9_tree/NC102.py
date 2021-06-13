# -*- coding: utf-8 -*-

class Solution:
    def lowestCommonAncestor(self , root , o1 , o2 ):
        # write code here
        def attend(root, o1, o2):
            if not root or root.val==o1 or root.val==o2:
                return root
            lt = attend(root.left, o1, o2)
            rt = attend(root.right, o1, o2)
            if lt and rt:
                return root
            if not lt:
                return rt
            if not rt:
                return lt
        zu = attend(root, o1, o2)
        return zu.val