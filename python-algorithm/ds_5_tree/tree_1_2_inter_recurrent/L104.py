#--coding:utf-8--


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        lt = self.maxDepth(root.left)
        rt = self.maxDepth(root.right)
        return max(lt, rt)+1

import collections
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root ==  None:
            return 0
        q = collections.deque()
        q.append(root)
        level = 0
        while q:
            level += 1
            for i in range(len(que)):
                cur_node = q.popleft()
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
        return level

