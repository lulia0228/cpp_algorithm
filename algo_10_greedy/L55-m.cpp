//
// Created by LiHeng on 2020/4/22.
//

//跳跃游戏
#include <iostream>
#include <vector>
using namespace std;

//贪心算法
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int k = 0;
        for(int i=0;i<nums.size()&&k<nums.size()-1;i++){
            if(i>k) return false;
            k = max(k,i+nums[i]);
        }
        return true;
    }
};

//我写的贪心
class Solution1 {
public:
    bool canJump(vector<int>& nums) {
        int available_step = nums[0];
        //available_step<nums.size()-1起到剪枝作用
        for(int i=1; i<nums.size()&&available_step<nums.size()-1; ++i){
            if (available_step < i)
                return false;
            if (nums[i]+i > available_step)
                available_step = nums[i]+i;
        }
        return true;
    }
};

//这道题好像也可以用动态规划做
class Solution2 {
public:
    bool canJump(vector<int>& nums) {
        int sz = nums.size();
        if(sz == 0)
            return true;
        vector<bool> dp(sz, false);
        dp[0] = true;
        //状态转移方程
        for(int i = 0; i < sz; i++) {
            for(int k = i - 1; k >= 0; k--) {  //从后往前，可以减低复杂度
                if(dp[k] == true && k + nums[k] >= i) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[sz - 1];
    }
};
