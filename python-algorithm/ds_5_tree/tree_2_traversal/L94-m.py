# -*- coding: utf-8 -*-

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        self.postorder(root, res)
        return res

    def postorder(self, root, res):
        if not root:
            return
        self.postorder(root.left, res)  # 左
        res.append(root.val)            # 根
        self.postorder(root.right, res) # 右

# 栈迭代1
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root == None: return res
        tmp = root
        stk = []
        while stk or tmp:
            while tmp:
                # 下面2句顺序不要弄反
                stk.append(tmp)
                tmp = tmp.left
            tmp = stk.pop()
            res.append(tmp.val)
            tmp = tmp.right
        return res

# 前、中、后序遍历的栈迭代通用写法
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
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