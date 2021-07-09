#--coding:utf-8--

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0
        if not root: return 0
        q = collections.deque()
        q.append((root, 1))
        while q:
            sz = len(q)
            start, end = 0, 0
            for i in range(sz):
                cur_nd = q.popleft()
                if i == 0:
                    start = cur_nd[1]
                if i == sz - 1:
                    end = cur_nd[1]
                if cur_nd[0].left:
                    q.append((cur_nd[0].left, 2 * cur_nd[1]))
                if cur_nd[0].right:
                    q.append((cur_nd[0].right, 2 * cur_nd[1] + 1))
            ans = max(ans, end - start + 1)
        return ans

