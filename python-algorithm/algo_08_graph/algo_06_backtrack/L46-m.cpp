
//带循环的递归，注意皇后问题51和全排列46、组合77这3道题目问题对比

//全排列----给定一个 没有重复 数字的序列，返回其所有可能的全排列

#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    vector<vector<int>> res ;
    vector<bool>  flags;

    void gene_permute(vector<int>& nums , int index, vector<int>&  tem){
        if(index == nums.size()){
            res.push_back(tem);
            return; //递归退出条件
        }
        for(int i=0; i < nums.size(); i++){
            if (!flags[i]){
                tem.push_back(nums[i]);
                flags[i] = true;
                gene_permute(nums, index+1, tem);
                tem.pop_back();
                flags[i] = false;
            }
        }
        return;
    }

public:
    vector<vector<int>> permute(vector<int>& nums) {
        res.clear();
        if (nums.size() == 0)
            return res;
        flags = vector<bool>(nums.size(), false);
        vector<int> tem;
        gene_permute(nums, 0, tem);
        return res;
    }

};