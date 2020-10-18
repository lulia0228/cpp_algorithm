

//leetcode 300 最长上升子序列问题
//DP时间复杂度O(n*n)

#include <iostream>
#include <vector>

using namespace std ;
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if(nums.size() == 0)
            return 0;
        int maxL = 1;
        //memo[i] 表示 以nums[i] 结尾的最长上升子序列的长度
        vector<int> memo(nums.size(), 1) ;
        for(int i = 1 ; i < nums.size() ; i ++){
            for(int j = 0 ; j < i ; j ++){
                if(nums[i] > nums[j])
                    memo[i] = max(memo[i] , 1 + memo[j]);
            }
            maxL = max(maxL,memo[i]);
        }
        return maxL;
    }
};

int main(){
    //int arry[] = {1, 7 , 3 , 5 , 9 , 4 , 8};
    int arry[] = {10,9,2,5,3,7,101,18};
    vector<int> nums(arry ,  arry + 7);
    cout << Solution().lengthOfLIS(nums) ;
}

// 做题体会！！！
// 有一类问题的写法，包括双指针，dp,滑动窗口，都是以当前遍历到的元素i作为一个考察点，
// 然后从0向后遍历到i或者从i往前倒着走来解决问题


//这道题还有一种nlogn的解法，还没做,不太好理解贪心+二分查找


