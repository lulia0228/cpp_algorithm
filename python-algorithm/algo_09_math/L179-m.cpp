//
// Created by LiHeng on 2020/6/30.
//
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
class Solution {
public:
    string largestNumber(vector<int>& nums) {
        string res;
        sort(nums.begin(), nums.end(), cmp);
        for (int i = 0; i < nums.size(); ++i) {
            res += to_string(nums[i]);
        }
        if (res[0] == '0') {
            res = '0';
        }
        return res;
    }

    static bool cmp(const int &a, const int &b) {
        string s1 = to_string(a) + to_string(b);
        string s2 = to_string(b) + to_string(a);
        return s1 > s2;
    }
};

// 自定义了一个比较函数，c++ stl sort 自定义比较函数必须是静态
// 对于2个数字a,b合在一起谁大 就看ab和ba谁大 如果ab>ba 那就认为排序时候a>b a排在前面