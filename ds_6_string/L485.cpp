//
// Created by 李恒 on 2020/7/1.
//
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int res = 0;
        int tmp = 0;
        for(int i=0; i<nums.size(); ++i){
            if(nums[i] == 0){
                res = max(res, tmp);
                tmp = 0;
            }
            else
                ++tmp;
        }
        return max(res, tmp); //不是以0结尾的时候最后一次tmp要额外处理
    }
};


class Solution1 {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int res = 0;
        int tmp = 0;
        for(int i=0; i<nums.size(); ++i){
            if(nums[i] == 0)
                tmp = 0;
            else
                ++tmp;
            res = max(res, tmp);
        }
        return res;
    }
};