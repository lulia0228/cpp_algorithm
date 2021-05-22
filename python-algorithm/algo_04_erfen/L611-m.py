#--coding:utf-8--

# 首先对数组排序，a,b,c排序完成后可以保证a+c>b b+c>a 剩下的只需要去关注a+b>c这个关系成立与否。
# 固定最短的两条边，二分查找第一个大于两边之和的位置。可以求得固定两条边长之和满足条件的结果。
# O(n^2logn)

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        sz = len(nums)
        cnt = 0
        for i in range(0, sz-2):
            # if nums[i] == 0: continue
            for j in range(i+1, sz-1):
                t_sum = nums[i] + nums[j]
                lt, rt = j+1, sz-1
                # 数组最右边的值也是小于目标值的
                if nums[rt] < t_sum:
                    cnt += rt - j
                else:
                    # 找到第一个大于目标值的下标
                    while lt < rt:
                        mid = lt +(rt-lt)//2
                        if nums[mid] < t_sum:
                            lt = mid+1
                        else:
                            rt = mid
                    cnt += lt-j-1
        return cnt

# 排序+双指针
# 首先对数组排序。a,b,c排序完成后可以保证a+c>b b+c>a 剩下的只需要去关注a+b>c这个关系成立与否。
# 固定最长的一条边，运用双指针扫描

'''如果 nums[l] + nums[r] > nums[i]，同时说明 
nums[l + 1] + nums[r] > nums[i], ..., nums[r - 1] + nums[r] > nums[i]，
满足的条件的有 r - l 种，r 左移进入下一轮。
如果 nums[l] + nums[r] <= nums[i]，l 右移进入下一轮。'''

# O(n^2)

class Solution1:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        sz = len(nums)
        cnt = 0
        for i in range(sz-1, 1, -1): # 前闭后开
            lt, rt = 0, i-1
            while lt<rt:
                if nums[lt] + nums[rt] > nums[i]:
                    cnt += rt -lt
                    rt -= 1
                else:
                    lt += 1
        return cnt
