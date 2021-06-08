#--coding:utf-8--


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
        res = []
        que = collections.deque()
        que.append(root)
        while que:
            cur_nd = que.popleft()
            if not cur_nd:
                res.append("#")
            else:
                res.append(str(cur_nd.val))
                que.append(cur_nd.left)
                que.append(cur_nd.right)

        return ','.join(res)

    def Deserialize(self, s):
        # write code here
        if s == "": return None
        nds = s.split(",")
        root = TreeNode(int(nds[0]))
        i = 1
        que = collections.deque()
        que.append(root)
        while que:
            cur_nd = que.popleft()
            if nds[i] != "#":
                cur_nd.left = TreeNode(int(nds[i]))
                que.append(cur_nd.left)
            i += 1
            if nds[i] != "#":
                cur_nd.right = TreeNode(int(nds[i]))
                que.append(cur_nd.right)
            i += 1
        return root

