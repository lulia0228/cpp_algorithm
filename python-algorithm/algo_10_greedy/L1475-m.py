#--coding:utf-8--

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        cnt = 0
        max_turned_on = -float("inf")
        for idx, bulb in enumerate(light):
            max_turned_on = max(max_turned_on, bulb)
            if idx+1 == max_turned_on:
                cnt += 1
        return cnt
