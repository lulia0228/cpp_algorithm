
#include <iostream>
#include <vector>
#include <set>
using namespace std;

//利用set去重 效率很低
class Solution {
private:
    vector<vector<int>> res ;
    vector<bool>  flags;
    set<vector<int>> s;

    void gene_permute(vector<int>& nums , int index, vector<int>&  tem){
        if(index == nums.size()){
            s.insert(tem);
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
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        res.clear();
        if (nums.size() == 0)
            return res;
        flags = vector<bool>(nums.size(), false);
        vector<int> tem;
        gene_permute(nums, 0, tem);
        res = vector<vector<int>> (s.begin(), s.end());
        return res;
    }

};

//优化剪枝 和 L40去重思路一样，先排序
//一开始写剪枝条件的时候：去了一个条件 !flags[i-1] 这个最关键了
class Solution1 {
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
                //去重，最关键 !flags[i-1]
                if(i>0 && nums[i]==nums[i-1]&& !flags[i-1])
                    continue;
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
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        res.clear();
        sort(nums.begin(), nums.end());
        if (nums.size() == 0)
            return res;
        flags = vector<bool>(nums.size(), false);
        vector<int> tem;
        gene_permute(nums, 0, tem);
        return res;
    }

};