#--coding:utf-8--
'''
@Time   : 2020/10/13
@Author : No Name
'''

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        # 对当前节点而言，左子树为空，右子树不一定为空
        if left == 0:
            return right+1
        if right == 0:
            return left+1
        return min(left, right)+1


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root ==  None:
            return 0
        que = []
        que.append(root)
        level = 0
        while que != []:
            level += 1
            for i in range(len(que)):
                cur_node = que.pop(0)
                if cur_node.left == None and cur_node.right == None:
                    return level
                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)
        return 0