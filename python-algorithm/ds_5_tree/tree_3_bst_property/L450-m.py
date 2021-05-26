#--coding:utf-8--


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None: return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else: # 当前节点就是要删除的节点
            if not root.left:     # 情况1，欲删除节点无左子
                return root.right
            if not root.right:    # 情况2，欲删除节点无右子
                return root.left
            tmp_nd = root.right
            while tmp_nd.left:    # 寻找欲删除节点右子树的最左节点
                tmp_nd = tmp_nd.left
            tmp_nd.left = root.left # 将欲删除节点的左子树接续到其右子树的最左节点的左边
            root = root.right       # 欲删除节点的右子顶替其位置，节点被删除
        return root