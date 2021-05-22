#--coding:utf-8--

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            if not root: return
            inorder(root.left)
            inorder_ls.append(root)
            inorder(root.right)

        error_order_nodes = []
        inorder_ls = []
        inorder(root)

        for i in range(len(inorder_ls)-1):
            if inorder_ls[i].val > inorder_ls[i+1].val:
                error_order_nodes.append(inorder_ls[i])
                error_order_nodes.append(inorder_ls[i+1])

        if len(error_order_nodes) == 2:
            error_order_nodes[0].val, error_order_nodes[1].val = \
            error_order_nodes[1].val, error_order_nodes[0].val
        elif len(error_order_nodes) == 4:
            error_order_nodes[0].val, error_order_nodes[3].val = \
            error_order_nodes[3].val, error_order_nodes[0].val


class Solution1:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        x, y = None, None
        pre = None
        stk = []
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            if pre:
                if pre.val > root.val:
                    y = root
                    if not x:
                        x = pre
            pre = root
            root = root.right

        x.val, y.val = y.val, x.val