
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        long long sum = (n+1)*n/2;
        for(int i=0; i<nums.size(); i++)
            sum -= nums[i];
        return sum;
    }
};

//没出现在序列中的那个数就是 (和总和的差距)


//也可以用位运算解决