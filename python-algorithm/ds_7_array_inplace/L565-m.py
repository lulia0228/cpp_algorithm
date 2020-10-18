# -*- coding: utf-8 -*-


# 提示：
# N是[1, 20,000]之间的整数。
# A中不含有重复的元素。
# A中的元素大小在[0, N-1]之间。

# 剪枝很重要，否则超时
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 1
        visited = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = 1
                cnt = 1
                nxt = nums[nums[i]]
                while nxt != nums[i]:
                    visited[nxt] = 1
                    cnt += 1
                    nxt = nums[nxt]
                res = max(res, cnt)
        return res

#    更省空间的写法
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 1
        for i in range(len(nums)):
            tmp_len = 0
            idx = i
            while nums[idx] != -1:
                tmp_len += 1
                nxt_idx = nums[idx]
                # 访问过的被标记成-1
                nums[idx] = -1
                idx = nxt_idx
            res = max(res, tmp_len)
        return res