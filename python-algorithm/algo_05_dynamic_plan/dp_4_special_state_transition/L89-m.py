#--coding:utf-8--


# 由n位推导n+1位结果时，n+1位结果包含n位结果，同时包含n位结果中在高位再增加一个位1所形成的另一半结果，
# 但是为了保证格雷编码要求的2个连续数值只能有一个二进制位不一样，需要这一半结果和前一半结果镜像排列，即倒过来。
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n+1):
            add = 1<<(i-1)
            for j in range(len(res)-1, -1, -1):
                res.append(add + res[j])
        return res