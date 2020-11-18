#--coding:utf-8--

# 二叉搜索树的第K大值节点和leetcode230第K小节点反过来
# 即采用逆中序遍历解决

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        cnt = 0
        stk = []
        while stk != [] or root != None:
            while root:
                stk.append(root)
                root = root.right
            root = stk.pop(-1)
            if cnt == k-1:
                return root.val
            cnt += 1
            root = root.left
        return -1