# -*- coding: utf-8 -*-
class Solution:
    def mergeTrees(self , t1 , t2 ):
        # write code here
        if not t1 :
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left )
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

# 新建一个树
class Solution:
    def mergeTrees(self, t1, t2):
        # write code here
        if not t1:
            return t2
        if not t2:
            return t1
        # if t1 and t2
        root = TreeNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root