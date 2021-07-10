# -*- coding: utf-8 -*-

# 根据二叉搜索树的性质，即二叉树后序遍历时候，每次把末尾即根节点作为pivot，
# 那么从遍历序列从前往后，前半部分肯定是小于pivot，后半部分是大于pivot

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i, j):
            if i >= j:
                return True
            p = i
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            while postorder[p] > postorder[j]:
                p += 1
            # if p == j:
            #     return True
            # else:
            #     return False
            # return recur(i, m-1) and recur(m, j-1)
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)

