# -*- coding: utf-8 -*-



# 超时
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        cnt = 1  # 2是质数
        for i in range(3, n):
            if i % 2 == 0:
                continue
            else:
                if self.isP(i):
                    cnt += 1
        return cnt

    def isP(self, n):
        # 从3开始是因为传过来的n是奇数
        k = 3
        while k * k <= n:
            if n % k == 0:
                return False
            # 为什么可以加2，因为传过来的不是偶数
            k += 2
        return True

# 埃氏筛
class Solution:
    def countPrimes(self, n: int) -> int:
        """
        求n以内的所有质数个数（纯python代码）
        """
        # 最小的质数是 2
        if n <= 2:
            return 0

        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0   # 0和1不是质数，先排除掉

        # 埃式筛，把不大于根号n的所有质数的倍数剔除,剩下的就是除掉0,1就是不大于n的质数
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

        return sum(isPrime)


aa = [1,5,7,2,3,8,0,12]
print(aa[4:8:2])

