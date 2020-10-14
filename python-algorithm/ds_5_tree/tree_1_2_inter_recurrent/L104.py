#--coding:utf-8--
'''
@Time   : 2020/10/13
@Author : No Name
'''

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right)+1


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root ==  None:
            return 0
        que = []
        que.append(root)
        level = 0
        while que != []:
            level += 1
            for i in range(len(que)):
                cur_node = que.pop(0)
                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)
        return level

