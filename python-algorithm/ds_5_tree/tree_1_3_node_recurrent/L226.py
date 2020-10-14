#--coding:utf-8--
'''
@Time   : 2020/10/14
@Author : No Name
'''

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

