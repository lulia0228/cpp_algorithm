#--coding:utf-8--

# 前缀和+哈希思想

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0:-1}
        res = 0
        cnt = 0
        for idx, itm in enumerate(nums):
            if itm == 0:
                cnt += 1
            else:
                cnt -= 1
            if cnt in dic:
                res = max(res, idx-dic[cnt])
            else:
                dic[cnt] = idx
        return res