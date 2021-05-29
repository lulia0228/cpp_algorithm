#--coding:utf-8--
'''使用双指针维护这些区间，每次右指针右移，如果区间仍然满足条件，那么左指针不移动，
否则左指针至多右移一格，保证区间长度不减小（这样即使新区间内非连续字符个数大于K，该区间也不会对最终结果造成贡献）'''

# 这道滑动窗口和之前的通用滑动窗口做法不太一样
# 维护的是区间内历史最大的字符出现长度；不太好理解

# 这道题的重点在于是平移而不是缩小窗口;而且是带上maxn的平移
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        num = [0] * 26
        n = len(s)
        maxn = left = right = 0

        while right < n:
            num[ord(s[right]) - ord("A")] += 1
            maxn = max(maxn, num[ord(s[right]) - ord("A")])
            if right - left + 1 - maxn > k:
                num[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1

        return right - left
