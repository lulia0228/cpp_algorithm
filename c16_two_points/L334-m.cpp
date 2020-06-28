//
// Created by LiHeng on 2020/6/28.
//
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int len = nums.size();
        if (len < 3) return false;
        int small = INT_MAX, mid = INT_MAX;
        for (auto num : nums) {
            if (num <= small)
                small = num;
            else if (num <= mid)
                mid = num;
            else if (num > mid)
                return true;
        }
        return false;
    }

};

//算是双指针+贪心算法吧
//有一点要想明白，当下次更新完small时候，small对应的索引不是小于当前mid的索引吗？
//别忘了这里隐藏事实，就算下次出现大于mid值的时候，更新small之前的那个small是介于
//当前的small和mid之间的，那依然可以构成上升子序列