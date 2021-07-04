#--coding:utf-8--
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     self.res = []
    #     def preOrder(root):
    #         if not root:
    #             return
    #         self.res.append(root.val)
    #         preOrder(root.left)
    #         preOrder(root.right)
    #     preOrder(root)
    #     return self.res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stk = []
        stk.append([root, "go"])
        while stk:
            cur_nd = stk.pop()
            if cur_nd[1] == "print":
                res.append(cur_nd[0].val)
            else:
                if cur_nd[0].right:
                    stk.append([cur_nd[0].right, "go"])
                if cur_nd[0].left:
                    stk.append([cur_nd[0].left, "go"])
                stk.append([cur_nd[0], "print"])
        return res

    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     res = []
    #     stk = []
    #     while stk != [] or root != None:
    #         while root:
    #             res.append(root.val)
    #             stk.append(root)
    #             root = root.left
    #         root = stk.pop(-1)
    #         root = root.right
    #     return res



