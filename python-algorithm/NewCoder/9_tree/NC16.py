# -*- coding: utf-8 -*-

# 递归的方法
class Solution:
    def isSymmetric(self, root):
        # write code here
        return self.isSYM(root, root)

    def isSYM(self, r1, r2):
        if not r1 and not r2: return True
        if not r1 or not r2: return False
        if r1.val != r2.val: return False
        return self.isSYM(r1.left, r2.right) and self.isSYM(r1.right, r2.left)

# 迭代的方法
import collections
class Solution:
    def isSymmetric(self , root ):
        # write code here
        if not root: return True
        q = collections.deque()
        q.append(root)
        while q:
            cur_nd = q.popleft()
            if cur_nd == root:
                q.append(root.left)
                q.append(root.right)
            else:
                cur_nd_nxt = q.popleft()
                if not cur_nd and not cur_nd_nxt:
                    continue # 遇到空节点必须continue 否则下面cur_nd.left会报错
                elif not cur_nd or not cur_nd_nxt :
                    return False
                elif cur_nd.val != cur_nd_nxt.val:
                    return False
                q.append(cur_nd.left)
                q.append(cur_nd_nxt.right)
                q.append(cur_nd.right)
                q.append(cur_nd_nxt.left)
        return True