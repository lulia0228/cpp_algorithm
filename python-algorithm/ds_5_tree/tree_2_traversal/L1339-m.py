#--coding:utf-8--
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 后序遍历
# 计算出以每个节点作为根节点的子树的和，在同剩下的节点的和做乘积

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        mod = 10 ** 9 + 7

        # 计算所有节点之和
        def getsum(root):
            if not root:
                return 0
            total = root.val
            total += getsum(root.left)
            total += getsum(root.right)
            return total

        total = getsum(root)

        res = float('-inf')
        # 计算每个节点分裂后的乘积
        # 后序遍历
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            subsum = root.val + left + right
            nonlocal res
            res = max(res, subsum * (total - subsum))
            return subsum

        dfs(root)
        return res % mod


class Solution1:
    res = float('-inf')

    def maxProduct(self, root: TreeNode) -> int:
        mod = 10 ** 9 + 7

        # 计算所有节点之和
        def getsum(root):
            if not root:
                return 0
            total = root.val
            total += getsum(root.left)
            total += getsum(root.right)
            return total

        total = getsum(root)

        # 计算每个节点分裂后的乘积
        # 后序遍历
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            subsum = root.val + left + right
            # nonlocal res
            self.res = max(self.res, subsum * (total - subsum))
            return subsum

        dfs(root)
        return self.res % mod