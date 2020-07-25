//
// Created by LiHeng on 2020/6/21.
//

// 很简单求子数组num[i:j]之和，题目要求多次调用，因此生成了一个累加数组

#include <iostream>
#include <vector>

using namespace std ;
class NumArray {
public:
    vector<int> S;
    NumArray(vector<int>& nums) {
        S.push_back(0);
        int sum = 0 ;
        for(int i=0; i<nums.size(); ++i){
            sum += nums[i];
            S.push_back(sum);
        }
    }

    int sumRange(int i, int j) {
        return S[j+1]-S[i];
    }
};

