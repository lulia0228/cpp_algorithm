#--coding:utf-8--

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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
