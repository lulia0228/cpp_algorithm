#--coding:utf-8--

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归写法
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.mypreorder(root, res)
        return res

    def mypreorder(self, root, res):
        if not root:
            return
        res.append(root.val)              # 根
        self.mypreorder(root.left, res)   # 左
        self.mypreorder(root.right, res)  # 右

# 栈迭代1
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stk = []
        stk.append(root)
        while stk != []:
            cur = stk.pop(-1)
            res.append(cur.val)
            if cur.right:
                stk.append(cur.right)
            if cur.left:
                stk.append(cur.left)
        return res

# 栈迭代2
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stk = []
        while stk != [] or root != None:
            while root:
                res.append(root.val)
                stk.append(root)
                root = root.left
            root = stk.pop(-1)
            root = root.right
        return res


# 前、中、后序遍历的栈迭代通用写法
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stk = []
        stk.append([root, "go"])
        while stk != [] :
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

