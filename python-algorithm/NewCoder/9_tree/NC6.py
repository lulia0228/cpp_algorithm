# -*- coding: utf-8 -*-

'''
对于每个节点而言，四种路径情况:
// 1 路径只包含节点本身；
// 2 路径只包含左子树+本身；
// 3 路径只包含本身+右子树；
// 4 路径包含左子树+本身+右子树
'''

class Solution:
    ans = -float("inf")
    def maxPathSum(self, root):
        # write code here
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if not root: return 0
        max_left = self.dfs(root.left)
        max_right = self.dfs(root.right)

        # 在遍历到的每个节点上计算最大值
        self.ans = max(self.ans, root.val)
        self.ans = max(self.ans, root.val + max_left)
        self.ans = max(self.ans, root.val + max_right)
        self.ans = max(self.ans, root.val + max_left + max_right)

        if max_left <= 0 and max_right <= 0:
            return root.val
        return max_left + root.val if max_left > max_right else max_right + root.val