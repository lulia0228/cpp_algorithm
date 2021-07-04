#--coding:utf-8--

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSym(root, root)

    def isSym(self, r1, r2):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        if r1.val != r2.val:
            return False
        return self.isSym(r1.left, r2.right) and self.isSym(r1.right, r2.left)

# bfs
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        q = collections.deque()
        q.append(root.left)
        q.append(root.right)
        while q:
            cur_nd1 = q.popleft()
            cur_nd2 = q.popleft()
            if not cur_nd1 and not cur_nd2:
                continue
            if not cur_nd1 or not cur_nd2:
                return False
            if cur_nd1.val != cur_nd2.val:
                return False
            q.append(cur_nd1.left)
            q.append(cur_nd2.right)
            q.append(cur_nd1.right)
            q.append(cur_nd2.left)
        return True

