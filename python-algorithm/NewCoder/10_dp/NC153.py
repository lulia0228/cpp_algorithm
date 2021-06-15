#--coding:utf-8--

class Solution:
    def maxLetters(self, letters):
        # write code here
        if not letters:
            return 0

        n = len(letters)
        # 相当于固定了第一维度求最长上升子序列
        # 这里第二维度降序排列的原因，是为了避免第一维度出现相同值的时候，会被塞进去
        letters.sort(key=lambda x: (x[0], -x[1]))

        # 对第二维度求最长上升子序列
        f = [1] * n
        for i in range(n):
            for j in range(i):
                if letters[j][1] < letters[i][1]:
                    f[i] = max(f[i], f[j] + 1)
        return max(f)

# 另一种方法是基于二分查找的动态规划；lc354官方题解
