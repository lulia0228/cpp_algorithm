#--coding:utf-8--
'''
@Time   : 2020/10/14
@Author : No Name
'''

# 题目：思路
#     两个节点p,q分为两种情况：
#         	p和q在相同子树中
#         	p和q在不同子树中
#     从根节点遍历，递归向左右子树查询节点信息。
#     递归终止条件：如果当前节点为空(走过叶子结点了)或等于p或q，则返回当前节点。
#         	递归遍历左右子树，如果左右子树查到节点都不为空，则表明p和q分别在左右子树中，因此，当前节点即为最近公共祖先；
#         	如果左右子树其中一个不为空，则返回非空节点。


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left == None:
            return right
        if right == None:
            return left