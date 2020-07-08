//
// Created by 李恒 on 2020/7/8.
//
#include <iostream>
#include <set>
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
            sort(candidate_array.begin(),candidate_array.end());
            s.insert(candidate_array);
        }else if(partial_sum > target){
            return;
        }else{// partial_sum < target
            for(int i = idx; i < candidates.size(); ++i){
                cout << i << endl;
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