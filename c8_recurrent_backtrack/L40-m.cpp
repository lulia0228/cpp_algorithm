//
// Created by 李恒 on 2020/7/8.
//
#include <iostream>
#include <set>
#include <algorithm>
#include <vector>

using namespace std;
class Solution {
public:
    set<vector<int>> s;
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<int> candidate_array;
        getCombination(candidates, candidate_array, 0, target, 0);
        vector<vector<int>> ret(s.begin(), s.end()); //用集合的迭代器生成二维vector
        return ret;
    }
    void getCombination(vector<int>& candidates, vector<int> &candidate_array, int partial_sum, int &target, int idx){
        if(partial_sum == target){
            //因为下面还要pop_backc andidate_array的最后一个元素，所以不能直接对andidate_array排序，另外使用tmp
            vector<int> tmp = candidate_array;
            sort(tmp.begin(),tmp.end());
            s.insert(tmp);
            return;
        }else if(partial_sum > target){
            return;
        }else{ // partial_sum < target
            for(int i = idx; i < candidates.size(); ++i){
                candidate_array.push_back(candidates[i]);
                getCombination(candidates, candidate_array, partial_sum + candidates[i], target, i+1);
                candidate_array.pop_back();

            }
        }
    }
};



int main(){
    vector<int> v = {2,5,2,1,2};
    vector<vector<int>> res = Solution().combinationSum2(v,5);
    for (auto item :res){
        for(auto i:item)
            cout << i << '\t';
        cout << endl;
    }
}

//利用set 去除重复 底层是红黑树 效率上会变慢
//优化思路：（1）先排序，再回溯，可以提前剪枝
//          （2）排序后，有利于去重

class Solution1 {
public:
    vector<vector<int>> res;
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(),candidates.end());
        vector<int> candidate_array;
        getCombination(candidates, candidate_array, 0, target, 0);
        return res;
    }
    void getCombination(vector<int>& candidates, vector<int> &candidate_array, int partial_sum, int target, int idx){
        if(partial_sum == target){
            res.push_back(candidate_array);
            return;
        }
        for(int i=idx; i<candidates.size(); ++i){
            //因为排序了，可以提前剪枝
            if (partial_sum+candidates[i] > target)
                break;
            //去重操作，设计巧妙，条件i!=idx很重要
            if (i!=idx&&candidates[i] == candidates[i-1])
                continue;
            candidate_array.push_back(candidates[i]);
            getCombination(candidates, candidate_array, partial_sum+candidates[i], target, i+1);
            candidate_array.pop_back();
        }
    }
};

//反向
class Solution2 {
public:
    vector<vector<int>> res;
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(),candidates.end());
        vector<int> candidate_array;
        getCombination(candidates, candidate_array, target, 0);
        return res;
    }
    void getCombination(vector<int>& candidates, vector<int> &candidate_array, int target, int idx){
        if(target == 0){
            res.push_back(candidate_array);
            return;
        }
        for(int i=idx; i<candidates.size(); ++i){
            //因为排序了，可以提前剪枝
            if (target-candidates[i] < 0)
                break;
            //去重操作，设计巧妙，条件i!=idx很重要
            if (i!=idx&&candidates[i] == candidates[i-1])
                continue;
            candidate_array.push_back(candidates[i]);
            getCombination(candidates, candidate_array, target-candidates[i], i+1);
            candidate_array.pop_back();
        }
    }
};

/*
2,5,2,1,2
2 5   -> 弹出5 回到第一个2所在的层，继续下探，插入 2 1
2 2 1 -> 弹出1 回到第二个2所在的层，继续下探，插入 2
2 2 2 -> 弹出2 回到第二个2所在的层，无法下探
2 2   -> 弹出2 回到第一个2所在的层，继续下探，插入 1 2
2 1 2 -> 弹出2 回到1所在的层，无法下探
2 1   -> 弹出1 回到第一个2所在的层，继续下探，插入 2
2 2   -> 弹出2 回到第一个2所在的层，无法下探
2     -> 弹出2 回到顶层，继续下探，插入 5
5     -> 弹出5, 回到顶层，继续下探，插入 2 1 2
2 1 2 -> 弹出2，回到1所在的层，无法下探
2 1   -> 弹出1，回到2所在的层，继续下探，插入2
2 2   -> 弹出2，回到第一个2所在的层，无法下探
2     -> 弹出2，回到顶层，继续下探，插入 1 2
1 2   -> 弹出2，回到1所在的层，无法下探
1     -> 弹出1，回到顶层，继续下探，插入2
2     -> 弹出2
结束
*/

