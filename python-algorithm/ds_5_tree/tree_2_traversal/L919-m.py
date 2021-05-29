# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root
        self.que = []
        q = [root]  # 根节点一开始要放在队列中
        while q:
            cur = q.pop(0)
            if not cur.left or not cur.right:
                self.que.append(cur)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    def insert(self, v: int) -> int:
        self.que.append(TreeNode(v))
        father = self.que[0]
        if not father.left:
            father.left = self.que[-1]
        else:
            father.right = self.que[-1]
            self.que.pop(0)
        return father.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()