
// 状态转移方程 dp[i]表示抢劫nums[0,..,i]所能获得的最大收益
// dp[i] = max(dp[i-1], dp[i-2]+nums[i])
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n==0)
            return 0;
        vector<int> dp(n,0) ;
        dp[0] = nums[0];
        for(int i=1; i<n; ++i)
            dp[i] = max(dp[i-1], nums[i]+(i-2>=0 ? dp[i-2]:0));
        return dp[n-1];
    }
};

//优化了空间存储,学学空间是怎么优化的？
class Solution1 {
public:
    int rob(vector<int>& nums) {
        /*
        动态转移方程是：
        f(n)=max(nums[n]+f(n-2),f(n-1))
        prevMax:f(k-2)
        currMax:f(k-1)
        x:Ak
        */
        int prevMax = 0;
        int currMax = 0;
        for(int i=0; i<nums.size(); ++i){
            int temp = currMax;
            currMax = max(nums[i]+prevMax, currMax);
            prevMax = temp;
        }
        return currMax;
    }

};

//此题变种 L213房子变成环形排列
//解法：第一个和最后一个相连  拆成2个子问题
// （1）不抢劫第一个房子 问题变成了对nums[1:n]使用198的解法
// （2）抢劫第一个房子 问题变成了对nums[0:n-1]使用198的解法
// 看（1）（2）哪个大？

class Solution_ {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n==0) return 0;
        if(n == 1) return nums[0];
        int Max1 = rob1(nums,0,n-1);//不偷窃最后一个房子
        int Max2 = rob1(nums,1,n);//不偷窃第一个房子
        return max(Max1,Max2);
    }

    int rob1(vector<int>& nums,int start,int end){
        /*
        动态转移方程是：
        f(n)=max(nums[n]+f(n-2),f(n-1))
        prevMax:f(k-2)
        currMax:f(k-1)
        x:Ak
        */
        int prevMax = 0;
        int currMax = 0;
        for(int i=start;i<end;i++){
            int temp = currMax;
            currMax = max(nums[i]+prevMax, currMax);
            prevMax = temp;
        }
        return currMax;
    }
};