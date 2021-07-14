# -*- coding: utf-8 -*-

'''
所有可能的情况
1.该数只能被a整除 (该数一定是a 的整数倍)
2.该数只能被b整除 (该数一定是b 的整数倍)
3.该数只能被c整除 (该数一定是c 的整数倍)
4.该数只能被a和b同时整除 (该数一定是a、b最小公倍数的整数倍)
5.该数只能被a和c同时整除 (该数一定是a、c最小公倍数的整数倍)
6.该数只能被b和c同时整除 (该数一定是b、c最小公倍数的整数倍)
7.该数只能被a和b和c同时整除（该数一定是a、b、c的最小公倍数的整数倍）
'''
# 同leetcode 878 被2个数整除 这里是848的升级版本 被3个数整除

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        l_ab, l_ac, l_bc = self.LCM(a,b), self.LCM(a,c), self.LCM(b,c)
        l_abc = self.LCM(l_ab, c)
        low = min(min(a,b),c)  # 下边界显然是a、b、c中最小者
        high = low*n
        while low<high:
            mid = low+(high-low)//2
            # 计算小于等于mid的丑数个数
            cnt = mid//a+mid//b+mid//c-mid//l_ab-mid//l_ac-mid//l_bc+mid//l_abc
            if cnt<n:
                low = mid + 1
            else:
                high = mid
        return low

    # 求最小公倍数
    def LCM(self, A, B):
        # 求最大公约数
        def GCD(a, b):
            while b:
                tmp = a%b
                a = b
                b = tmp
            return a
        return A*B/GCD(A, B)
