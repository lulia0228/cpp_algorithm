# -*- coding: utf-8 -*-

# 这道题很难

# 从10叉前缀树前序遍历的角度去理解；不过这里无需建树
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        prefix = 1
        pos = 1
        while pos < k:
            cnt = self.get_count(prefix, n)
            if pos+cnt > k:
                prefix *= 10 # 前缀后推1位，注意和前缀+1的区别
                pos += 1
            else:
                prefix += 1  # 前缀自身+1
                pos += cnt
        return prefix

    # 计算以prefix为前缀的数字个数，且小于指定数字范围n
    def get_count(self, prefix, n):
        cnt = 0
        a, b = prefix, prefix+1
        while a <= n:
            cnt += min(n+1, b)-a
            a *= 10
            b *= 10
        return cnt
