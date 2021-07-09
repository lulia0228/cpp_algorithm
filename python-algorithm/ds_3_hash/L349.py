# -*- coding: utf-8 -*-

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        r_d = {k: 0 for k in nums1}
        for n in nums2:
            if n in r_d:
                res.append(n)
                del r_d[n]
        return res

    # # 考虑相同元素的写法
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     res = []
    #     r_d = collections.defaultdict(int)
    #     for n in nums1:
    #         r_d[n] += 1
    #     for n in nums2:
    #         if n in r_d and r_d[n]>0:
    #             res.append(n)
    #             r_d[n] -= 1
    #     return res


# 其它方法
# 先排序，排序后对2个数组用双指针遍历
