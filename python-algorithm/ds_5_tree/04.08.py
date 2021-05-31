#--coding:utf-8--

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == None or root == p or root == q:
            return root
        lt = self.lowestCommonAncestor(root.left, p, q)
        rt = self.lowestCommonAncestor(root.right, p, q)
        if lt == None: return rt
        if rt == None: return lt
        if lt and rt : return root

