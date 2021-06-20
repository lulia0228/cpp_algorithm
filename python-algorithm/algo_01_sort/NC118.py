
#数组中的逆序对

class Solution:
    ans = 0
    def InversePairs(self, nums):
        # write code here
        self.GbSort(nums, 0, len(nums) - 1)
        return self.ans%1000000007

    def GbSort(self, nums, lt, rt):
        if lt >= rt: return
        mid = lt + (rt - lt) // 2
        self.GbSort(nums, lt, mid)
        self.GbSort(nums, mid + 1, rt)
        self.merge(nums, lt, mid, rt)

    def merge(self, nums, left, mid, right):
        tempArray = [0] * (right - left + 1)  # 临时数组
        i, j, k = left, mid + 1, 0
        while i <= mid and j <= right:
            if nums[i] <= nums[j]: # # 说明后半部分数组从mid+1到j-1都是小于nums[i]的
                tempArray[k] = nums[i]
                i += 1
                self.ans += j-mid-1
            else:
                tempArray[k] = nums[j]
                j += 1
            k += 1
        while i <= mid:
            tempArray[k] = nums[i]
            k += 1
            i += 1
            self.ans += (right-mid)
        while j <= right:
            tempArray[k] = nums[j]
            k += 1
            j += 1
        for x in range(k):  # 将排序好的数组放回原来的数组
            nums[left + x] = tempArray[x]