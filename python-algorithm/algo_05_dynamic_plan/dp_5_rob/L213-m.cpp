
#include <iostream>
#include <vector>
using namespace std;
class Solution {
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