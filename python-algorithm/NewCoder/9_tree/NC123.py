# -*- coding: utf-8 -*-
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Serialize(self, root):
        # write code here
        if not root: return ""
        q = collections.deque()
        q.append(root)
        tmp = []
        while q:
            cur = q.popleft()
            if cur:
                tmp.append(str(cur.val))
                q.append(cur.left)
                q.append(cur.right)
            else:
                tmp.append("#")
        return "!".join(tmp)

    def Deserialize(self, s):
        # write code here
        tmp = s.split("!")
        if s == "": return None
        q = collections.deque()
        root, idx = TreeNode(int(tmp[0])), 0
        q.append(root)
        while q:
            cur = q.popleft()
            idx += 1
            if tmp[idx] != "#":
                cur.left = TreeNode(int(tmp[idx]))
                q.append(cur.left)
            idx += 1
            if tmp[idx] != "#":
                cur.right = TreeNode(int(tmp[idx]))
                q.append(cur.right)
        return root