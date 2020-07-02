//
// Created by 李恒 on 2020/7/2.
//
//循环数组中比当前元素大的下一个元素
//与 739. Daily Temperatures (Medium) 不同的是，数组是循环数组，并且最后要求的不是距离而是下一个元素。
#include <iostream>
#include <vector>
#include <stack>

using namespace std;
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> next(n,-1);
        stack<int> pre; //存的是索引，栈中索引对应的元素构成的序列值永远是递减的
        for (int i = 0; i < n*2; i++) {
            int num = nums[i%n];
            while (!pre.empty() && nums[pre.top()]<num) {
                next[pre.top()] = num;
                pre.pop();
            }
            if (i < n){
                pre.push(i);
            }
        }
        return next;
    }
};