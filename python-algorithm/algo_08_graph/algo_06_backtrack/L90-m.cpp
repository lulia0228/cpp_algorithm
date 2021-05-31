
#include <iostream>
#include <vector>
using namespace std;

//方法1 子集78的做法 然后用set去重
//方法2 先排序，然后利用40 47 类似的方法去重

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        auto res = vector<vector<int>> ();
        sort(nums.begin(), nums.end());
        vector<int> tmp;
        backtrack(res, tmp, nums, 0);
        return res;
    }
    //注意在循环内部写递归语句是怎么运行的？另外，注意list.push_back(tempL)所处位置，带来的结果的顺序变动，有助于理解过程
    void backtrack(vector<vector<int>>& list ,vector<int>& tempL, vector<int>& nums,int start){
        list.push_back(tempL); //[[],[1],[1,2],[1,2,2],[2],[2,2]]
        for(int i=start ;i <nums.size();i++){//注意是i=start 不能i=0
            //很重要的去重
            if(i!=start && nums[i]==nums[i-1])
                continue;
            tempL.push_back(nums[i]);
            backtrack(list,tempL,nums,i+1);
            tempL.pop_back();
        }
        //list.push_back(tempL); //[[1,2,2],[1,2],[1],[2,2],[2],[]]
    }
};

//[1,2,3]