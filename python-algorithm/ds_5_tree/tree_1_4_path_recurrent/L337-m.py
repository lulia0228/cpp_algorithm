#--coding:utf-8--


class Solution:

    dic = {} # 记忆化搜索

    def rob(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root in self.dic:
            return self.dic[root]
        val1 = root.val
        if root.left:
            val1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val1 += self.rob(root.right.left) + self.rob(root.right.right)
        val2 = self.rob(root.left) + self.rob(root.right)
        res = max(val1, val2)
        self.dic[root] = res
        return res


# 动态规划  没咋看懂
# ls表示偷左子树能带来的最大收益，ln表示不偷左子树能带来的最大收益，rs、rn同理
class Solution:
    def rob(self, root: TreeNode) -> int:
        def _rob(root):
            if not root:
                return 0, 0
            ls, ln = _rob(root.left)
            rs, rn = _rob(root.right)
            return root.val + ln + rn, max(ls, ln) + max(rs, rn)
        return max(_rob(root))