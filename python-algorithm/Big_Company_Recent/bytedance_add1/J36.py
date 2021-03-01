# -*- coding: utf-8 -*-
# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root == None: return None
        pre = None
        new_head = None
        stk = []
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop(-1)
            if pre == None:
                new_head = root
            else:
                root.left = pre
                pre.right = root
            pre = root
            root = root.right
        pre.right = new_head
        new_head.left = pre
        return new_head
# leetcode submit region end(Prohibit modification and deletion)