# -*- coding: utf-8 -*-


class Solution:
    def hasPathSum(self , root , sum ):
        # write code here
        if not root: return False
        if not root.left and not root.right and root.val == sum:
            return True
        flag1 = self.hasPathSum(root.left, sum-root.val)
        flag2 = self.hasPathSum(root.right, sum-root.val)
        # 即2个子树有一个为真则是满足要求的
        return flag1 or flag2