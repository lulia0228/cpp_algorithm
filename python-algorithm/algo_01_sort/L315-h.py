#--coding:utf-8--
'''
@Time   : 2020/8/4
@Author : Heng Li
@Email  : liheng@elensdata.com
'''

# 1 暴力法 2层循环
class Solution:
    def countSmaller(self, nums: list) -> list:
        lenth = len(nums)
        res = []
        for i in range(lenth):
            cnt = 0
            for j in range(i+1, lenth):
                if nums[j]<nums[i]:
                    cnt += 1
            res.append(cnt)
        return res


# 2 借助归并排序
class Solution1:
    def __init__(self):
        self.res = []

    def countSmaller(self, nums) :
        info = []
        lenth = len(nums)
        self.res = [0 for i in range(lenth)]
        for i in range(lenth):
            info.append((nums[i], i))
        self.gb_sort(info, 0, lenth - 1)
        return self.res

    def gb_sort(self, nums, left, right):
        if left >= right:
            return;
        mid = left + (right - left) // 2;
        self.gb_sort(nums, left, mid);
        self.gb_sort(nums, mid + 1, right);
        self.merge(nums, left, mid, right);

    def merge(self, nums, left, mid, right):
        i = left
        j = mid + 1
        tmp_nums = []
        while i <= mid and j <= right:
            if nums[i][0] <= nums[j][0]:
                self.res[nums[i][1]] += j - mid - 1
                tmp_nums.append(nums[i])
                i += 1
            else:
                tmp_nums.append(nums[j])
                j += 1

        # while i<= mid:
        #     self.res[nums[i][1]] += j - mid - 1
        #     tmp_nums.append(nums[i])
        #     i += 1
        # while j<=right:
        #     tmp_nums.append(nums[j])
        #     j += 1

        if j == right+1:
            for k in range(i, mid+1):
                self.res[nums[k][1]] += j-mid-1
                tmp_nums.append(nums[k])
        else:
            for h in range(j, right+1):
                tmp_nums.append(nums[h])

        m = 0
        n = left
        while m < len(tmp_nums):
            nums[n] = tmp_nums[m]  # 每次小合并后在原数组上相应位置赋值
            n += 1
            m += 1
        # print(nums)


a = [5,2,6,1]
print(Solution1().countSmaller(a))