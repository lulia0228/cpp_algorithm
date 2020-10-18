# -*- coding: utf-8 -*-


# 这道题告诉我们，有时候要活用数组元素和它们的索引之间的关系
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # 当遍历到第i个位置时，如果可以切分为块，那前i个位置的最大值一定等于i。
        # 否则，一定有比i小的数划分到后面的块，那块排序后，一定不满足升序。
        sz = len(arr)
        if sz==0 :
            return 0;
        cursor = arr[0];
        res = 0;
        for i in range(sz):
            cursor = max(cursor, arr[i])
            if cursor == i:
                res += 1
        return res
