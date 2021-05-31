#--coding:utf-8--

# 958. 二叉树的完全性检验

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        que = []
        que.append((root, 1))
        last_node_idx, node_nums = 1, 0
        while que:
            cur_node, idx = que.pop(0)
            node_nums += 1
            last_node_idx = idx
            if cur_node.left:
                que.append((cur_node.left, 2*idx))
            if cur_node.right:
                que.append((cur_node.right, 2*idx+1))
        # 只需要判断最后一个节点的下标是否等于节点总数
        return  last_node_idx == node_nums