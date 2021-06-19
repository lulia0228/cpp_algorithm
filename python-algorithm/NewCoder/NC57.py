
class Solution:
    def reverse(self, x):
        # write code here
        flag = False
        m = x
        if x < 0:
            m = -x
            flag = True
        sum_ = 0
        while m:
            last = m % 10
            m = m // 10
            if sum_ > pow(2, 31) // 10 or (sum_ == pow(2, 31) and last > 7 and not flag) \
            or (sum_ == pow(2, 31) and last > 8 and flag):
                return 0
            sum_ = sum_ * 10 + last
        if flag:
            return -sum_
        return sum_
