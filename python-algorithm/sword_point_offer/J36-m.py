#--coding:utf-8--


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
        stk = []
        pre = None
        head = None
        if root == None: return root
        while stk != [] or root != None:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop(-1)
            if pre == None:
                head = root
            else:
                root.left = pre
                pre.right = root
            pre = root
            root = root.right
        pre.right = head
        head.left = pre

        return head

