#--coding:utf-8--


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 和判断子树572那道题的结构很类似

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None:
            return 0
        # 对于每个节点考虑三种情况：
        # 1.路径包含这个节点
        # 2.路径不包含这个节点，以当前节点的左子节点开头
        # 3.路径不包含这个节点，以当前节点的右子节点开头
        res = self.start_of_curnode(root, sum)
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        return res

    # 返回以当前节点为根节点的子树的路径和我sum的个数
    def start_of_curnode(self, root, sum):
        if root == None:
            return 0
        res = 0
        if root.val == sum:
            res += 1
        res += self.start_of_curnode(root.left, sum-root.val)
        res += self.start_of_curnode(root.right, sum-root.val)
        return res
