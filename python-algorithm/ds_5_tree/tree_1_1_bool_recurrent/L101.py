#--coding:utf-8--
'''
@Time   : 2020/10/13
@Author : No Name
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isMirror(root, root)

    # 判断2棵树对称相等
    def isMirror(self, t1, t2):
        if t1 == None and t2 == None:
            return True
        # 其中 一个为空
        if t1 == None or t2 == None:
            return False
        if t1.val != t2.val:
            return False
        return self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)


# 队列
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        que = []
        que.append(root.left)
        que.append(root.right)
        while que != []:
            t1 = que.pop(0)
            t2 = que.pop(0)
            if t1==None and t2==None:
                continue
            if t1==None or t2==None:
                return False
            if t1.val != t2.val:
                return False
            que.append(t1.left)
            que.append(t2.right)
            que.append(t1.right)
            que.append(t2.left)
        return True

