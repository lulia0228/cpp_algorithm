# -*- coding: utf-8 -*-

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        cnt = 0
        stk = []
        while stk or pRoot:
            while pRoot:
                stk.append(pRoot)
                pRoot = pRoot.left
            pRoot = stk.pop()
            cnt += 1
            if cnt == k:
                return pRoot
            pRoot = pRoot.right