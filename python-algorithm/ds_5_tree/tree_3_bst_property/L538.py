# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 16:31
# @Author  : No Name

# 逆中序遍历（右-根-左），不是后续遍历
class Solution:
    cur_sum = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.convertBST(root.right)
        self.cur_sum += root.val
        root.val = self.cur_sum
        self.convertBST(root.left)
        return root