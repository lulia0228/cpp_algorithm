#--coding:utf-8--
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        pre = None
        stk = []
        while root or stk :
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop(-1)
            if pre ==  p:
                return root
            pre = root
            root = root.right
        return None
