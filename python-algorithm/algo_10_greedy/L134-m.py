# -*- coding: utf-8 -*-


# 环形加油站
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_tank = 0;
        curr_tank = 0;
        starting_station = 0;

        for i in range(n):
            total_tank += gas[i] - cost[i];
            curr_tank += gas[i] - cost[i];
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1  # 仔细想一想这里
                # Start with an empty tank.
                curr_tank = 0

        return starting_station if total_tank >= 0 else  -1