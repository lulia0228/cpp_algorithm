#--coding:utf-8--

# 单调栈+二分


# (1)记录数组每个时候最小值作为1 及其隐藏下标i
# (2)倒序遍历，符合大于当前1的值可作为3 可保证j>i
# (3)保持单调栈，在已经入栈的元素中 寻找2 可保证k>i
# (4)如果寻找的2满足2<3即找到了 且有k>j

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        sz = len(nums)
        if sz < 3: return False
        stk = []
        # 当前位置最小的值
        cur_min = [nums[i] for i in range(sz)]
        for i in range(1, sz):
            cur_min[i] = min(cur_min[i - 1], nums[i])
        # 倒序遍历
        for j in range(sz - 1, -1, -1):
            # 保证3>1 且 3的下标j大于1(cur_min[j])在原数组的下标i
            if nums[j] > cur_min[j]:
                # 寻找2 保证2>1 且 2(stk[-1])在原数组的下标k大于1(cur_min[j])在原数组的下标i
                while stk != [] and stk[-1] <= cur_min[j]:
                    stk.pop()
                # 存在2<3 且 2(stk[-1])在原数组的下标k大于3的下标j
                if stk != [] and stk[-1] < nums[j]:
                    return True
                stk.append(nums[j])
        return False