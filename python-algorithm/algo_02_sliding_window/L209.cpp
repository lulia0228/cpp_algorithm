

//leetcode 在整型数组中找到一个最短的连续子数组，使其元素和>=s

#include <iostream>
#include <vector>
using namespace std;

//以下写法算是双指针思想
class Solution{
public:
    int minSubArrayLen(int s, vector<int>&  nums){
        int l = 0, r = -1;
        int sum = 0;
        int res = nums.size() + 1;
        while (l < nums.size()){
            if (r+1 < nums.size() && sum < s)
                sum += nums[++r]; //最关键的点，r从-1开始，然后使用了++r。我一开始r=0,下面使用r++就写不出来
            else
                sum -= nums[l++];
            if (sum >= s)
                res = min(res, r-l+1);
        }
        return res>nums.size()? 0:res;
    }
};

//下面这个是我的写法，就当做是滑动窗口思路，本身滑动窗口和双指针就很像。
class Solution1 {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int lt = 0;
        int sum = 0;
        int len = nums.size() + 1;
        for(int rt=0; rt<nums.size(); ++rt){
            sum += nums[rt];
            while(sum >= s && lt<=rt){
                len = min(len, rt-lt+1);
                sum -= nums[lt]; //先减去当前左边界值，再更新左边界
                ++lt;
            }
        }
        return len>nums.size()? 0:len;
    }
};

int main(){
    vector<int> arr = {2, 3, 1, 2, 4, 3};
    Solution sample = Solution();
    int p = sample.minSubArrayLen(7, arr);
    cout << p;
}