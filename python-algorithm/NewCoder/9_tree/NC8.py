# -*- coding: utf-8 -*-
class Solution:
    def pathSum(self, root, sum):
        # write code here
        res = []
        if not root: return res
        self.dfs(root, sum, [], res)
        return res

    def dfs(self, root, target, tmp, res):
        if not root.left and not root.right:
            if target == root.val:
                tmp.append(root.val)
                res.append(tmp[:])
                tmp.pop()  # 最后个值要弹出去的，否则会影响其它路径递归
            return
        tmp.append(root.val)
        if root.left:
            self.dfs(root.left, target - root.val, tmp, res)
        if root.right:
            self.dfs(root.right, target - root.val, tmp, res)
        tmp.pop()
