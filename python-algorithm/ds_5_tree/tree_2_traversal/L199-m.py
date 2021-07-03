#--coding:utf-8--

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if root == None: return res
        q = collections.deque()
        q.append(root)
        while q:
            sz = len(q)
            for i in range(sz):
                cur_nd = q.popleft()
                if i == sz-1:
                    res.append(cur_nd.val)
                if cur_nd.left:
                    q.append(cur_nd.left)
                if cur_nd.right:
                    q.append(cur_nd.right)
        return res

# DFS
class Solution1:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if root == None: return res
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, depth, res):
        if root == None: return
        # 每层第一个被访问到的就是每层最右边的
        if len(res) == depth:
            res.append(root.val)
        self.dfs(root.right, depth + 1, res)
        self.dfs(root.left, depth + 1, res)
        return