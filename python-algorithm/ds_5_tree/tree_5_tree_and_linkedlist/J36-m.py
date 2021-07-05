# -*- coding: utf-8 -*-
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
        if not root: return None
        pre = None
        stk = []
        cursor = root
        while stk or cursor:
            while cursor:
                stk.append(cursor)
                cursor = cursor.left
            cursor = stk.pop()
            if not pre:
                head = cursor
            else:
                pre.right = cursor
                cursor.left = pre
            pre = cursor
            cursor = cursor.right
        #  连接首尾
        head.left = pre
        pre.right = head
        return head


