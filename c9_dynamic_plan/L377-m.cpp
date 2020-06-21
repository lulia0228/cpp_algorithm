//
// Created by LiHeng on 2020/6/21.
//

#include <iostream>
#include <vector>
using namespace std;

//这个题目和硬币找0很像，区别是硬币找0的组合元素不考虑顺序，这里不同顺序算不同的组合
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<int> dp(target+1, 0);
        dp[0] = 1;
        for (int i=1; i<=target; ++i) {
            for (auto n:nums) {
                if(i>=n && dp[i-n]!=0 )
                    dp[i] = (dp[i]>=INT_MAX-dp[i-n]) ? INT_MAX : dp[i]+dp[i-n]; //用long long 还是会溢出 这里没办法
            }
        }
        return dp[target];
    }

};