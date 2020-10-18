
#include <iostream>
#include <vector>
using namespace std;

//最大子序列和

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int final_max = nums[0];
        vector<int> dp(nums.size(),0);
        dp[0] = nums[0];
        for(int i=1 ;i<nums.size();i++){
            dp[i] = max(dp[i-1]+nums[i],nums[i]);
            final_max = max(final_max,dp[i]);
        }
        return final_max;
    }
};

//优化空间存储的写法
class Solution1 {
public:
    int maxSubArray(vector<int>& nums) {
        int final_max = nums[0];
        int temp_max = nums[0];
        for(int i=1 ; i<nums.size(); ++i){
            temp_max = max(temp_max+nums[i], nums[i]);
            final_max = max(final_max, temp_max);
        }
        return final_max;
    }
};