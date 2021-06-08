# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类
# @return int整型二维数组
#

import collections

class Solution:
    def zigzagLevelOrder(self, root):
        # write code here
        res = []
        if not root: return res
        que = collections.deque()
        que.append(root)
        level = 0
        while que:
            sz = len(que)
            tmp = []
            level += 1
            for _ in range(sz):
                cur_nd = que.popleft()
                tmp.append(cur_nd.val)
                if cur_nd.left:
                    que.append(cur_nd.left)
                if cur_nd.right:
                    que.append(cur_nd.right)
            if level % 2 == 0:
                res.append(tmp[::-1])
            else:
                res.append(tmp)
        return res




