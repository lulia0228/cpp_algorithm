# -*- coding: utf-8 -*-

class Solution:
    def sortedArrayToBST(self, num):
        # write code here
        sz = len(num)
        return self.buildBst(num, 0, sz - 1)

    def buildBst(self, num, lt, rt):
        if lt > rt: return None
        mid = lt + (rt - lt + 1) // 2
        # mid = lt +(rt-lt)//2 # leetcode 2种都可以过；构成的树形不一样而已;牛客这种过不了
        root = TreeNode(num[mid])
        root.left = self.buildBst(num, lt, mid - 1)
        root.right = self.buildBst(num, mid + 1, rt)
        return root