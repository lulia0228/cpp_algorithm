# -*- coding: utf-8 -*-

# 非递归写法
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if not root.left:
                root = root.right
            else:
                # 找左子树最右边的节点
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right
                # 将原来的右子树接到左子树的最右边节点
                tmp.right = root.right
                # 将原来的左子树插入到原来的右子树的地方
                root.right = root.left
                root.left = None
                root = root.right

# 递归写法
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        # 必须写成if else 不能平行
        if not root.left:
            self.flatten(root.right)
        elif not root.right:
            root.right = root.left
            root.left = None
            self.flatten(root.right)
        else:
            cur = root.left
            while cur.right:
                cur = cur.right
            cur.right = root.right
            root.right = root.left
            root.left = None
            self.flatten(root.right)

