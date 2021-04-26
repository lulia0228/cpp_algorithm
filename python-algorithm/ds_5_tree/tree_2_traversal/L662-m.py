#--coding:utf-8--
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        que = []
        que.append((root, 1))
        max_bridth = 0
        while que:
            sz = len(que)
            tmp = []
            for i in range(sz):
                cur_nd, idx = que.pop(0)
                tmp.append(idx)
                if cur_nd.left:
                    que.append((cur_nd.left, 2*idx))
                if cur_nd.right:
                    que.append((cur_nd.right, 2*idx+1))
            cur_bridth = tmp[-1]-tmp[0]+1
            max_bridth = max(max_bridth, cur_bridth)
        return max_bridth