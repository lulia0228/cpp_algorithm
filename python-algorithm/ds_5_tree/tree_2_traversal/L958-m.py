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
        q = collections.deque()
        q.append(root)
        while q:
            cur_nd = q.popleft()
            # 如果出现空节点，其后面的节点应该都为空
            if cur_nd == None:
                while q:
                    t_nd = q.popleft()
                    if t_nd != None:
                        return False
            else:
                q.append(cur_nd.left)
                q.append(cur_nd.right)
        return True

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        q = collections.deque()
        q.append((root, 1))
        last_node_idx, node_nums = 1, 0
        while q:
            cur_node, idx = q.popleft()
            node_nums += 1
            last_node_idx = idx
            if cur_node.left:
                q.append((cur_node.left, 2*idx))
            if cur_node.right:
                q.append((cur_node.right, 2*idx+1))
        # 只需要判断最后一个节点的下标是否等于节点总数
        return  last_node_idx == node_nums