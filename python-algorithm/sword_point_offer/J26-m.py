# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 和leetcode572有区别，572是判断B是A的子树（以相同的根节点开始所有的子节点都一样）
# 这里是判断B是A的子结构，即B只要是和A中相同根节点的子树的部分结构是一样的即可。

# 案例A=[10,12,6,8,3,11] B=[10,12,6,8] 在572为fasle 在本题应该为True

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A == None or B == None:  # 说明A树都走到了叶子结点也没找到相同的子结构
            return False
        if self.isEqual(A, B):
            return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def isEqual(self, A, B):
        if A == None and B == None:
            return True
        # 子树和子结构区别体现：B是空而A不是空的时候是True
        if A != None and B == None:
            return True
        if A == None and B != None:
            return False
        if A.val != B.val:
            return False
        return self.isEqual(A.left, B.left) and self.isEqual(A.right, B.right)

