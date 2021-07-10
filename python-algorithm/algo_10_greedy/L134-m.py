# -*- coding: utf-8 -*-

# 暴力模拟
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sz = len(gas)
        for i in range(sz):
            if self.canBack(gas, cost, i):
                return i
        return -1

    def canBack(self, gas, cost, i):
        start_volume = 0
        for k in range(len(gas)-i):
            j = (i+k)%len(gas)
            arrive_volume = start_volume+gas[j]-cost[j]
            if arrive_volume<0:
                return False
            start_volume = arrive_volume
        return True

# 2 贪心算法 速度快一些
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_tank = 0  # 标记能否完成一圈循环
        curr_tank = 0 # 标记以当前起点开始能否完成一圈循环
        starting_station = 0

        for i in range(n):
            total_tank += gas[i] - cost[i];
            curr_tank += gas[i] - cost[i];
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0

        return starting_station if total_tank >= 0 else  -1