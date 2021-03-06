# -*- coding: utf-8 -*-

# 2种思路速度是差不多的；注意的是遍历过的需要在哈希中删除记录

# 思路1 把所有数放到哈希表中，遍历原始数组，找到每个数 左右两边能到达的最大长度，遍历过的从哈希中先删除
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        s = set(nums)
        res = 1
        for i in range(len(nums)):
            tmp_len = 1
            back = nums[i]-1
            future = nums[i]+1
            while back in s:
                tmp_len += 1
                s.remove(back)
                back -= 1
            while future in s:
                tmp_len += 1
                s.remove(future)
                future += 1
            res = max(res, tmp_len)
        return res

# 思路2 最长连续序列的最小值一定是数组中的某个值，那遍历的时候只用分析以这个最小值开头的连续序列就可以了。
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]: return 0
        # 先全部转化成集合
        st = set(nums)
        max_len, start = 1, 0
        for n in nums:
            if n-1 not in st:
                tmp = n
                while tmp in st:
                    st.remove(tmp)
                    tmp += 1
                if tmp-n>max_len:
                    max_len = tmp-n
                    start = n
        return max_len


