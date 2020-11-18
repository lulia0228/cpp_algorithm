#--coding:utf-8--


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        res = []
        if root == None:
            return res
        que = []
        que.append(root)
        while que != []:
            cur_node = que.pop(0)
            res.append(cur_node.val)
            if cur_node.left:
                que.append(cur_node.left)
            if cur_node.right:
                que.append(cur_node.right)
        return res