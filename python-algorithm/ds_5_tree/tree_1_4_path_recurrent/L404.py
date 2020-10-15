#--coding:utf-8--
'''
@Time   : 2020/10/15
@Author : No Name
'''

class Solution:
    res = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.find_left_leaf(root, root)
        return self.res

    def find_left_leaf(self, cur, pre):
        if not cur.left and not cur.right and pre.left == cur:
            self.res += cur.val
        if cur.left:
            self.find_left_leaf(cur.left, cur)
        if cur.right:
            self.find_left_leaf(cur.right, cur)
