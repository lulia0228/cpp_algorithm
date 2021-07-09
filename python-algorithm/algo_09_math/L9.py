# -*- coding: utf-8 -*-

# 为了防止有些语言的溢出，这里只反转一半数字
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        m = x
        cnt = 0
        # 求出x有多少位
        while m:
            m = m//10
            cnt += 1
        n = x
        k = 0
        # 反转整数的一半
        for _ in range(cnt//2):
            k = k*10 + n%10
            n //= 10
        if cnt&1:
            return n//10 == k
        else:
            return n==k


