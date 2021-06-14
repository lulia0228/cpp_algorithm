# -*- coding: utf-8 -*-

class Solution:
    def findError(self , root ):
        # write code here
        # first, second = None, None
        record = []
        pre = None
        stk = []
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            if pre:
                if pre.val > root.val:
                    record.append(pre.val)
                    record.append(root.val)
            pre = root
            root = root.right
        if len(record) == 2:
            return [record[1], record[0]]
        else:
            return [record[3], record[0]]