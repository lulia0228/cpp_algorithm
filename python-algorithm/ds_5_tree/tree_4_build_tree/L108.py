# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 19:39
# @Author  : No Name

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.dfs(nums, 0, len(nums) - 1)

    def dfs(self, nums, start, end):
        if start > end:
            return None
        mid = start + (end - start) // 2
        root = TreeNode(nums[mid])
        root.left = self.dfs(nums, start, mid - 1)
        root.right = self.dfs(nums, mid + 1, end)
        return root


