# -*- coding: utf-8 -*-


# 判断一棵树是否为二叉搜索树

# 递归
class Solution:
    def isValidBST(self, root):
        def BFS(root, left, right):
            if root is None:
                return True
            if left < root.val < right:
                return BFS(root.left, left, root.val) and BFS(root.right, root.val, right)
            else:
                return False
        return BFS(root, -float('inf'), float('inf'))


# 中序遍历二叉树；为了省空间，不采用全部记录下来的方式，设置一个变量记录上一个节点即可
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stk = []
        pre = -float("inf")
        while stk != [] or root != None:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop(-1)
            if root.val <= pre:
                return False
            pre = root.val
            root = root.right
        return True