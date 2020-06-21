//
// Created by LiHeng on 2020/6/21.
//

// 给定非负整数数组，要求用“+”“-”随意组合数组元素 使它们的和为S
// 转化成了0-1背包问题变种

//转化思路：假如添加+的是正子集A  添加-的是负子集B
// sum(A) - sum(B) =  S
// sum(A) + sum(B) =  Sum
// sum(A) = (S+Sum)/2  因此S+Sum必须是偶数 而且Sum必须大于等于S

//因此问题就转化成了用数组来填充容量(S+Sum)/2有多少种组合？ 注意和L416对比下
#include <iostream>
#include <vector>
using namespace std ;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int sum = 0;
        for (int i = 0; i < nums.size(); i++)
            sum += nums[i];
        if (sum < S || (sum + S) % 2 != 0)
            return 0;
        int target = (S + sum) / 2;
        vector<int> dp(target+1, 0) ;
        dp[0] = 1;

        //假如给定nums = [num1,num2,num3]，则有dp[j] = dp[j-num1] + dp[j-num2] + dp[j-num3].
        //经过转化后，题目就变成了在数组num中选择一个子集使它们的和为target。看着有点像硬币找零组合数，不过不是，区别在于
        //这里每个元素只能使用1次，硬币找零的时候，每种硬币使用次数无限制
        for (int i = 0; i < nums.size(); i++) {
            //倒着设计可以避免元素被重复使用
            for (int j = target; j >= nums[i]; j--) {
                dp[j] += dp[j-nums[i]];
            }

        }
        return dp[target];
    }
};


//换一种思路更直接，也是DP思想
//dp[i][j]表示用nums的前i个元素组成j的方法数
//dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j+nums[i]] 即第i个元素可以是+,可以是-
//这种做法要考虑的太多了, j的边界是[-sum,sum]