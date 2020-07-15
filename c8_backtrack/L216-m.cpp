//
// Created by 李恒 on 2020/7/9.
//

//这道题和 L39 L40题 比较相似；区别是这道题真能下探k层

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> candidates = {1,2,3,4,5,6,7,8,9};
    vector<vector<int>> res;
    vector<vector<int>> combinationSum3(int k, int n){
        vector<int> c;
        getCombination(k, n, 0, 0, c);
        return res;
    }
    void getCombination(int k, int n, int count, int idx, vector<int>& c){
        if(count == k){
            if(n == 0)
                res.push_back(c);
            return;
        }
        for(int i=idx; i<candidates.size(); ++i){
            //剪枝，因为1~9是单调递增的
            if (n-candidates[i] < 0)
                break;
            c.push_back(candidates[i]);
            getCombination(k, n-candidates[i], count+1, i+1, c);
            c.pop_back();
        }
    }
};