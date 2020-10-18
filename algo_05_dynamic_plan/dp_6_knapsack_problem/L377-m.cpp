
//注意 322：最少找零硬币数 377：组合总数 518：硬币找零组合种类 这三道题的区别
//注意区别 377 和 39 两个组合总和，377不同顺序视为不同组合，39不考虑顺序
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