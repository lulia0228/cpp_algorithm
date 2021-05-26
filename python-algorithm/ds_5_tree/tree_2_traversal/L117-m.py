#--coding:utf-8--
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        que = [root]
        while que:
            sz = len(que)
            last = None
            for i in range(sz):
                cur_nd = que.pop(0)
                if cur_nd.left:
                    que.append(cur_nd.left)
                if cur_nd.right:
                    que.append(cur_nd.right)
                if last:
                    last.next = cur_nd
                last = cur_nd
        return root