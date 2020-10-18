

// 在出现 nums[i]<nums[i-1] 时，需要考虑的是应该修改数组的哪个数，使得本次修改能使 i 之前的数组成为非递减数组，并且 不影响后续的操作
// 优先考虑令 nums[i-1] = nums[i]，因为如果修改nums[i] = nums[i-1]的话，那么nums[i]这个数会变大就有可能比nums[i+1] 大，
// 特殊情况：nums[i]<nums[i-1]&&nums[i]<nums[i-2]，修改 nums[i-1]=nums[i] 不能使数组成为非递减数组，只能修改 nums[i]=nums[i-1]。

#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int cnt = 0;
        //cnt<2起到剪枝作用，可以不要
        for (int i = 1; i < nums.size() && cnt < 2; i++) {
            if (nums[i] >= nums[i - 1]) {
                continue;
            }
            cnt++;
            if (i - 2 >= 0 && nums[i - 2] > nums[i]) {
                nums[i] = nums[i - 1];
            } else {
                nums[i - 1] = nums[i];
            }
        }
        return cnt <= 1;
    }
};