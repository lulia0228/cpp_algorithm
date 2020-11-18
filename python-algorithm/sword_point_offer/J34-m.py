#--coding:utf-8--

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if root == None:
            return res
        self.dfs(root, sum, [], res)
        return res

    def dfs(self, root, target, tmp, res):
        if root == None:
            return
        tmp.append(root.val)
        if root.left == None and root.right==None and root.val == target:
            res.append(tmp[:])
        self.dfs(root.left, target-root.val, tmp, res)
        self.dfs(root.right, target-root.val, tmp, res)
        tmp.pop(-1)
