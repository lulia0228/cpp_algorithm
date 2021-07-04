#--coding:utf-8--
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root == None:
            return False
        if not root.left and not root.right and targetSum == root.val:
            return True
        if self.hasPathSum(root.left, targetSum-root.val):
            return True
        if self.hasPathSum(root.right, targetSum-root.val):
            return True
        return False

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # 说明走到叶子节点的时候不满足，然后走到了叶子节点的子节点为空
        if root == None:
            return False
        if root.left == None and root.right == None and root.val == sum:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

