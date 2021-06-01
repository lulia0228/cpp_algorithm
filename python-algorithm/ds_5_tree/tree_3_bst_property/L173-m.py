#--coding:utf-8--

# 173. 二叉搜索树迭代器

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stk = []
        self.cur = root

    def next(self) -> int:
        while self.cur:
            self.stk.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.stk.pop()
        res = self.cur.val
        self.cur = self.cur.right
        return res

    def hasNext(self) -> bool:
        return self.cur != None or len(self.stk) != 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()