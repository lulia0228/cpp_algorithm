
#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();

        int total_tank = 0;
        int curr_tank = 0;
        int starting_station = 0;

        for (int i = 0; i < n; ++i) {
            total_tank += gas[i] - cost[i];
            curr_tank += gas[i] - cost[i];
            // If one couldn't get here,
            if (curr_tank < 0) {
                // Pick up the next station as the starting one.
                starting_station = i + 1; //仔细想一想这里
                // Start with an empty tank.
                curr_tank = 0;
            }
        }
        return total_tank >= 0 ? starting_station : -1;
    }
};
//对于当前gas[i] - cost[i]<0 那当前不能做起始位置，因为当前可加的油不够开到下一站
//如果到某个位置，累加gas[i] - cost[i]还是＜0;那起始位置只能变下一个，
//因为即使起始位置在前面重新选择也会导致累加<0(这点要想明白)