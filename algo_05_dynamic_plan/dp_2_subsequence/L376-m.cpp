
#include <iostream>
#include <vector>

using namespace std ;
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int sz = nums.size();
        if (sz == 0)
            return 0;
        //原理：不停的更新序列长度，连续出现上升的时候只在down上加1，同理连续出现下降只在up上累加
        int up = 1, down = 1;
        for (int i = 1; i < sz; i++) {
            if (nums[i] > nums[i - 1]) {
                up = down + 1;
            } else if (nums[i] < nums[i - 1]) {
                down = up + 1;
            }
        }
        return max(up, down);
    }
};