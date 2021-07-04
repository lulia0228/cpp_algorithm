#--coding:utf-8--

# 110 判断平衡二叉树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = True
        self.length_transvel(root)
        return self.flag

    def length_transvel(self, root):
        if not root: return 0
        lt = self.length_transvel(root.left)
        rt = self.length_transvel(root.right)
        if abs(lt - rt) > 1: self.flag = False
        return max(lt, rt) + 1


