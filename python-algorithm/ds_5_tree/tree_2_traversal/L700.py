#--coding:utf-8--

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        tmp = root
        while tmp:
            if tmp.val == val: return tmp
            elif tmp.val > val:
                tmp = tmp.left
            else:
                tmp = tmp.right
        return None