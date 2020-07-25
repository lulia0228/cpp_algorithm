//
// Created by LiHeng on 2020/4/21.
//

#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
#include <algorithm>
using namespace std;

// 从无重复元素数组中找到组合和为Target,元素使用次数随意。

//这个题目我觉得挺难的，有DP法和递归写法

//这个写法用的是DP思想，貌似速度很慢啊；下面换成  递归回溯+剪枝  看看怎么样
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        if(candidates.size() == 0)
            return {};
        unordered_map<int, set<vector<int>>> dict; //key是target,value是组合方式的集合
        for(int i = 1;i <= target; i++){     //从1到target一步步求解
            for(auto n:candidates){     //c++ 14以后才可以这么用的！！！
                if(n == i)
                    dict[i].insert(vector<int> {n}); //vector直接赋值的话要用花括号
                else if(i > n){    // 说明i可以通过由n加上其他数组合而来
                    for(auto tmp:dict[i-n]){    //对于i-n的每一种组合方法
                        tmp.push_back(n);
                        sort(tmp.begin(), tmp.end());
                        dict[i].insert(tmp);
                    }
                }
            }
        }
        vector<vector<int>> ret(dict[target].begin(), dict[target].end()); //用集合的迭代器生成二维vector
        return ret;
    }
};


//以下1~4都是递归写法


class Solution1 {
public:
    vector<vector<int>> res;
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> temp;
        __combinationSum1(candidates, target, temp, 0, 0);
        // __combinationSum2(candidates, target, temp, 0);
        return res;
    }
private:
    // 遍历路径求并和
    // temp: 存放可能为解的结果
    // start： 开始位置
    // temp_sum: vector<int> temp 现有元素的和， 用这个参数可以简化计算过程
    void __combinationSum1(vector<int>& candidates, int target, vector<int> temp, int temp_sum, int start){
        if(temp_sum == target){
            res.push_back(temp);
        }else if(temp_sum > target){
            return;
        }else{
            for(int i = start; i < candidates.size(); i++){
                temp.push_back(candidates[i]);
                __combinationSum1(candidates, target, temp, temp_sum + candidates[i], i);
                temp.pop_back(); // pop 是为了回溯， 也可以理解为不让此次循环 push 的数值带入下一个分支
            }
        }
    }
    // 在下一层寻找需要的元素数值
    // temp: 存放可能为解的结果
    // start： 开始位置
    // target: 当前与和相差的数值
    // 貌似目前为止，我觉得这个最好理解；时间上也貌似没有下面的方法快，不过这个对我来说 似乎好理解一点儿撒！！！！！！
    void __combinationSum2(vector<int>& candidates, int target, vector<int> temp, int start){
        if(target == 0){
            res.push_back(temp);
        }else{
            for(int i = start; i < candidates.size(); i++){
                if(target >= candidates[i]){
                    temp.push_back(candidates[i]);
                    __combinationSum2(candidates, target - candidates[i], temp, i);
                    temp.pop_back();
                }

            }
        }
    }
};



class Solution2{
public:
    vector<vector<int>> ans;
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        ans.clear();
        vector<int> cur;
        dfs(candidates, target, 0, cur);
        return ans;
    }

    void dfs(vector<int>& candidates, int target, int idx, vector<int>& cur) {
        if (target == 0) {
            ans.push_back(cur);
            return;
        }
        if(target < 0 )
            return;
        for (int i = idx; i<candidates.size(); i++) {
            cur.push_back(candidates[i]);
            dfs(candidates, target-candidates[i], i, cur);
            cur.pop_back();
        }
    }
};


class Solution3 {
public:
    vector<vector<int>> res;
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> cur;
        getCombination(candidates, 0, target, 0, cur);
        return res;
    }
    void getCombination(vector<int>& candidates, int partial_sum, int &target, int idx, vector<int> &cur){
        if(partial_sum == target) {
            res.push_back(cur);
            return;
        }
        if(partial_sum > target)
            return;
        for(int i = idx; i < candidates.size(); ++i){
            cur.push_back(candidates[i]);
            getCombination(candidates, partial_sum + candidates[i], target, i, cur);
            cur.pop_back();
        }

    }
};


//原题没说数组是有序的正整数数组,先排序，排序后可以剪枝
class Solution4 {
public:
    vector<vector<int>> ans;
    vector<vector<int>> combinationSum(vector<int> &candidates, int target) {
        ans.clear();
        sort(candidates.begin(), candidates.end());
        vector<int> cur;
        dfs(candidates, target, 0, cur);
        return ans;
    }

    void dfs(vector<int> &candidates, int target, int idx, vector<int> &cur) {
        if (target == 0) {
            ans.push_back(cur);
            return;
        }
        for (int i = idx; i < candidates.size(); i++) {
            //剪枝
            if (target < 0)
                break;
            cur.push_back(candidates[i]);
            dfs(candidates, target - candidates[i], i, cur);
            cur.pop_back();
        }
    }

};