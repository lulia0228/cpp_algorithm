#--coding:utf-8--

# 单调栈
# O(n) O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = list()
        n = len(height)

        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)

        return ans


# 计算并存储每个位置两边的最大高度
# O(n) O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans


# 升级
# O(n) O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        sz = len(height)
        if sz < 3:
            return 0
        left, right = 0, sz-1
        l_max, r_max = height[0], height[sz-1]
        res = 0
        while left <= right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            if l_max <= r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        return res

