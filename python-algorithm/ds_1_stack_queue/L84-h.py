# -*- coding: utf-8 -*-


# 单调递增栈，即出现破坏单调性的元素的时候，找它的上一个元素往起始方向
# 滑动可组成的最大矩形，直到高度≤破坏单调性的元素的高度（即栈恢复单调递增）

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 为了让最两端的元素有可比较值，让它们出栈，两端加2个0
        heights.insert(0, 0)
        heights.append(0)
        stk = []
        ans = 0
        for i in range(len(heights)):
            while stk != [] and heights[stk[-1]]>heights[i]:
                cur_idx = stk.pop(-1)
                # 容易出错，左边界left不能直接使用cur_idx，因为往左可能隔着破坏单调性的元素
                left = stk[-1] + 1
                right_border = i-1
                ans = max(ans, (right_border-left+1)*heights[cur_idx])
            stk.append(i)
        return ans
