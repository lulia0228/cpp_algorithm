#--coding:utf-8--
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root == None:
            return res
        que = []
        que.append(root)
        level = 0
        while que != []:
            curline = []
            cur_layer_size = len(que)
            for i in range(cur_layer_size):
                cur_node = que.pop(0)
                curline.append(cur_node.val)
                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)
            if level%2 == 0:
                res.append(curline)
            else:
                res.append(curline[::-1])
            level += 1
        return res