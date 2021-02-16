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
        if root == None: return None
        pre = None
        head = None
        stk = []
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            if not pre:
                head = root
            else:
                pre.right = root
                root.left = pre
            pre = root
            root = root.right
        # pre是中序遍历的最后一个元素(易出错)
        pre.right = head
        head.left = pre
        return head