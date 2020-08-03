//
// Created by 李恒 on 2020/1/9.
//

//子集-----给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        auto res = vector<vector<int>> ();
        vector<int> tmp;
        backtrack(res, tmp, nums, 0);
        return res;
    }
    //注意在循环内部写递归语句是怎么运行的？另外，注意list.push_back(tempL)所处位置，带来的结果的顺序变动，有助于理解过程
    void backtrack(vector<vector<int>>& list ,vector<int>& tempL, vector<int>& nums,int start){
        list.push_back(tempL); //[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
        for(int i=start ;i <nums.size();i++){//注意是i=start 不能i=0
            tempL.push_back(nums[i]);
            backtrack(list,tempL,nums,i+1);
            tempL.pop_back();
        }
        //list.push_back(tempL); //[[1,2,3],[1,2],[1,3],[1],[2,3],[2],[3],[]]
    }
};

// [] [1] [1 2] [1 2 3] [1 3]
// [2] [2 3]
// [3]