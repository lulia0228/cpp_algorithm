# -*- coding: utf-8 -*-


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        self.postorder(root, res)
        return res

    def postorder(self, root, res):
        if not root:
            return
        self.postorder(root.left, res)  # 左
        self.postorder(root.right, res) # 右
        res.append(root.val)            # 根

# 前、中、后序遍历的栈迭代通用写法
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root: return res
        stk = []
        stk.append((root, "go"))
        while stk:
            cur_nd = stk.pop()
            if cur_nd[1] == "print":
                res.append(cur_nd[0].val)
            else:
                stk.append((cur_nd[0], "print"))
                if cur_nd[0].right:
                    stk.append((cur_nd[0].right, "go"))
                if cur_nd[0].left:
                    stk.append((cur_nd[0].left, "go"))
        return res