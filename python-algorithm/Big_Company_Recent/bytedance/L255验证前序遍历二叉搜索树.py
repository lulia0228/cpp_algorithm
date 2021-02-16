# -*- coding: utf-8 -*-

# 验证前序遍历序列是否是二叉搜索树的前序遍历序列

'''由于二叉搜索树中，树上任何一个节点，它的值比所有的左子树大，比所有的右子树小
遇到左子树时，全部入栈，遇到右子树时，将与其平级的左子树出栈【它具有大于平级左子树的性质】；
出现出栈的时候，新来的元素必定是大于已经出栈的元素。'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verifyPreorder(self, preorder):
        if not preorder: return True
        stk = []
        stk.append(preorder[0])
        temp = -float("inf") # temp表示的树中应该比当前节点值小的最大节点
        for i in range(1, len(preorder)):
            if preorder[i] < temp: return False
            while stk != [] and preorder[i] > stk[0]:
                temp = stk.pop(0)
            stk.append(preorder[i])
        return True

if __name__ == "__main__":
    # pre = [5,2,8,6,10]
    pre = [5,2,6,1,3]
    cls = Solution().verifyPreorder(pre)
    print(cls)
