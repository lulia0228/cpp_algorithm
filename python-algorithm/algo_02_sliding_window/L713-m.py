# -*- coding: utf-8 -*-

# 方法1 滑动窗口
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = right = 0
        while right < len(nums):
            prod *= nums[right]
            while prod >= k:
                prod //= nums[left]
                left += 1
            # print(left, right)
            ans += right - left + 1
            right += 1
        return ans


# 方法2 二分法
'''
bisect.bisect(a, x, lo=0, hi=len(a))：
在有序列表 a 中查找 x 的位置，并且返回其 索引 (index)，使得插入 x 后序列依然保持有序
返回值把列表分成两部分，插入点左侧满足all(val <= x for val in a[lo:i+1])，
插入点右侧满足all(val > x for val in a[i+1:hi])
bisect 函数是 bisect_right 函数的别名，返回的索引是原序列相等元素之后的位置，即新元素插入在旧元素的右边
bisect_left 函数返回的索引是原序列中相等元素的位置，新元素插入在旧元素的左边
'''
# 取对数是为了避免整数乘积溢出
# 前缀和存储的是子数组乘积的对数；因为是递增的，因此可以对前缀和数组使用二分查找
# 二分查找是对每个前缀和数组左侧端点i寻找最大的右端点j满足num[i+1:j]的子数组乘积小于k

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k == 0: return 0
        k = math.log(k)

        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + math.log(x))

        ans = 0
        for i, x in enumerate(prefix):
            # j指的是x + k-1e-9插入prefix后它本身的索引
            j = bisect.bisect(prefix, x + k-1e-9 , i+1)

            ans += (j-1)-(i+1)+1
        return ans



