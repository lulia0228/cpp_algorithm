

// 这道题标记的是easy,我感觉有点难
// 最短无序子序列

#include <iostream>
#include <vector>
using namespace std;

//优秀，高效
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        //此解法参考英文官方LeetCode上的讨论
        //从左到右扫描（或从右到左）找局部极大值（或局部极小值），若位置放置不正确，找到其应该存在的地方
        int n = nums.size();
        //赋初始开始和结束值
        int start = -1;
        int end = -2;
        //结束值赋为-2是考虑在数组本身就是有序时,return也可以给出正确值
        int min_val = nums[n - 1];
        int max_val = nums[0];
        for(int i = 0, pos = 0; i < n; i++) {
            pos = n - 1 - i;
            //找出局部极大、极小值
            max_val = max(max_val, nums[i]);
            min_val = min(min_val, nums[pos]);
            //如果当前值小于局部极大值，用end记录该位置，找到该max_val的合适位置，
            if(nums[i] < max_val)
                end = i;
            //如果当前值大于局部极小值，用star记录该位置，找到该star的合适位置
            if(nums[pos] > min_val)
                start = pos;
        }
        //返回开始和结束的索引差
        return end - start + 1;
    }
};

