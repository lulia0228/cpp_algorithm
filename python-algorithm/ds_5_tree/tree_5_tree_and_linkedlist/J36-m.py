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
        if root == None:
            return None
        pre = None
        head = None
        stk = []
        while stk != [] or root != None:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop(-1)
            if pre == None:
                # 找到中序遍历起始节点head
                head = root
                pass
            else:
                root.left = pre
                pre.right = root
            pre = root
            root = root.right
        # 首尾连起来
        head.left = pre
        pre.right = head
        return head