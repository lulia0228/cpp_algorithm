#--coding:utf-8--

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        res = []
        self.dfs(root, "", res)
        return  sum([int(p) for p in res])

    def dfs(self, root, t_s, res):
        if not root:
            return
        if not root.left and not root.right:
            res.append(t_s+str(root.val))
        self.dfs(root.left, t_s+str(root.val), res)
        self.dfs(root.right, t_s+str(root.val), res)

# 先把根节点放在路径里
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []
        self.dfs(root, str(root.val), res)
        return sum([int(x) for x in res])

    def dfs(self, root, tmp, res):
        if root.left == None and root.right == None:
            res.append(tmp)
            return
        if root.left:
            self.dfs(root.left, tmp+str(root.left.val), res)
        if root.right:
            self.dfs(root.right, tmp+str(root.right.val), res)
        return
