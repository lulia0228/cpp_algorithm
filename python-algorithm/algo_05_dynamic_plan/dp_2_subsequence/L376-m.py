#--coding:utf-8--


# up[i]   记录的是遍历到第i个元时候的最长上升摆动序列的长度(先上升后下降)
# down[i] 记录的是遍历到第i个元素结尾的最长下降摆动序列的长度(先下降后上升)

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        sz = len(nums)
        if sz == 0:
            return 0
        # 原理：不停的更新序列长度，连续出现上升的时候只在down上加1，同理连续出现下降只在up上累加
        up = [1]*sz
        down = [1]*sz
        for i in range(1, sz):
            if nums[i] > nums[i - 1]: # 说明上一个元素是下降的
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i] < nums[i - 1]: # 说明上一个元素是上升的
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
            else:
                up[i] = up[i-1]
                down[i] =  down[i-1]
        return max(up[sz-1], down[sz-1])


# 优化空间复杂度
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        sz = len(nums)
        if sz == 0:
            return 0
        # 原理：不停的更新序列长度，连续出现上升的时候只在down上加1，同理连续出现下降只在up上累加
        up = 1
        down = 1
        for i in range(1, sz):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)