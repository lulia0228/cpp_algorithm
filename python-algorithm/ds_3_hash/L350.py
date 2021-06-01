# -*- coding: utf-8 -*-

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        d1 = {}
        for i in nums1:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        for i in nums2:
            if d1.get(i, -1) > 0:
                d1[i] -= 1
                res.append(i)
        return res


# 排序+双指针
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        length1, length2 = len(nums1), len(nums2)
        intersection = list()
        index1 = index2 = 0
        while index1 < length1 and index2 < length2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                intersection.append(nums1[index1])
                index1 += 1
                index2 += 1

        return intersection

