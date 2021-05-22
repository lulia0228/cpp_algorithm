#--coding:utf-8--
# 同余定理
'''令 P[i] = A[0] + A[1] + ... + A[i]P[i]=A[0]+A[1]+...+A[i]。
那么每个连续子数组的和 sum(i,j) 就可以写成 P[j]−P[i−1]（其中0<i<j）的形式。
此时，判断子数组的和能否被 K 整除就等价于判断(P[j]−P[i−1])modK==0，
根据 同余定理，只要P[j]modK==P[i−1]modK，就可以保证上面的等式成立'''


# 初始化record[0]=1，就可以考虑了前缀和本身被可以被K整除的情况

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        record = {0: 1}
        total, ans = 0, 0
        for elem in A:
            total += elem
            modulus = total % K
            same = record.get(modulus, 0)
            ans += same
            record[modulus] = same + 1
        return ans


