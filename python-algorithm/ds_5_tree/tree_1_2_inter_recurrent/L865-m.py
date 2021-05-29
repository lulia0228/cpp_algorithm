#--coding:utf-8--

'''类似于前序遍历，从根节点开始，分别求左右子树的高度left，和right。

情况1：left=right 那么两边子树的最深高度相同，返回本节点
情况2：left<right 说明最深节点在右子树，直接返回右子树的递归结果
情况2：left>right 说明最深节点在左子树，直接返回右子树的递归结果'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root: return None
        lt = self.max_depth(root.left)
        rt = self.max_depth(root.right)
        if lt == rt: return root
        elif lt > rt: return self.subtreeWithAllDeepest(root.left)
        return self.subtreeWithAllDeepest(root.right)

    def max_depth(self, root):
        if not root : return 0
        left = self.max_depth(root.left)
        right = self.max_depth(root.right)
        return max(left, right)+1