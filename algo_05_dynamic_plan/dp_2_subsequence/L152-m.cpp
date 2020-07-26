//
// Created by LiHeng on 2020/6/3.
//

#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int sz = nums.size();
        int tmp_max = nums[0];
        int tmp_min = nums[0];
        int final_max = nums[0];
        for(int i=1; i<sz; ++i){
            //考虑到负数的情况，每一步都要保存最大正值和最小负值
            //先把上一步的最大值保存下来，防止下面被修改掉
            int tmp = tmp_max;
            tmp_max = max(max(tmp_max*nums[i], tmp_min*nums[i]), nums[i]);
            tmp_min = min(min(tmp*nums[i], tmp_min*nums[i]), nums[i]);
            final_max = max(final_max, tmp_max);
        }
        return final_max;
    }
};