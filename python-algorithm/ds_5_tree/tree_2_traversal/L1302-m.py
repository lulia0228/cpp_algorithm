#--coding:utf-8--

#  BFS
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root: return 0
        que = [root]
        tmp = []
        while que:
            sz = len(que)
            tmp = []
            for i in range(sz):
                cur_nd = que.pop(0)
                tmp.append(cur_nd)
                if cur_nd.left:
                    que.append(cur_nd.left)
                if cur_nd.right:
                    que.append(cur_nd.right)
        res = 0
        for nd in tmp:
            res += nd.val
        return res

#   队列中顺便记录遍历层数
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = collections.deque([(root, 0)])
        maxdep, total = -1, 0
        while len(q) > 0:
            node, dep = q.pop()
            if dep > maxdep:
                maxdep, total = dep, node.val
            elif dep == maxdep:
                total += node.val
            if node.left:
                q.append((node.left, dep + 1))
            if node.right:
                q.append((node.right, dep + 1))
        return total

# DFS
class Solution:
    def __init__(self):
        self.maxdep = -1
        self.total = 0

    def deepestLeavesSum(self, root: TreeNode) -> int:
        def dfs(node, dep):
            if not node:
                return
            if dep > self.maxdep:
                self.maxdep, self.total = dep, node.val
            elif dep == self.maxdep:
                self.total += node.val
            dfs(node.left, dep + 1)
            dfs(node.right, dep + 1)

        dfs(root, 0)
        return self.total

