#--coding:utf-8--


# 例如： 序列1,...,7
# F(n)表示以n作为根节点的二叉搜索树的种类 G(n)表示表示以1~n个数可组成的二叉搜索树的种类
# F(3) = G(2) * G(4)    G(2)是元素1,2可构成的左子树的种类，G(4)是元素4,5,6,7可构成的右子树的种类
# G(n) = F(1)+...+F(n)
# 2个公式结合 就得到G(n)的递推公式

# 边界条件G(0)=1 G(1)=1 G(0)代表空因此是1种 G(1)代表一个数字因此也是1种


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[n]
