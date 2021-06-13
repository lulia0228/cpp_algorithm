# -*- coding: utf-8 -*-

class Solution:
    res = 0
    def sumNumbers(self, root):
        # write code here
        if not root: return 0
        self.dfs(root, "")
        return self.res

    def dfs(self, root, tmp_s):
        if not root.left and not root.right:
            tmp_s += str(root.val)
            self.res += int(tmp_s)
        if root.left:
            self.dfs(root.left, tmp_s + str(root.val))
        if root.right:
            self.dfs(root.right, tmp_s + str(root.val))