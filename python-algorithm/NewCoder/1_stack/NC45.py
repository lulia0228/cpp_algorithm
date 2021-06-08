#--coding:utf-8--
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类 the root of binary tree
# @return int整型二维数组
#
class Solution:
    def threeOrders(self, root):
        # write code here
        def preorderTraversal(root: TreeNode):
            res = []
            if not root:
                return res
            stk = []
            stk.append([root, "go"])
            while stk != []:
                cur = stk.pop(-1)
                if cur[1] == "print":
                    res.append(cur[0].val)
                else:

                    if cur[0].right:
                        stk.append([cur[0].right, "go"])
                    if cur[0].left:
                        stk.append([cur[0].left, "go"])
                    stk.append([cur[0], "print"])
            return res

        def inorderTraversal(root: TreeNode):
            res = []
            if not root:
                return res
            stk = []
            stk.append([root, "go"])
            while stk != []:
                cur = stk.pop(-1)
                if cur[1] == "print":
                    res.append(cur[0].val)
                else:

                    if cur[0].right:
                        stk.append([cur[0].right, "go"])
                    stk.append([cur[0], "print"])
                    if cur[0].left:
                        stk.append([cur[0].left, "go"])
            return res

        def postorderTraversal(root: TreeNode):
            res = []
            if not root:
                return res
            stk = []
            stk.append([root, "go"])
            while stk != []:
                cur = stk.pop(-1)
                if cur[1] == "print":
                    res.append(cur[0].val)
                else:
                    stk.append([cur[0], "print"])
                    if cur[0].right:
                        stk.append([cur[0].right, "go"])
                    if cur[0].left:
                        stk.append([cur[0].left, "go"])
            return res

        res = []
        res.append(preorderTraversal(root))
        res.append(inorderTraversal(root))
        res.append(postorderTraversal(root))
        return res