# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        sz = len(pre)
        idx_in = {}
        for idx, n in enumerate(tin):
            idx_in[n] = idx
        res = self.rebuild_(pre, tin, 0, sz-1, 0, sz-1, idx_in)
        return res

    def rebuild_(self, pre, tin, p_st, p_ed, i_st, i_ed, idx_tin):
        if p_ed < p_st:
            return None
        r_val = pre[p_st]
        r_in_tin = idx_tin[r_val]
        root = TreeNode(r_val)
        nums_of_left = r_in_tin - i_st
        root.left = self.rebuild_(pre, tin, p_st + 1, p_st + nums_of_left, i_st, r_in_tin - 1, idx_tin)
        root.right = self.rebuild_(pre, tin, p_st + nums_of_left + 1, p_ed, r_in_tin + 1, i_ed, idx_tin)
        return root

a = [1,2,3,4,5,6,7]
b = [3,2,4,1,6,5,7]
root = Solution().reConstructBinaryTree(a,b)

res = []
def preorder(root):
    if not root: return
    res.append(root.val)
    if root.left:
        preorder(root.left)
    # res.append(root.val)
    if root.right:
        preorder(root.right)

preorder(root)
print(res)