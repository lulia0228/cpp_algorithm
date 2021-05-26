#--coding:utf-8--

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS+BFS

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        def helper(root):
            if root.left:
                root.left.par = root
                helper(root.left)
            if root.right:
                root.right.par = root
                helper(root.right)

        helper(root)  # 所有节点完成遍历;给每个节点一个指向父节点的par指针
        root.par = None  # 补充根节点的父节点为空
        que = [target]  # 每一层的节点列表，初始化为距离=0层，即target节点本身
        seen = {target}  # 已访问的节点列表
        level = 0
        nd_ls = []
        while que:
            tmp = []
            sz = len(que)
            for i in range(sz):
                cur_nd = que.pop(0)
                tmp.append(cur_nd)
                for son in [cur_nd.left, cur_nd.right, cur_nd.par]:
                    if son and son not in seen:
                        seen.add(son)
                        que.append(son)
            level += 1
            if level == K+1:
                nd_ls = tmp
                break
        res = [nd.val for nd in nd_ls]
        return res