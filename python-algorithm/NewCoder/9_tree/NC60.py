# -*- coding: utf-8 -*-

# lc958
import collections
class Solution:
    def judgeIt(self, root):
        # write code here
        return [self.isBST(root), self.isMT(root)]

    def isBST(self, root):
        if not root: return False
        stk = []
        pre = None
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            if pre:
                if root.val < pre.val:
                    return False
            pre = root
            root = root.right
        return True

    # 完全二叉树在遇到空节点之后剩余的应当全是空节点
    # 完全二叉树≠满二叉树
    def isMT(self, root):
        if not root: return False
        q = collections.deque()
        q.append(root)
        while q:
            cur_nd = q.popleft()
            if not cur_nd:
                break
            q.append(cur_nd.left)
            q.append(cur_nd.right)
        while q:
            tmp = q.popleft()
            if tmp: return False
        return True