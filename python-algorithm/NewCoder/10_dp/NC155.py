#--coding:utf-8--


# 有点山脉数组的意思

# 思路：求出以i下标起始和结束的递增数列长度，然后，若i-1与i的值差值大于2，则可以拼接长度

class Solution:
    def maxSubArrayLength(self , nums ):
        n = len(nums)
        # 以 tail[i] 结尾的 最长连续上升子序列
        tail = [0] * n
        # 以 head[i] 开始的 最长连续上升子序列
        head = [0] * n
        tail[0] = 1
        # 最左向右 找出 连续的子序列
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                tail[i] = tail[i - 1] + 1
            else:
                tail[i] = 1
        head[n - 1] = 1
        # 从右向左 找出 连续的子系列
        for i in range(n - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                head[i] = head[i + 1] + 1
            else:
                head[i] = 1
        # 最终结果
        res = 1
        for i in range(1, n - 1):
            # 串联不起来的时候，取一下最大值
            res = max(tail[i], head[i], res)
            # 说明nums[i]可以被替换从而使得tail[i - 1]和head[i + 1]可以被串联起来
            if nums[i + 1] - nums[i - 1] >= 2:
                res = max(res, head[i + 1] + tail[i - 1] + 1)
        return res